
from langchain.schema import AgentAction, AgentFinish
from langchain_core.messages import AIMessage, ToolMessage
from pydantic import BaseModel

from typing import List, Tuple, Union

class RoleParser(BaseModel):
    total_tokens: int = 0
    total_hit_tokens: int = 0
    total_miss_tokens: int = 0
    intermediate_steps: List[Tuple[AgentAction, AIMessage, ToolMessage]] = []

    def parse(self, message: AIMessage) -> Union[List[Tuple[AgentAction, str]], AgentFinish]:
        # 提取 token 使用情况
        token_usage = message.response_metadata.get("token_usage", {})
        total_tokens = token_usage.get("total_tokens", 0)

        self.total_tokens += total_tokens
        self.total_hit_tokens += token_usage.get("prompt_cache_hit_tokens", 0)
        self.total_miss_tokens += token_usage.get("prompt_cache_miss_tokens", 0)
        # 检查是否有 tool_calls
        if hasattr(message, "tool_calls") and message.tool_calls:
            actions = []
            for tool_call in message.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_call_id = tool_call["id"]
                actions.append((AgentAction(
                    tool=tool_name,
                    tool_input=tool_args,
                    log=f"{tool_name}({tool_args})"
                ), tool_call_id))
            if len(actions) > 1:
                raise ValueError("Only one tool call is allowed.")
            return actions
        # 如果没有 返回 AgentFinish
        intermediate_steps = self.intermediate_steps.copy()
        self.intermediate_steps = []
        return AgentFinish(
            return_values={"output": message,
                           "intermediate_steps": intermediate_steps},
            log=f"{message.content}"
        )

    def add_intermediate_step(self, step: AgentAction, message: AIMessage,
                              observation: ToolMessage):
        self.intermediate_steps.append((step, message, observation))
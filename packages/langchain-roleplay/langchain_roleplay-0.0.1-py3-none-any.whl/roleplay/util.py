import ast
import atexit
import builtins
from getpass import getpass
from os import environ
import os
import runpy
import signal
import tempfile
from yaml import load, dump, FullLoader

def get_yaml(file_path):
    """
    Reads a yaml file and returns the content as a dictionary.
    """
    with open(file_path, 'r') as stream:
        return load(stream, Loader=FullLoader)

def get_yaml_from_string(yaml_string):
    """
    Reads a yaml string and returns the content as a dictionary.
    """
    return load(yaml_string, FullLoader)

def write_yaml(data, file_path):
    """
    Writes a dictionary to a yaml file.
    """
    with open(file_path, 'w') as stream:
        dump(data, stream)

def set_if_undefined(var: str) -> None:
    """
    If the environment variable is not set, prompt the user to provide it.
    """
    if not environ.get(var):
        environ[var] = getpass(f"Please provide your {var}")

def get_env_var(var: str) -> str | None:
    """
    Get the value of an environment variable.
    """
    set_if_undefined(var)
    return environ.get(var)

class CodeRunner:
    def __init__(self):
        # 创建一个临时文件
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        self.temp_file_path = self.temp_file.name
        # 注册程序退出时的清理函数
        atexit.register(self.cleanup)
        # 注册信号处理函数
        self.register_signal_handlers()

    def run(self, code_string, init_globals):
        try:
            # 将代码写入临时文件
            with open(self.temp_file_path, 'w') as f:
                f.write(code_string)
            # 使用 runpy 运行临时文件中的代码
            return runpy.run_path(self.temp_file_path, init_globals=init_globals)
        except Exception as e:
            print(f"An error occurred while running the code: {e}")
            return {'result': f"An error occurred while running the code: {e}"}

    def cleanup(self):
        # 删除临时文件
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)
            print(f"Temporary file {self.temp_file_path} has been cleaned up.")

    def register_signal_handlers(self):
        # 捕获常见的终止信号（如 Ctrl+C 或 kill 命令）
        signal.signal(signal.SIGINT, self.handle_exit)
        signal.signal(signal.SIGTERM, self.handle_exit)

    def handle_exit(self, signum, frame):
        # 处理退出信号
        print(f"\nReceived signal {signum}, cleaning up...")
        self.cleanup()
        os._exit(1)

_code_runner = CodeRunner()
_show_map = {}

class SafeEval:
    """
    A class to evaluate expressions safely with a blacklist approach.
    Only import operations are prohibited; otherwise, most built-in functions are allowed.
    """
    LIST = {
        # 'ChatOpenAI': ChatOpenAI,
        '__name__': '__safe_eval__',
        '_show_map': _show_map,
        # 'AIMessage': AIMessage,
        # 'AgentAction': AgentAction,
        # 'AgentFinish': AgentFinish,
        # 'BaseOutputParser': BaseOutputParser,
        # 'OutputParserException': OutputParserException,
    }
    BLACKLIST = {
        'import', 'exec', 'eval', '__import__', 'globals', 'locals', 'open',
        'os', 'sys', 'exit', 'quit', 'getattr', 'setattr', 'delattr', 'execfile',
        'compile', 'input', 'repr', 'eval', 'exec', 'exit', 'os.system'
    }

    def __init__(self, extra_functions=None) -> None:
        self.code_runner = _code_runner
        # We will allow all built-ins except those in the blacklist
        self.safe_builtins = {name: func for name, func in builtins.__dict__.items() if name not in self.BLACKLIST}
        # self.safe_builtins = builtins.__dict__
        self.safe_builtins.update(self.LIST)
        if extra_functions:
            self.safe_builtins.update(extra_functions)

    def eval(self, expr: str, **variables):
        if not isinstance(expr, str):
            raise TypeError("Expression must be a string")

        # Check blacklist for dangerous operations
        self._check_blacklist(ast.parse(expr, mode='exec'))

        safe_builtins = self.safe_builtins.copy()
        safe_builtins.update(variables)
        # self.safe_builtins['_variables'] = variables
        try:
            # Execute the expression or statement
            # exec(expr, self.safe_builtins, variables)
            result = self.code_runner.run(expr, safe_builtins)
        except Exception as e:
            # Handle the exception and print the error message
            print(f"[SafeEval]: Error occurred: {e}")
            raise
        if 'result' in result:
            # If 'result' is in the variables, return its value
            return result['result']
        raise ValueError("No result found")

    def _check_blacklist(self, tree):
        for node in ast.walk(tree):
            # Check for import statements
            # if isinstance(node, (ast.Import, ast.ImportFrom)):
            #     raise ValueError("Import statements are not allowed")
            # Check for blacklisted names
            if isinstance(node, ast.Name) and node.id in self.BLACKLIST:
                raise ValueError(f"Operation '{node.id}' is not allowed")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                        and node.func.id in self.BLACKLIST:
                raise ValueError(f"Function '{node.func.id}' is not allowed")

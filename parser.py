import ast
import os

class CodeParser:
    def __init__(self, directory):
        self.directory = directory
        self.functions = {}
        self.calls = []

    def parse(self):
        for filename in os.listdir(self.directory):
            if filename.endswith(".py"):
                with open(os.path.join(self.directory, filename), "r") as file:
                    tree = ast.parse(file.read())
                    self.visit(tree)
        return self.functions, self.calls

    def visit(self, node):
        for child in ast.walk(node):
            if isinstance(child, ast.FunctionDef):
                self.functions[child.name] = {
                    "type": "function"
                }
                for n in ast.walk(child):
                    if isinstance(n, ast.Call):
                        if isinstance(n.func, ast.Name):
                            self.calls.append((child.name, n.func.id))
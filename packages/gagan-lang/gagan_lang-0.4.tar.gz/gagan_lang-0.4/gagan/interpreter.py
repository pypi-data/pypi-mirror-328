from .lexer import TokenType, tokenize, LexerError
from .parser import Parser, PrintNode, ScanNode, BinOpNode, AssignNode, ParserError, IfNode
import sys

class InterpreterError(Exception):
    def __init__(self, message, node=None, token=None):
        location = ""
        if node and hasattr(node, 'token') and node.token:
            location = f" at line {node.token.line}, column {node.token.column}"
        elif token:
            location = f" at line {token.line}, column {token.column}"
        super().__init__(f"Interpreter Error{location}: {message}")
        self.node = node
        self.token = token


class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, PrintNode):
            return self.visit_print_node(node)
        elif isinstance(node, ScanNode):
            return self.visit_scan_node(node)
        elif isinstance(node, AssignNode):
            return self.visit_assign_node(node)
        elif isinstance(node, BinOpNode):
            return self.visit_bin_op_node(node)
        elif isinstance(node, IfNode):
            return self.visit_if_node(node)
        else:
            raise InterpreterError(f"Unknown node type: {type(node).__name__}", node)

    def visit_print_node(self, node):
        value = self.evaluate(node.value)
        print(value)

    def visit_scan_node(self, node):
        identifier = node.identifier
        user_input = input("Enter a value: ").strip()  # Remove leading/trailing whitespace
        self.variables[identifier] = user_input

    def visit_assign_node(self, node):
        identifier = node.identifier
        self.variables[identifier] = self.evaluate(node.value)

    def _convert_to_number(self, value, node):
        if isinstance(value, (int, float)):
            return value
        try:
            return float(value)
        except ValueError:
            try:
                return int(value)
            except ValueError:
                if isinstance(value, str):
                    return value  # Treat as string for operations like concatenation
                raise InterpreterError(f"Operand must be a number or string convertible to number in binary operation", node)

    def _compare_values(self, left, op, right):
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise InterpreterError(f"Comparison requires numeric operands for '{op}'", None)
        
        if op == TokenType.EQUAL_TO:
            return left == right
        elif op == TokenType.NOT_EQUAL:
            return left != right
        elif op == TokenType.GREATER:
            return left > right
        elif op == TokenType.LESS:
            return left < right
        else:
            raise InterpreterError(f"Unknown comparison operator: {op}", None)

    def visit_bin_op_node(self, node):
        left_value = self.evaluate(node.left)
        right_value = self.evaluate(node.right)

        left_value = self._convert_to_number(left_value, node)
        right_value = self._convert_to_number(right_value, node)

        if node.op in (TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE):
            if node.op == TokenType.PLUS:
                # Allow for string concatenation if either operand is a string
                if isinstance(left_value, str) or isinstance(right_value, str):
                    return str(left_value) + str(right_value)
                return left_value + right_value
            elif node.op == TokenType.MINUS:
                if not isinstance(left_value, (int, float)) or not isinstance(right_value, (int, float)):
                    raise InterpreterError("Subtraction requires numeric operands", node)
                return left_value - right_value
            elif node.op == TokenType.MULTIPLY:
                if not isinstance(left_value, (int, float)) or not isinstance(right_value, (int, float)):
                    raise InterpreterError("Multiplication requires numeric operands", node)
                return left_value * right_value
            elif node.op == TokenType.DIVIDE:
                if not isinstance(left_value, (int, float)) or not isinstance(right_value, (int, float)):
                    raise InterpreterError("Division requires numeric operands", node)
                if right_value == 0:
                    raise InterpreterError("Division by zero", node)
                return left_value / right_value
        elif node.op in (TokenType.EQUAL_TO, TokenType.NOT_EQUAL, TokenType.GREATER, TokenType.LESS):
            return self._compare_values(left_value, node.op, right_value)
        else:
            raise InterpreterError(f"Unknown binary operator: {node.op}", node)

    def visit_if_node(self, node):
        condition = self.evaluate(node.condition)
        if condition:
            for statement in node.body:
                self.visit(statement)
        elif node.else_body:
            for statement in node.else_body:
                self.visit(statement)

    def evaluate(self, value):
        if isinstance(value, str) and value in self.variables:
            return self.variables[value]
        elif isinstance(value, BinOpNode):
            return self.visit_bin_op_node(value)
        return value


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Gagan-lang Interpreter")
    parser.add_argument('--version', action='version', version='%(prog)s 0.3')
    parser.add_argument('filename', nargs='?', help='The script file to run')
    args = parser.parse_args()

    if args.filename:
        filepath = args.filename
        try:
            with open(filepath, 'r') as file:
                code = file.read()
        except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        try:
            tokens = tokenize(code)
            parser = Parser(tokens)
            ast = parser.parse()
            interpreter = Interpreter()
            for node in ast:
                interpreter.visit(node)
        except LexerError as e:
            print(e)
        except ParserError as e:
            print(e)
        except InterpreterError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            import traceback
            traceback.print_exc()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
from .lexer import TokenType, Token

class AST:
    pass

class PrintNode(AST):
    def __init__(self, value):
        self.value = value

class ScanNode(AST):
    def __init__(self, identifier):
        self.identifier = identifier

class BinOpNode(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class AssignNode(AST):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class IfNode(AST):
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class ParserError(Exception):
    def __init__(self, message, token):
        super().__init__(f"Parser Error at line {token.line}, column {token.column}: {message} near '{token.value}'")
        self.token = token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self, expected_type=None):
        if self.pos >= len(self.tokens):
            return None
        token = self.tokens[self.pos]
        if expected_type and token.type != expected_type:
            return None
        return token

    def consume(self, expected_type):
        token = self.peek(expected_type)
        if not token:
            expected_str = expected_type.name if isinstance(expected_type, TokenType) else expected_type
            actual_token = self.tokens[self.pos] if self.pos < len(self.tokens) else Token(TokenType.EOF, 'EOF', -1, -1)  # Dummy EOF token for error message
            raise ParserError(f"Expected token type {expected_str}", actual_token)
        self.pos += 1
        return token

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens) and self.peek().type != TokenType.EOF:
            token = self.peek()
            if token.type == TokenType.GPRINT:
                nodes.append(self.parse_print_statement())
            elif token.type == TokenType.GSCAN:
                nodes.append(self.parse_scan_statement())
            elif token.type == TokenType.IDENTIFIER:
                nodes.append(self.parse_assignment_statement())
            elif token.type == TokenType.IF:
                nodes.append(self.parse_if_statement())
            else:
                raise ParserError(f"Unexpected token at top level", token)
        return nodes

    def parse_print_statement(self):
        self.consume(TokenType.GPRINT)
        value = self.parse_expression()
        return PrintNode(value)

    def parse_scan_statement(self):
        self.consume(TokenType.GSCAN)
        identifier_token = self.consume(TokenType.IDENTIFIER)
        return ScanNode(identifier_token.value)

    def parse_assignment_statement(self):
        identifier_token = self.consume(TokenType.IDENTIFIER)
        self.consume(TokenType.EQUAL)
        value = self.parse_expression()
        return AssignNode(identifier_token.value, value)

    def parse_if_statement(self):
        self.consume(TokenType.IF)
        condition = self.parse_expression()
        self.consume(TokenType.LBRACE)
        body = self.parse_block()
        else_body = None
        if self.peek() and self.peek().type == TokenType.ELSE:
            self.consume(TokenType.ELSE)
            self.consume(TokenType.LBRACE)
            else_body = self.parse_block()
        return IfNode(condition, body, else_body)

    def parse_block(self):
        nodes = []
        while self.peek() and self.peek().type != TokenType.RBRACE:
            if self.peek().type == TokenType.GPRINT:
                nodes.append(self.parse_print_statement())
            elif self.peek().type == TokenType.GSCAN:
                nodes.append(self.parse_scan_statement())
            elif self.peek().type == TokenType.IDENTIFIER:
                nodes.append(self.parse_assignment_statement())
            elif self.peek().type == TokenType.IF:
                nodes.append(self.parse_if_statement())
            else:
                raise ParserError("Expected statement in block", self.peek())
        self.consume(TokenType.RBRACE)
        return nodes

    def parse_expression(self):
        return self.parse_bin_op()

    def parse_bin_op(self, precedence=0):
        left = self.parse_primary()

        while True:
            op_token = self.peek()
            if not op_token or op_token.type not in (TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.EQUAL_TO, TokenType.NOT_EQUAL, TokenType.GREATER, TokenType.LESS):
                break

            # Here we could implement operator precedence but for simplicity, we treat all as equal
            self.consume(op_token.type)  # Consume the operator
            right = self.parse_primary()
            left = BinOpNode(left, op_token.type, right)
        return left

    def parse_primary(self):
        token = self.peek()
        if not token:
            actual_token = self.tokens[self.pos-1] if self.pos > 0 else Token(TokenType.EOF, 'EOF', -1, -1)
            raise ParserError("Expected primary expression", actual_token)

        if token.type == TokenType.NUMBER:
            return self.consume(TokenType.NUMBER).value
        elif token.type == TokenType.STRING:
            return self.consume(TokenType.STRING).value
        elif token.type == TokenType.IDENTIFIER:
            return self.consume(TokenType.IDENTIFIER).value
        elif token.type == TokenType.LPAREN:
            self.consume(TokenType.LPAREN)
            expr = self.parse_expression()
            self.consume(TokenType.RPAREN)
            return expr
        else:
            raise ParserError(f"Expected primary expression (number, string, identifier, or expression in parentheses)", token)
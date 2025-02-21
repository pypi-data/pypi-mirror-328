from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    GPRINT = auto()
    GSCAN = auto()
    IF = auto()
    ELSE = auto()
    # Literals
    STRING = auto()
    NUMBER = auto()
    IDENTIFIER = auto()
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EQUAL = auto()
    # Comparison
    EQUAL_TO = auto()
    NOT_EQUAL = auto()
    GREATER = auto()
    LESS = auto()
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    # End of file
    EOF = auto()

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value}, line={self.line}, col={self.column})"

class LexerError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"Lexer Error at line {line}, column {column}: {message}")
        self.line = line
        self.column = column

def tokenize(code):
    tokens = []
    i = 0
    line = 1
    column = 1
    while i < len(code):
        char = code[i]

        if char.isspace():
            if char == '\n':
                line += 1
                column = 1
            else:
                column += 1
            i += 1
            continue

        if char == '"':
            i += 1
            column += 1
            string = ''
            start_column = column
            while i < len(code) and code[i] != '"':
                string += code[i]
                if code[i] == '\n':
                    line += 1
                    column = 1
                else:
                    column += 1
                i += 1
            if i == len(code) or code[i] != '"':
                raise LexerError("Unterminated string", line, start_column)
            tokens.append(Token(TokenType.STRING, string, line, start_column))
            i += 1
            column += 1
        elif char.isdigit() or (char == '-' and i + 1 < len(code) and code[i + 1].isdigit()):
            num_str = ''
            start_column = column
            while i < len(code) and (code[i].isdigit() or code[i] == '.'):
                num_str += code[i]
                i += 1
                column += 1
            # Check if it's a valid number (int or float)
            try:
                if '.' in num_str:
                    tokens.append(Token(TokenType.NUMBER, float(num_str), line, start_column))
                else:
                    tokens.append(Token(TokenType.NUMBER, int(num_str), line, start_column))
            except ValueError:
                raise LexerError(f"Invalid number: {num_str}", line, start_column)
        elif char.isalpha() or char == '_':
            word = ''
            start_column = column
            while i < len(code) and (code[i].isalpha() or code[i] == '_' or code[i].isdigit()):
                word += code[i]
                i += 1
                column += 1
                if i < len(code):
                    char = code[i]
                else:
                    break

            if word == 'gprint':
                tokens.append(Token(TokenType.GPRINT, word, line, start_column))
            elif word == 'gscan':
                tokens.append(Token(TokenType.GSCAN, word, line, start_column))
            elif word == 'if':
                tokens.append(Token(TokenType.IF, word, line, start_column))
            elif word == 'else':
                tokens.append(Token(TokenType.ELSE, word, line, start_column))
            else:
                tokens.append(Token(TokenType.IDENTIFIER, word, line, start_column))
        else:
            start_column = column
            if char == '+':
                tokens.append(Token(TokenType.PLUS, '+', line, start_column))
            elif char == '-':
                tokens.append(Token(TokenType.MINUS, '-', line, start_column))
            elif char == '*':
                tokens.append(Token(TokenType.MULTIPLY, '*', line, start_column))
            elif char == '/':
                tokens.append(Token(TokenType.DIVIDE, '/', line, start_column))
            elif char == '=':
                if i + 1 < len(code) and code[i + 1] == '=':
                    tokens.append(Token(TokenType.EQUAL_TO, '==', line, start_column))
                    i += 1
                    column += 1
                else:
                    tokens.append(Token(TokenType.EQUAL, '=', line, start_column))
            elif char == '(':
                tokens.append(Token(TokenType.LPAREN, '(', line, start_column))
            elif char == ')':
                tokens.append(Token(TokenType.RPAREN, ')', line, start_column))
            elif char == '{':
                tokens.append(Token(TokenType.LBRACE, '{', line, start_column))
            elif char == '}':
                tokens.append(Token(TokenType.RBRACE, '}', line, start_column))
            else:
                raise LexerError(f"Unexpected character: '{char}'", line, start_column)
            i += 1
            column += 1

    tokens.append(Token(TokenType.EOF, 'EOF', line, column))
    return tokens
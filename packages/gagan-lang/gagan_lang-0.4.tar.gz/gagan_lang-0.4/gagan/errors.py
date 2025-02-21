class Error:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"Error: {self.message}"

class SyntaxError(Error):
    pass

class RuntimeError(Error):
    pass
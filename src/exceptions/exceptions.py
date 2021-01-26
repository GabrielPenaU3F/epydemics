class ExceptionWithMessage(Exception):

    def __init__(self, arg):
        self.strerror = str(arg)
        self.args = tuple(arg)
        super().__init__()


class InvalidArgumentException(ExceptionWithMessage):

    pass

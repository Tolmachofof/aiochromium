

class AIOChromiumException(Exception):
    pass


class InvalidParameters(AIOChromiumException):
    pass


class TabConnectionClosed(AIOChromiumException):
    """Raises when web socket connection to tab has been closed"""


class ErrorsHandler:
    pass


class ErrorProcessor:
    ERROR_CODES = {
        '-32602': InvalidParameters
        
    }
    
    @staticmethod
    def process(error):
        error_handler = ErrorProcessor.ERROR_CODES.get(str(error['code']),
                                                       AIOChromiumException)
        return error_handler(error['data'])
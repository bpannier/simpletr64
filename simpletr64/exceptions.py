class SimpleTR64Error(RuntimeError):
    pass


class RequestError(SimpleTR64Error):
    pass


class ParseError(RequestError):
    pass


class DeviceError(RequestError):
    pass

class SimpleTR64Error(RuntimeError):
    pass


class ParseError(SimpleTR64Error):
    pass


class DeviceError(SimpleTR64Error):
    pass

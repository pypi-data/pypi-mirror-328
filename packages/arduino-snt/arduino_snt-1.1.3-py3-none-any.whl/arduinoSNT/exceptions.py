class PinAlreadyUsedError(Exception):
    def __init__(self, message: str = "Another component is already connected to this pin."):
        super().__init__(message)

class PinNotUsedError(Exception):
    def __init__(self, message: str = "No component connected to this pin."):
        super().__init__(message)
class InvalidFormat(Exception):
    """Exception raised for errors in the cedula format.
    
    Methods
    -------
    __init__() -> None
        Initializes the error message for invalid cedula format.
    """
    
    def __init__(self) -> None:
        """Initializes an InvalidFormat error with a default message."""
        super().__init__("FormatError: Invalid cedula format")
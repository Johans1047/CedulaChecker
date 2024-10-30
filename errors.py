class InvalidFormat(Exception):
    
    def __init__(self):
        super().__init__("FormatError: Invalid ID format")

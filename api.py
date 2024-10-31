from cedula import CedulaChecker

class CedulaCheckerAPI(CedulaChecker):

    def __init__(self, cedula):
        super().__init__(cedula)

    def check(self):
        ced_type, province = super().validate()
        formatted_cedula, prefix, book, volume = super().format()

        result = {
            'pattern': self.cedula,
            'cedula': formatted_cedula,
            'type': ced_type,
            'province': province,
            'length': len(formatted_cedula),
            'prefix': prefix,
            'book': book,
            'volume': volume
        }

        return result
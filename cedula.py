import re
from errors import InvalidFormat

class CedulaChecker:
    def __init__(self, cedula):
        self.cedula = cedula
        self.pattern = r'^(1[0-3]|[1-9]|PE|E|N|(1[0-3]|[1-9])AV|(1[0-3]|[1-9])PI)-\d{1,4}-\d{1,6}$'
        self.cedula_splitted = None
        self.prefix_required_len = None
        self.book_required_len = None
        self.volume_required_len = None
        self.length = 14

    def validate(self) -> tuple[str, str]:
        """Validates the cedula format and returns its type and province.
        
        Returns
        -------
        tuple[str, str]
            The tag (cedula type) and the province associated with the prefix if applies.

        Raises
        ------
        InvalidFormat
            If the cedula does not match the expected pattern.
        """
        
        # Validate that the required format is met
        if not re.match(self.pattern, self.cedula):
            raise InvalidFormat()
        
        # Since the format is valid, we save the different parts of the cedula
        self.cedula_splitted = self.cedula.split("-")
        
        prefix = self.cedula_splitted[0]
        patterns = self.pattern_dict()
        
        # Initialize the default length requirements
        self.prefix_required_len = 0
        self.book_required_len = 0
        self.volume_required_len = 0
        
        # Verify the type of pattern that corresponds
        for prefix_regex, tag in patterns.items():
            if re.match(prefix_regex, prefix):
                if tag == 'Regular':
                    self.prefix_required_len = 2
                    self.book_required_len = 4
                    self.volume_required_len = 5
                elif tag in ['Panameno_Vigencia', 'Indigena']:
                    self.prefix_required_len = 4
                    self.book_required_len = 4
                    self.volume_required_len = 5
                elif tag in ['Extranjero', 'Naturalizado']:
                    self.prefix_required_len = 1
                    self.book_required_len = 4
                    self.volume_required_len = 5
                elif tag == 'Panameno_Extranjero':
                    self.prefix_required_len = 2
                    self.book_required_len = 4
                    self.volume_required_len = 6
                break  # Exit the loop upon finding a match
            
        provinces = self.province_dict()
        province = ''
        for number, prov in provinces.items():
            
            prefix_numbers = ''.join([character for character in prefix if character.isdigit()])
            
            if prefix_numbers == '':
                break
            
            if int(prefix_numbers) == number:
                province = prov
                break
        
        return tag, province
        
    def format(self) -> tuple[str, str, str, str]:
        """Formats the cedula to match the required format with leading zeros.
        
        Returns
        -------
        tuple[str, str, str, str]
            The formatted cedula string and individual parts (prefix, book, volume).
        """
        
        elements_required_len = [self.prefix_required_len, self.book_required_len, self.volume_required_len]
        
        for i in range(len(self.cedula_splitted)):
            part = self.cedula_splitted[i]
            required_len = elements_required_len[i]
            
            if len(part) == required_len: # if both lengths are equal, move to the next iteration
                continue
            
            self.cedula_splitted[i] = '0' * (required_len - len(part)) + part
        
        formatted_cedula = ''.join(self.cedula_splitted)
            
        formatted_cedula = formatted_cedula + '0' * (self.length - len(formatted_cedula))
            
        return formatted_cedula, self.cedula_splitted[0], self.cedula_splitted[1], self.cedula_splitted[2]
        
    def pattern_dict(self) -> dict[str, str]:
        """Provides a dictionary of regex patterns to identify cedula types.
        
        Returns
        -------
        dict[str, str]
            Dictionary with regex patterns as keys and cedula type tags as values.
        """
        regex_dict = {
            r'^(1[0-3]|[1-9])$': 'Regular',
            r'^PE$': 'Panameno_Extranjero',
            r'^E$': 'Extranjero',
            r'^N$': 'Naturalizado',
            r'^(1[0-3]|[1-9])AV$': 'Panameno_Vigencia',
            r'^(1[0-3]|[1-9])PI$': 'Indigena',
        }
        return regex_dict
    
    def province_dict(self) -> dict[int, str]:
        """Provides a dictionary of province codes and province names.
        
        Returns
        -------
        dict[int, str]
            Dictionary with province codes as keys and province names as values.
        """
        province_dict = {
            1: "Bocas del Toro",
            2: "Coclé",
            3: "Colón",
            4: "Chiriquí",
            5: "Darién",
            6: "Herrera",
            7: "Los Santos",
            8: "Panamá",
            9: "Veraguas",
            10: "Guna Yala",
            11: "Emberá Wounaan",
            12: "Ngäbe-Buglé",
            13: "Panamá Oeste"
        }
        return province_dict
        
        

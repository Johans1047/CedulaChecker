import re
from errors import InvalidFormat

class CedulaChecker:
    def __init__(self, cedula):
        self.cedula = cedula
        self.pattern = r'^(1[0-3]|[1-9]|PE|E|N|(1[0-3]|[1-9])AV|(1[0-3]|[1-9])PI)-\d{1,4}-\d{1,6}$'
        self.cedula_splitted = cedula.split("-")

    def validate(self):
        
        # Validamos que se cumpla el formato requerido
        if not re.match(self.pattern, self.cedula):
            raise InvalidFormat()
        
        prefix = self.cedula_splitted[0]
        patterns = self.pattern_dict()
        
        # SI SON LOS TAGS ['Regular', 'Panameno_Vigencia', 'Indigena'] hacer un province DICT
        
        # Inicializamos los requerimientos de longitud por defecto
        prefix_required_len = 0
        book_required_len = 0
        volume_required_len = 0
        
        # Verificamos cual es el tipo de patron correspondiente 
        for prefix_regex, tag in patterns.items():
            if re.match(prefix_regex, prefix):
                if tag in ['Regular', 'Panameno_Vigencia', 'Indigena']:
                    prefix_required_len = 2
                    book_required_len = 4
                    volume_required_len = 5
                elif tag in ['Extranjero', 'Naturalizado']:
                    prefix_required_len = 1
                    book_required_len = 4
                    volume_required_len = 5
                elif tag == 'Panameno_Extranjero':
                    prefix_required_len = 2
                    book_required_len = 4
                    volume_required_len = 6
                break  # Salir del bucle al encontrar una coincidencia
        
        #cedula_len = len(self.cedula) - 2 # si el formato es correcto dos caracteres que son guion no se cuentan
        
        # cedula_parts = self.cedula.split("-")
        
        # Obtenemos el total de caracteres para poder completar con la cantidad de 0s requerida
        # total_characters = 0
        # for i, part in enumerate(cedula_parts):
        #     print(i)
        #     part_len = len(part)
        #     total_characters = total_characters + part_len
               
        # print(total_characters)
        
        #total_characters = len(self.cedula) - 2 # si el formato es correcto dos caracteres que son guion no se cuentan
        
        
        # prefix_len = len(self.cedula_splitted[0])
        # book_len = len(self.cedula_splitted[1])
        # volume_len = len(self.cedula_splitted[2])
        
        return prefix_required_len, book_required_len, volume_required_len
        
        # return total_characters, prefix_required_len, book_required_len, volume_required_len
        
        # print(cedula_len, initial_prefix, volume)
        
        # total_characters = initial_prefix + book + volume
        
        # for i in range(14 - total_characters):
        #     self.cedula = self.cedula + '0'
        
        # print(self.cedula)
        
        # for part in cedula_parts:
        #     print(len(part))
        
        # # print(f"Hola, la cedula es {cedula_parts}.")
        
    def format(self, prefix_required_len, book_required_len, volume_required_len):
        
        elements_required_len = [prefix_required_len, book_required_len, volume_required_len]
        
        for i in range(len(self.cedula_splitted)):
            part = self.cedula_splitted[i]
            required_len = elements_required_len[i]
            
            if len(part) == required_len: # si ambas longitudes son iguales pasamos a la siguiente iteracion
                continue
            
            self.cedula_splitted[i] = '0' * (required_len - len(part)) + part
        
        # book = self.cedula_splitted[1]
        # print(book)
        # if book_len != 4:
        #     self.cedula_splitted[1] = '0' * (4 - book_len) + self.cedula_splitted[1] # que la cadena 0 se concatene las veces necesarias
        #     print(self.cedula_splitted[1])
        
        formatted_cedula = ''
        for part in self.cedula_splitted:
            formatted_cedula = formatted_cedula + part
            
        formatted_cedula = formatted_cedula + '0' * (14 - len(formatted_cedula))
            
        print(formatted_cedula)
        print(len(formatted_cedula))
        
    def pattern_dict(self):
        regex_dict = {
            r'^(1[0-3]|[1-9])$': 'Regular',
            r'^PE$': 'Panameno_Extranjero',
            r'^E$': 'Extranjero',
            r'^N$': 'Naturalizado',
            r'^(1[0-3]|[1-9])AV$': 'Panameno_Vigencia',
            r'^(1[0-3]|[1-9])PI$': 'Indigena',
        }
        return regex_dict
        
        

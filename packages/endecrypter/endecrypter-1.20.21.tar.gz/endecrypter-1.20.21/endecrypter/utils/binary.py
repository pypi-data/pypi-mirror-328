class Binary:
    """
    Una clase que proporciona métodos estáticos para la conversión entre texto y representación binaria.
    Methods
    -------
    text_to_binary(text: str) -> str
        Convierte una cadena de texto a su representación binaria.
        Parámetros:
            text (str): El texto a convertir.
        Retorna:
            str: La representación binaria del texto, con cada carácter 
            separado por espacios y representado en 8 bits.
    binary_to_text(binary: str) -> str
        Convierte una representación binaria a texto.
        Parámetros:
            binary (str): La cadena binaria a convertir, con cada byte 
            separado por espacios.
        Retorna:
            str: El texto decodificado de la representación binaria.
    """
    @staticmethod
    def text_to_binary(text: str) -> str:
        return ' '.join(format(ord(c), '08b') for c in text)

    @staticmethod
    def binary_to_text(binary: str) -> str:
        binary_list = binary.split(' ')
        return ''.join(chr(int(b, 2)) for b in binary_list)
class CaesarCipher:
    """
    Una implementación del cifrado César clásico.
    El cifrado César es una técnica de cifrado por sustitución donde cada letra en el texto original
    es reemplazada por una letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
    Methods:
        encrypt_caesar(text: str, shift: int) -> str:
            Encripta un texto usando el cifrado César.
            Args:
                text (str): El texto a encriptar.
                shift (int): El número de posiciones a desplazar cada letra.
            Returns:
                str: El texto encriptado.
        decrypt_caesar(text: str, shift: int) -> str:
            Desencripta un texto que ha sido cifrado con César.
            Args:
                text (str): El texto cifrado a desencriptar.
                shift (int): El número de posiciones que se usó para cifrar.
            Returns:
                str: El texto desencriptado.
    """
    
    @staticmethod
    def encrypt_caesar(text: str, shift: int) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def decrypt_caesar(text: str, shift: int) -> str:
        return CaesarCipher.encrypt(text, -shift)
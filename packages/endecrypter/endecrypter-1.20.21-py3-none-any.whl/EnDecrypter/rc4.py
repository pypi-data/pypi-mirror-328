def cifrar_rc4(key, plaintext):
    """
    Función para cifrar texto utilizando RC4.
    :param key: La clave secreta de cifrado
    :param plaintext: El texto plano a cifrar
    :return: El texto cifrado en bytes
    """
    # Inicialización de la S-box
    S = list(range(256))
    j = 0
    key_length = len(key)

    # Inicialización de la S-box usando la clave
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    # Cifrado
    i = j = 0
    result = []
    for byte in plaintext.encode():  # Convertimos el texto plano a bytes
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)  # XOR con el byte generado

    return bytes(result)

def descifrar_rc4(key, ciphertext):
    """
    Función para descifrar texto utilizando RC4.
    :param key: La clave secreta de cifrado
    :param ciphertext: El texto cifrado en bytes
    :return: El texto descifrado como string
    """
    # Inicialización de la S-box
    S = list(range(256))
    j = 0
    key_length = len(key)

    # Inicialización de la S-box usando la clave
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    # Descifrado
    i = j = 0
    result = []
    for byte in ciphertext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)  # XOR con el byte generado

    return bytes(result).decode()  # Convertimos el resultado de vuelta a string

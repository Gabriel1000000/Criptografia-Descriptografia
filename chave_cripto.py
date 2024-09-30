import base64
from cryptography.fernet import Fernet

class Chave:

    def __init__(self) -> None:
        pass

    def chave_cripto_personalizada(self) -> bytes:
        """
        Solicita que o usuario crie uma chave personalizada.
        """
        # Caso queira criar sua propria chave de critografia:
        print('Informe a chave de criptografia.')
        key = input(">").encode()
        key_32_bytes = base64.urlsafe_b64encode(key.ljust(32, b'\0'))
        # Criar o objeto Fernet com a chave personalizada
        cipher_personalisado = Fernet(key_32_bytes)
        print("\nChave de criptografia:")
        print(f"chave:{key}")
        print(f"chave bytes:{key_32_bytes}")
        # Sua chave de criptografia:
        # print(f"chave chave em 32 bytes:{key_32_bytes}")  
        return cipher_personalisado
    
    def chave_cripto(self) -> bytes:
        """
            Gera uma chave de criptografia
        """
        # Caso queira usar uma chave de criptografia gerada de forma aleatoria:
        key = Fernet.generate_key()
        cipher = Fernet(key)
        print("\nChave de criptografia:")
        print(f"chave:{key}")
        return cipher

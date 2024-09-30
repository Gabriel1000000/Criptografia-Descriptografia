import base64
from cryptography.fernet import Fernet

class Descriptografia:
    def __init__(self) -> None:
        pass

    def descriptografada(self, key: bytes, usuario: str, senha: str)-> None:
        """
            Descriptografa o usuario e a senha que foram fornecidos
        """
        cipher = Fernet(key)
        # Caso queira Descriptografar usuario e a senha:
        usuario_descriptografada = cipher.decrypt(usuario).decode('utf-8')
        senha_descriptografada = cipher.decrypt(senha).decode('utf-8')
        # Usuario e senha descriptografados:
        print("\nUsuario/Senhas descriptografadas:")
        print(f"Usuario descriptografada: {usuario_descriptografada}")
        print(f"Senha descriptografada: {senha_descriptografada}")
    
    
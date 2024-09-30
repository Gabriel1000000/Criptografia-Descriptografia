import base64
from cryptography.fernet import Fernet

class Criptografia:
    def __init__(self) -> None:
        pass

    def criptografada(self, cipher: Fernet, usuario: str, senha: str) -> None:
        """
            Criptografa o usuario e a senha que foram fornecidos
        """
        # Caso queira criptografar o usuario e senha:
        usuario_criptografada = cipher.encrypt(usuario.encode())
        senha_criptografada = cipher.encrypt(senha.encode())
        # return suario_criptografada, senha_criptografada
        # Usuario e senha descriptografados:
        print("\nUsuario/Senhas criptografadas:")
        print(f"Usuario criptografada: {usuario_criptografada}")
        print(f"Senha criptografada: {senha_criptografada}")

import base64
from chave_cripto import Chave
from criptografia import Criptografia
from cryptography.fernet import Fernet
from descritocrafia import Descriptografia


# chave de descriptografia -> KEY_GESAM_RPA
def solicita_chave():
    print("Informe a chave de critpografia:")

def tipo_crito(usuario:str, senha:str, chave: Chave, cripto: Criptografia) -> None:
    """
        Pergunta ao usuario qual tipo de Criptografia ele deseja. Uma que ele escolha a chave ou uma que a chave é aleatoria.
    """
    while True:    
        try:
            print("Para criptografar um usuario/senha digite[1] ")
            print("Para criptografar um usuario/senha com uma chave de criptografia personalisada digite[2]")
            resposta=int(input(">"))
        except Exception as e:
            print("Informe o valor que está no menu!")
            continue
        if resposta == 1:
            key=chave.chave_cripto()
            cripto.criptografada(key, usuario, senha)
            break
        elif resposta == 2:
            key_personalisada=chave.chave_cripto_personalizada()
            cripto.criptografada(key_personalisada, usuario, senha)
            break

def tipo_descrito(usuario:str, senha:str, descripto: Descriptografia) -> None:
    """
        Pergunta ao usuario qual tipo de Descriptografia ele deseja. Se a criptografia foi com a chave personalisada ou uma que a chave é aleatoria.
    """

    while True:    
        try:
            print("Para descriptografar um usuario/senha digite[1] ")
            print("Para descriptografar um usuario/senha com a chave de criptografia personalizada digite[2]")
            resposta=int(input(">"))
        except Exception as e:
            print("Informe o valor que está no menu!")
            continue
        if resposta == 1:
            print("Informe a chave de critpografia que foi gerada:")
            key=input(">")
            descripto.descriptografada(key, usuario, senha)
            break
        elif resposta == 2:
            print("Informe a chave de critpografia que você criou:")
            key = base64.urlsafe_b64encode(input(">").ljust(32, '\0').encode())
            descripto.descriptografada(key, usuario, senha)
            break

def menu(chave: Chave, cripto: Criptografia, descripto: Descriptografia) -> None:
    """
        Solicita ao usuario se ele quer criptografar, descriptografar ou sair do programa
    """
    while True:    
        try:
            print("Selecione uma das opções:")
            print("Se deseja criptografar digite [1]")
            print("Se deseja descriptografar digite [2]")
            print("Se deseja sair digite [3]")
            op=int(input(">"))
        except Exception as e:
            print("Informe o valor que está no menu!")
            continue
        if op == 1:
            usuario, senha = solicita_usuario_senha()
            tipo_crito(usuario, senha, chave, cripto)
            break
        elif op == 2:
            usuario, senha = solicita_usuario_senha_descriptografado()
            tipo_descrito(usuario,senha, descripto)
            break
        else:
            print("Obrigado por usar o codigo de criptografia!")
            exit()
        

def solicita_usuario_senha() -> str:
    """
        Solicita o usuario e a senha que deve ser criptografado.
    """
    print("informe o usuario que será criptografada:")
    # Criptografar a senha
    usuario=input("User ->")
    senha = input("Senha ->")
    return usuario, senha

def solicita_usuario_senha_descriptografado() -> str:
    """
        Solicita o usuario e a senha que deve ser descriptografado.
    """
    print("informe o usuario que será descriptografada:")
    # Criptografar a senha
    usuario=input("User criptografado -> ")
    senha = input("Senha criptografado -> ")
    return usuario, senha

def main() -> None:
    chave=Chave()
    cripto=Criptografia()
    descripto= Descriptografia()
    menu(chave, cripto, descripto)
    

if __name__ == "__main__":
    main()
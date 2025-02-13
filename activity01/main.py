def cadastrar_usuario(nome_arquivo):
    with open(nome_arquivo, 'a') as arquivo:
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
    
        arquivo.write(f"{nome}:{senha}\n")
        print("Usuário cadastrado com sucesso!")

def listar_usuarios(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print("Usuários cadastrados:")
            for linha in arquivo:
                usuario, _ = linha.strip().split(':')
                print(usuario)
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")

def login(nome_arquivo):
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                usuario, senha_armazenada = linha.strip().split(':')
                if usuario == nome and senha_armazenada == senha:
                    print("Login bem-sucedido!")
                    return
            print("Usuário ou senha incorretos.")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")

def main():
    nome_arquivo = "usuarios.txt"

    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Login")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario(nome_arquivo)
        elif opcao == '2':
            listar_usuarios(nome_arquivo)
        elif opcao == '3':
            login(nome_arquivo)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

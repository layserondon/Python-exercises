# Sistema de cadastro de usuários
# 1. Cadastro de 3 usuários
# 2. Login de usuário
# 3. Sair

while True:
    print("Bem-vindo ao sistema de cadastro de usuários")
    print("1. Cadastro de usuário")
    print("2. Login de usuário")
    print("3. Sair")

    escolha = int(input("Digite a opção desejada: "))

    if (escolha == 1):        
        for cadastro in range(1, 4):
            print("______Cadastre um novo usuário_______")
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            senha = input("Digite a senha do usuário (4 dígitos): ")
            print(f"_____Usuários cadastrados com sucesso!____\nNome: {nome}\nidade: {idade}\nSenha: ****")
            cadastro += 1
    elif (escolha == 2):
            print("_______Login de usuário_________")
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            print(f"Seja Bem-Vindo {nome}!")
    else:
        print("Saindo")
        break
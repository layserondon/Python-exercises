#Gerenciamento de Pedidos de uma empresa

while True:
    print(
        """ 1 - Cadastrar Cliente
            2 - Inserir Novo Atendimento
            3 - Importar Lista de Atendimento
            4 - Cancelar Atendimento
            5 - Concluir Atendimento
            6 - Listar Atendimentos Pendentes
            7 - Ordenar nomes
            8 - Procurar Atendimento
            9 - Mostrar Valor Total do Serviço
            10 - Mostrar Serivço Mais Caro 
            11 - Mostrar Serviço Mais Barato
            12 - Exportar Clientes
            13 - Importar Novos Clientes
            14 - Inverter Ordem de Atendimento 
            0 - Sair
            """ 
        )
    atendimentos = []
    atendimentos_outro = ['Thor - Shih-tzu', 'Amelia - Persa', 'Ônix - Husky', 'Violeta - Golden']

    escolha = int(input("Como podemos te ajudar? "))

    if escolha == 1:
        tutor = input("Nome do Responsável: ")
        pet = input("Nome do pet: ")
        raca = input("Raça do pet: ")
        servico = input("Serviços: [1-Banho, 2-Hidratação, 3-Tosa Hig., 4-Tosa da Raça, 5-Tosa Bebê, 6-Escovação]")
        novo_cadastro = print(tutor, pet, raca, servico)
        atendimentos.append(novo_cadastro)
        print(atendimentos)
    elif escolha == 2 :
        tutor = input("Nome do Tutor: ")
        pet = input("Nome do Pet: ")
        servico = input("Serviços: [1-Banho, 2-Hidratação, 3-Tosa Hig., 4-Tosa da Raça, 5-Tosa Bebê, 6-Escovação]")
        novo_atendimento = print(tutor, pet, servico)
        atendimentos.insert(-1, novo_atendimento)
        print(atendimentos)
    elif escolha == 3:
        atendimentos.extend(atendimentos_outro)
        print("Importação realizada com sucesso!")
        print(atendimentos)
    elif escolha == 4:
        for index, atendimentos in enumerate(atendimentos, start=1):
            print(index, atendimentos)
        cancelar_atend = input("Qual atendimento você quer cancelar? ")
        try:
            numero = int(cancelar_atend)
            atendimentos.remove(numero)
        except:
            print("Número inválido. [Atenção] A ação não foi concluída!")
            break
    elif escolha == 5:
        # Concluir Atendimento
        for index, atendimentos in enumerate(atendimentos, start=1):
            print(index, atendimentos)
        concluir = input("Qual atendimento foi concluído? ")
        try:
            numero = int(concluir)
            indice = numero - 1
            atendimentos.pop(indice)
        except:
            print("Número inválido. [Atenção] A ação não foi concluída!")
            break
    else:
        break



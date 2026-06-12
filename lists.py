#Gerenciamento de Pedidos de uma empresa

atendimentos = []
atendimentos_outro = ['Thor - Shih-tzu', 'Amelia - Persa', 'Ônix - Husky', 'Violeta - Golden']

while True:
    print(
        """ 1 - Cadastrar Cliente 
            2 - Inserir Novo Atendimento
            3 - Importar Lista de Atendimento
            4 - Cancelar Atendimento
            5 - Concluir Atendimento""")
        #     6 - Listar Atendimentos Pendentes
        #     7 - Ordenar nomes
        #     8 - Procurar Atendimento
        #     9 - Mostrar Valor Total do Serviço
        #     10 - Mostrar Serivço Mais Caro 
        #     11 - Mostrar Serviço Mais Barato
        #     12 - Exportar Clientes
        #     13 - Importar Novos Clientes
        #     14 - Inverter Ordem de Atendimento 
        #     0 - Sair
        #     """ 
        # )

    escolha = int(input("Como podemos te ajudar? "))

    if escolha == 1:

        tutor = input("Nome do Responsável: ")
        pet = input("Nome do pet: ")
        raca = input("Raça do pet: ")
        servico = input("Serviços: [Banho, Hidratação, Tosa Hig., Tosa da Raça, Tosa Bebê, Escovação]")
        novo_cadastro = f"{tutor} - {pet} - {raca} - {servico}"
        atendimentos.append(novo_cadastro)
        print(atendimentos)

    elif escolha == 2 :

        tutor = input("Nome do Tutor: ")
        pet = input("Nome do Pet: ")
        servico = input("Serviços: [1-Banho, 2-Hidratação, 3-Tosa Hig., 4-Tosa da Raça, 5-Tosa Bebê, 6-Escovação]") 
        novo_atendimento = f"{tutor} - {pet} - {servico}"
        atendimentos.insert(-1, novo_atendimento)
        print(atendimentos)

    elif escolha == 3:

        atendimentos.extend(atendimentos_outro)
        print(atendimentos)

    elif escolha == 4:
        if len(atendimentos) == 0:
            print("não há atendimentos para cancelar.")
        else:
            for index, atendimento in enumerate(atendimentos, start=1):
                print(index, atendimento)
            
            cancelar_atend = int(input("Qual atendimento você quer cancelar? "))
        
            if cancelar_atend >= 1 and cancelar_atend <= len(atendimentos):
                indice_real = cancelar_atend - 1
                atendimentos.pop(indice_real)
                print(f"Atendimento cancelado com sucesso!: {atendimentos}")
            else:
                print("Número inválido. [Atenção] A ação não foi concluída!")
                break

    elif escolha == 5:
        if len(atendimentos) == 0:
            print("Não há atendimentos para concluir!")
        else:
            for index, atendimento in enumerate(atendimentos, start=1):
                print(index, atendimento)

                concluir = int(input("Qual atendimento foi concluído? "))

            if concluir >= 1 and concluir <= len(atendimentos):
                indice_real = concluir - 1
                atendimentos.pop(indice_real)
                print(f"Atendimento realizado com sucesso! {atendimentos}")
    else:
        break

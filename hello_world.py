#Calculando a média de um aluno

nota1 = float(input("Digite a primerira nota:"))  # float para converter a string para um número decimal 
#input para digitar o valor

nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:      #if para verificar se a média é maior ou igual a 7
    print(f"Aprovado com média {media:.2f}")  # f-string para formatar a string e exibir o valor da média #.2f para exibir 2 casas decimais
else:               #else para verificar se a média é menor que 7
    print(f"Reprovado com média {media:.2f}")  # f-string para formatar a string e exibir o valor da média #.2f para exibir 2 casas decimais

#Coleta de dados de nota dos alunos
Num1 = float(input("Digite a nota do primeiro semestre: "))
Num2 = float(input("Digite a nota do segundo semestre: "))
Num3 = float(input("Digite a nota do terceiro semestre: "))
Num4 = float(input("Digite a nota do quarto semestre: "))

#equação para calcular a média dos alunos
Soma = Num1 + Num2 + Num3 + Num4
Media = Soma / 4

#imprime para o usuário a soma e a media usando o operador %
print("A soma entre:", Num1, ",", Num2, ",", Num3, "e", Num4,  "É igual a: %s"  %(Soma))
print("A média do aluno durante o semestre foi: %s" %(Media))
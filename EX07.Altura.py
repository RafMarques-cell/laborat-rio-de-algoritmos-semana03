Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura): 
Homens: (72.7 ∗ h) − 58
Mulheres: (62, 1 ∗ h) − 44, 7

# Recebe a altura (convertida para número decimal)
altura = float(input("Digite a altura em metros (ex: 1.75): "))

# Recebe o sexo do usuário e padroniza para maiúsculo
sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").strip().upper()

# Verifica o sexo e aplica a fórmula correspondente
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de {altura:.2f}m é: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de {altura:.2f}m é: {peso_ideal:.2f} kg")
else:
    print("Opção de sexo inválida! Use apenas 'M' ou 'F'.")

Digite a altura em metros (ex: 1.75): 1.80
Digite o sexo (M para Masculino, F para Feminino): m
O peso ideal para um homem de 1.80m é: 72.86 kg

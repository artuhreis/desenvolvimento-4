# Definindo a função da Calculadora
def calculadora (num1,num2,operacao):
    # Escolhendo qual operação irá realizar
    if operacao == 1:
        return  num1 + num2
    
    elif operacao == 2:
        return num1 - num2
    
    elif operacao == 3:
        return num1 * num2
    
    elif operacao == 4:
        return num1 / num2
    
    elif operacao > 4:
        return 0
    
# Coletando os Parâmetros
num1 = float(input("Digite o Primeiro Número: "))
num2 = float(input("Digite o Segundo Número: "))
operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

# Entregando o Resultado
resultado = calculadora(num1, num2, operacao)
print("O Resultado é " , resultado)

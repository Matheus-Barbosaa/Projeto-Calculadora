#Início do programa

print('Seja bem Vindo!')
print('Olá usuário vamos calcular?')

# Calculadora

print('Calculadora simples em Python!')
print('Operações: + , - , * , /')
print('Digite "sair" para encerrar.')

# Receber nome

operação =[]
while True:
# Escolher operação
    operacao = input('\nEscolha a operação (+, -, *, /) ou "sair": ')

# Encerrar programa
    if operacao == 'sair':
        print('Saindo do programa...')
        break    

 # Verificar operação válida
    if operacao not in ['+', '-', '*', '/']:
        print('Operação inválida!')
        continue

    nome = input('Digite seu nome: ')
    print(f'Olá {nome}, vamos calcular!')


# Receber números
    num_1 = float(input('Digite o primeiro número: '))
    num_2 = float(input('Digite o segundo número: '))

 # Fazer cálculo
    if operacao == '+':
        resultado = num_1 + num_2

    elif operacao == '-':
        resultado = num_1 - num_2

    elif operacao == '*':
        resultado = num_1 * num_2

    elif operacao == '/':
        if num_2 != 0:
            resultado = num_1 / num_2
        else:
            print('Erro: divisão por zero não é permitida!')
            continue
    # Mostrar resultado
    print(f'Resultado: {resultado}')
    print('Fim do programa')



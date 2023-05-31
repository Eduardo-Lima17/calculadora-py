from time import sleep

# IMPRIMINDO O NOME CALCULADORA NA TELA
print('='*130)
print(f"{'C A L C U L A D O R A  E M  P Y T H O N': >83}")
print('='*130)

# DECLARANDO FUNÇÕES - Função são blocos de código que realizam determinadas tarafes
#que normalmente precisam ser executadas diversas vezes dentro de uma aplicação.

def adicao():
    valor1 = float(input('\nDigite um número: '))
    valor2 = float(input('Digite outro número: '))
    print('\nValor de adição é: ', valor1 + valor2)

def subtracao():
    valor1 = float(input('\nDigite um número: '))
    valor2 = float(input('Digite outro número: '))
    print('\nValor de subtração é: ', valor1 - valor2)

def multiplicacao():
    valor1 = float(input('\nDigite um número: '))
    valor2 = float(input('Digite outro número: '))
    print('\nValor da multiplicação é: ', valor1 * valor2)

def divisao():
    valor1 = float(input('\nDigite um número: '))
    valor2 = float(input('Digite outro número: '))
    print('\nValor da divisão é: ', valor1 / valor2)

opcao = 1

# OPERAÇÕES

while opcao:

    try:
        print('-'*20)
        print('O P E R A D O R E S')
        print('-'*20)
        print('\n0 - Sair \
                1 - Adição \
                2 - Subtração \
                3 - Multiplicação \
                4 - Dividir ')
        
        opcao = int(input('\nEscolha a opção: '))

        if opcao == 1:
            adicao()

        elif opcao == 2:
            subtracao()

        elif opcao == 3:
            multiplicacao()

        elif opcao == 4:
            divisao()

        else:
            print('='*130)
            print(f"{'C A L C U L A D O R A  E N C E R R A D A':>83}")
            print(f"{'Até mais!':>65}")
            print('='*130)

    except:
        print('='*120)
        print(f"{'A T E N Ç Ã O':>69}")
        print(f"{'Escolha uma das opções abaixo!':>80}")
        print('='*120)

        sleep(2)

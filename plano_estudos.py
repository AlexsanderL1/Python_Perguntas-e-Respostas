import time
import os

#Funções:

def ajuda():    #Função de ajuda
    os.system('cls' if  os.name == 'nt' else 'clear')
    print('*****Ajuda*****\n')
    print('---Tipos Primitivos:---'           #Tipos Primitivos
          '\nint => Inteiros, Sem decimais'
          '\nfloat=> Numeros Reais,flutuantes ou Com decimais'
          '\n'
          'bool=> Booleanos, True ou False'
          '\nstr=> String, palavras.\n'
          )

    print('---Operadores Aritiméticos:---'    #Operadores Aritiméticos
          '\nSoma=> +'
          '\nSubtração=> -'
          '\nMultiplicação=> *'
          '\nDivisão=> /'
          '\nDivisão Inteira=> //'
          '\nPotência=> **'
          '\n')
    print('---Ordem de Precedência:---'       #Ordem de Precedencia
          '\n1° ()'
          '\n2° **'
          '\n3° * , /, //, %'
          '\n4° +, -\n '
          )

def tipos_primitivos(): #Função Tipos Primitivos
    # Tipos Primitivos
    print('1. Vamos começar pelos tipos primitivos !\n\n')

    while True:
        print('1.1 Para numeros inteiros digitamos:(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == 'int':
            print('EXATO!\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.2 Para números com casas decimais, números reais e etc. digitamos:(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == 'float':
            print('EXATO!\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.3 E para verdadeiro ou falso?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == 'bool':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.4 Para frases, palavras e afins?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == 'str':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def operadores_matematicos():   #Função Operadores Aritiméticos
    # Operadores Matemáticos

    print('2. Operadores matemáticos! Chegou sua hora\n\n')

    while True:
        print('2.1 Sinal de soma no python:(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '+':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('2.2 Sinal para subtração:(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '-':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('E que tal divisão?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '/':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('multiplicação é facil, mas fala ai qual é:(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '*':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('Agora é mais dificil, e Potência ?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '**':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('Divisão Inteira? e ai? lembra?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '//':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('E o resto da divisão?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '%':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def ordem_de_precedencia(): #Função Ordem de Precedência
    # Ordem de Precedencia

    print('3. Vamos a ordem de precedêcia !\n\n')
    while True:
        print('3.1 Qual a prioridade 1?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '()':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.2 Qual a ordem de procedência 2 ?(Digite "help" para ajuda)')
        resp = input().lower().strip()
        if resp == '**':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.3 Qual a ordem de procedência 3?(Digite "help" para ajuda)')
        resp = input('Digite na sequência(multiplicação, Divisão, Divisão Inteira, Resto da Divisão)separando por espaços:\n').lower().strip()
        if resp == ("* / // %"):
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.4 Por ultimo, ordem de procedência 4?(Digite "help" para ajuda)')
        resp = input('Na sequência (soma, subtração) separado por espaços:\n')
        if resp == '+ -':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def todos():    #Função Todos
    tipos_primitivos()
    operadores_matematicos()
    ordem_de_precedencia()






while True:
    print('-'*5,'Estudando Python','-'*5)    #Apresentação

    entrada = input('\nDigite por onde quer começar:'
                   '\n0- Todos '
                   '\n1- Tipos Primitivos'
                   '\n2- Operadores Aritimeticos'
                   '\n3- Ordem de Precedência'
                   '\n\n--> Digite o Número: '
    )
    try:
            num = int(entrada)
            if num == 0:
                todos()
                break
            elif num == 1:
                tipos_primitivos()
                break
            elif num == 2:
                operadores_matematicos()
                break
            elif num == 3:
                ordem_de_precedencia()
                break
            else:
                os.system('cls' if  os.name == 'nt' else 'clear')
                print('ERRO : Número ainda não implementado')
                time.sleep(1)

    except ValueError:
        os.system('cls' if  os.name == 'nt' else 'clear')
        print('ERRO : Digite apenas números')
        time.sleep(1)
        
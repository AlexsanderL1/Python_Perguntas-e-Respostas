#Funções:
def ajuda():
    print('\nTipos Primitivos:\nint => Inteiros, Sem decimais\nfloat=> Numeros Reais,flutuantes ou Com decimais\n'
          'bool=> Booleanos, True ou False\nstr=> String, palavras.')
    print('\nOperadores Aritiméticos:\nSoma=> +\nSubtração=> -\nMultiplicação=> *\nDivisão=> /\nDivisão Inteira=> //'
          '\nPotência=> **\n')
    print('\nOrdem de Precedência:\n1° ()\n2° **\n3° * , /, //, %\n4° +, -\n ')

def tipos_primitivos():
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

def operadores_matematicos():
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

def ordem_de_precedencia():
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
    resp = input(
            'Digite na sequência(multiplicação, Divisão, Divisão Inteira, Resto da Divisão)separando por espaços:\n').lower().strip()
        if resp == '* / // %':
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


def todos():
    tipos_primitivos()
    operadores_matematicos()
    ordem_de_precedencia()


#Apresentação
print('-'*5,'Plano de Estudos do Alex','-'*5)

indice = int(input('\nDigite por onde quer começar:\n0- Todos \n1- Tipos Primitivos\n2- Operadores Aritimeticos\n3- Ordem de Precedência\n'))
if indice == 1 :
    tipos_primitivos()



elif indice == 2:
    operadores_matematicos()


elif indice == 3:
    ordem_de_precedencia()

elif indice == 0:
    todos()


else:
    print('Ainda não implementado')

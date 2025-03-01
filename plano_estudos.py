import time
import os

#Funções:

def ajuda():                    #Função de ajuda
    #Ajuda com todas as informações necessárias
    os.system('cls' if  os.name == 'nt' else 'clear')
    print('===== Ajuda =====\n')
    print('---Tipos Primitivos:---\n'           #Tipos Primitivos
          '\nint => Inteiros, Sem decimais'
          '\nfloat=> Numeros Reais,flutuantes ou Com decimais'
          '\nbool=> Booleanos, True ou False'
          '\nstr=> String, palavras.\n')

    print('--- Operadores Aritiméticos ---\n'    #Operadores Aritiméticos
          '\nSoma=> +'
          '\nSubtração=> -'
          '\nMultiplicação=> *'
          '\nDivisão=> /'
          '\nDivisão Inteira=> //'
          '\nPotência=> **\n')

    print('--- Ordem de Precedência ---\n'       #Ordem de Precedencia
          '\n1° ()'
          '\n2° **'
          '\n3° * , /, //, %'
          '\n4° +, -\n')

    print('--- Manipulação de Texto ---\n'        #Manipulação de Texto
          '\n1- A contagem de caracteres começa do 0'
          '\n2- Para selecionar um caractere específico dentro de uma string, usamos []'
          '\n3- Para selecionar uma sequência de caracteres, usamos [:]'
          '\n4- Antes do ":" é o início da seleção e depois do ":" é o fim da seleção'
          '\n5- Usando mais um ":" podemos definir o pulo da seleção, ou seja, os caracteres que serão ignorados'
          '\n6- Por exemplo: [::2] seleciona todos os caracteres pulando de 2 em 2'
          '\n7- Usando len() podemos contar quantos caracteres tem uma string'
          '\n8- Usando .count() podemos contar quantas vezes uma palavra ou caractere aparece em uma string'
          '\n9- Usando .find() podemos encontrar a posição de uma palavra ou caractere em uma string'
          '\n10- Usando .replace() podemos substituir uma palavra ou caractere por outro em uma string'
          '\n11- O .replace() é usado da seguinte forma: .replace("palavra a ser substituída","palavra nova")'
          '\n12- Usando .upper() podemos transformar todos os caracteres em maiúsculo'
          '\n13- Usando .lower() podemos transformar todos os caracteres em minúsculo'
          '\n14- Usando .capitalize() podemos transformar o primeiro caractere em maiúsculo'
          '\n15- Usando .title() podemos transformar o primeiro caractere de cada palavra em maiúsculo'
          '\n16- Usando .strip() podemos remover espaços em branco no início e no fim da string'
          '\n17- Usando .split() podemos dividir uma string em uma lista de palavras'
          '\n18- Usando .join() podemos juntar palavras de uma lista em uma string'
          '\n19- O .join() é usado da seguinte forma: " ".join(lista)\n')

def tipos_primitivos():         #Função Tipos Primitivos
    # Tipos Primitivos
    print('\n1. Vamos começar pelos tipos primitivos !\n\n')

    while True:
        print('1.1 Para numeros inteiros digitamos:(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == 'int':
            print('EXATO!\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.2 Para números com casas decimais, números reais e etc. digitamos:(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == 'float':
            print('EXATO!\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.3 E para verdadeiro ou falso?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == 'bool':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('1.4 Para frases, palavras e afins?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == 'str':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def operadores_matematicos():   #Função Operadores Aritiméticos
    # Operadores Matemáticos

    print('\n2. Operadores matemáticos! Chegou sua hora\n\n')

    while True:
        print('2.1 Sinal de soma no python:(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '+':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('2.2 Sinal para subtração:(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '-':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('E que tal divisão?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '/':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('multiplicação é facil, mas fala ai qual é:(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '*':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('Agora é mais dificil, e Potência ?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '**':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('Divisão Inteira? e ai? lembra?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '//':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('E o resto da divisão?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '%':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def ordem_de_precedencia():     #Função Ordem de Precedência
    # Ordem de Precedência
    print('\n3. Vamos a ordem de precedêcia !\n\n')
    while True:
        print('3.1 Qual a prioridade 1?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '()':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.2 Qual a ordem de procedência 2 ?(Digite "help" para ajuda)')
        resp = input('Sua Resposta: ').lower().strip()
        if resp == '**':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.3 Qual a ordem de procedência 3?(Digite "help" para ajuda)')
        resp = input('Digite na sequência (multiplicação, Divisão, Divisão Inteira, Resto da Divisão) separando por espaços:\nSua Resposta: ').lower().strip()
        if resp == ("* / // %"):
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('3.4 Por ultimo, ordem de procedência 4?(Digite "help" para ajuda)')
        resp = input('Na sequência (soma, subtração) separado por espaços:\nSua Resposta: ')
        if resp == '+ -':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def manipulacao_texto():        #Função Manipulação de Texto
    print('\n4. Manipulação de Cadeias de Texto! Esse será mais difícil e longo...\n\n')
    while True:
        frase= 'frase = Estou aprendendo Python'
        print('4.1 Como selecionar o 2° caractere dentro de uma frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '[1]':
            print('EXATO!')
            break
        elif resp == 'help':
            print('Dica: Lembre-se que a contagem começa do 0')
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('4.2 Como selecionar os 5 primeiros caracteres?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '[:5]':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')
    
    while True:
        print('4.3 Como selecionar os caracteres pulando de 2 em 2?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '[::2]':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')
    
    while True:
        print('4.4 Como contar quantos caracteres tem uma frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: len(frase)').lower().strip()
        if resp == 'len(frase)':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('4.5 Como contar quantas vezes a palavra "Python" aparece na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '.count("Python")':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('4.6 Como encontrar a posição da palavra "Python" na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '.find("Python")':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

    while True:
        print('4.7 Como substituir a palavra "Python" por "Java" na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\nSua Resposta: frase').lower().strip()
        if resp == '.replace("Python","Java")':
            print('EXATO!')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('ERRADO! Tente de novo!')

def todos():                    #Função Todos
    tipos_primitivos()
    operadores_matematicos()
    ordem_de_precedencia()
    manipulacao_texto()
    print('Parabéns, você concluiu todas as questões! Você é incrivel!')
    creditos()

def creditos():                 #Contatos e Créditos
    os.system('cls' if  os.name == 'nt' else 'clear') 
    print('''
-------------------- Desenvolvido por Alexsander Lucio Barboza --------------------
Email: alexlucio.dev@gmail.com || Linkedin: /alexsanderlucio || Github: /AlexsanderL1
        ''')

#Loop Principal com as opções

while True:
    print('-'*5,'Estudando Python','-'*5)    #Apresentação

    entrada = input(                         #Menu de Opções
        '''\nDigite por onde quer começar:
        0- Todos 
        1- Tipos Primitivos
        2- Operadores Aritimeticos
        3- Ordem de Precedência
        4- Manipulação de Cadeias de Texto
        ___________________________________
        77- Contatos do Desenvolvedor
        99- Ajuda - Dicas e Informações
        \n--> Digite o Número: '''
    )
    try:                                     #Direcionamento de acordo com a opção escolhida
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
            elif num == 4:
                manipulacao_texto()
                break
            elif num == 77:
                creditos()
                break
            elif num == 99:
                ajuda()
                break
            else:
                os.system('cls' if  os.name == 'nt' else 'clear')
                print('ERRO : Número ainda não implementado')
                time.sleep(1)

    except ValueError:                      #Tratamento de Erro
        os.system('cls' if  os.name == 'nt' else 'clear')
        print('ERRO : Digite apenas números')
        time.sleep(1)
        
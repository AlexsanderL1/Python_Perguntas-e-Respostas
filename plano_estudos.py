import time
import os

#Funções:

def ajuda():                    #Função de Ajuda
    os.system('cls' if  os.name == 'nt' else 'clear')
    print('\033[33m===== Ajuda =====\n')
    print('---Tipos Primitivos:---\033[34m\n'                   #Tipos Primitivos
          '\nint    => Números Inteiros'
          '\nfloat  => Números Reais, com casas decimais'
          '\nbool   => Booleano, Verdadeiro ou Falso'
          '\nstr    => String, textos alfanuméricos\n')

    print('\033[33m--- Operadores Aritiméticos ---\033[34m\n'   #Operadores Aritiméticos
          '\nSoma           => +'
          '\nSubtração      => -'
          '\nMultiplicação  => *'
          '\nDivisão        => /'
          '\nDivisão Inteira=> //'
          '\nMódulo         => %'
          '\nPotência       => **\n')

    print('\033[33m--- Ordem de Precedência ---\033[34m\n'      #Ordem de Precedencia
          '\n1° ()'
          '\n2° **'
          '\n3° * , /, //, %'
          '\n4° +, -\n')

    print('\033[33m--- Manipulação de Texto ---\033[34m\n'      #Manipulação de Texto
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n1. Vamos começar pelos tipos primitivos !\n\n')

    while True:
        print('1.1 Para numeros inteiros digitamos:(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'int':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('1.2 Para números com casas decimais, números reais e etc. digitamos:(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'float':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('1.3 E para verdadeiro ou falso?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'bool':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('1.4 Para frases, palavras e afins?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'str':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

def operadores_matematicos():   #Função Operadores Aritiméticos
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n2. Operadores matemáticos! Chegou sua hora\n\n')

    while True:
        print('2.1 Sinal de soma no python:(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '+':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('2.2 Sinal para subtração:(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '-':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('E que tal divisão?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '/':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('multiplicação é facil, mas fala ai qual é:(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '*':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('Agora é mais dificil, e Potência ?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '**':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('Divisão Inteira? e ai? lembra?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '//':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('E o resto da divisão?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '%':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

def ordem_de_precedencia():     #Função Ordem de Precedência
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n3. Vamos a ordem de precedêcia !\n\n')
    while True:
        print('3.1 Qual a prioridade 1?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '()':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('3.2 Qual a ordem de procedência 2 ?(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '**':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('3.3 Qual a ordem de procedência 3?(Digite "help" para ajuda)')
        resp = input('Digite na sequência (multiplicação, Divisão, Divisão Inteira, Resto da Divisão) separando por espaços:\n\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == ("* / // %"):
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:
        print('3.4 Por ultimo, ordem de procedência 4?(Digite "help" para ajuda)')
        resp = input('Na sequência (soma, subtração) separado por espaços:\n\033[33mSua Resposta :\033[34m ')
        if resp == '+ -':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

def manipulacao_texto():        #Função Manipulação de Texto
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n4. Manipulação de Cadeias de Texto! Esse será mais difícil e longo...\n\n')
    frase= 'Estou aprendendo Python'

    while True:                 #Questão 4.1
        print('4.1 Como selecionar o 2° caractere dentro de uma frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '[1]':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('Dica: Lembre-se que a contagem começa do 0\n')
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:                 #Questão 4.2
        print('4.2 Como selecionar os 5 primeiros caracteres?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '[:5]':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('Dica: O Fim é não é incluso na seleção')
            print('Dica: [Inicio:Fim:Pulo]\n')
            print('\033[31mERRADO!\033[34m Tente de novo!')
    
    while True:                 #Questão 4.3
        print('4.3 Como selecionar os caracteres pulando de 2 em 2?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '[::2]':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('Dica: [Inicio:Fim:Pulo]')
            print('\033[31mERRADO!\033[34m Tente de novo!')
    
    while True:                 #Questão 4.4
        print('4.4 Como contar quantos caracteres tem uma frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'len(frase)':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:                 #Questão 4.5
        print('4.5 Como contar quantas vezes a palavra "Python" aparece na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '.count("python")' or resp == ".count('python')":
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:                 #Questão 4.6
        print('4.6 Como encontrar a posição da palavra "Python" na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '.find("python")' or resp == ".find('python')":
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

    while True:                 #Questão 4.7
        print('4.7 Como substituir a palavra "Python" por "Java" na frase?(Digite "help" para ajuda)')
        print('A Frase a ser usada será: ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '.replace("python","java")' or resp == ".replace('python','java')":
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO!\033[34m Tente de novo!')

def todos():                    #Função Todos
    tipos_primitivos()
    operadores_matematicos()
    ordem_de_precedencia()
    manipulacao_texto()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-'*5,'Parabéns, você concluiu todas as questões! Você é incrivel!','-'*5)
    creditos()

def creditos():                 #Contatos e Créditos
    print('''\033[33m
----------------------Desenvolvido por Alexsander Lucio Barboza----------------------\033[34m
Email: alexlucio.dev@gmail.com || Linkedin: /alexsanderlucio || Github: /AlexsanderL1
        \033[0m''')

#Loop Principal com as opções

while True:
    print('-'*5,'\033[34mEstudando \033[33mPython\033[0m','-'*5)    #Apresentação

    entrada = input(                                                #Menu de Opções
        '''\n\033[33mDigite por onde quer começar\033[36m:
        0- Todos 
        1- Tipos Primitivos
        2- Operadores Aritimeticos
        3- Ordem de Precedência
        4- Manipulação de Cadeias de Texto
        \033[33m___________________________________
        77- Contatos do Desenvolvedor
        99- Ajuda - Dicas e Informações\033[32m
        \n--> Digite o Número: \033[34m'''
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
        print('\033[31mERRO : Digite apenas números\033[34m')
        time.sleep(1)
        
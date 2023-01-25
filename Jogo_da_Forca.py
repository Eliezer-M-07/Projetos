def jogo():
    
    # BIBLIOTECA PYTHON PARA SORTEAR A PALAVRA
    from random import choice

    chances = 5

    # PALAVRAS A SEREM DESCOBERTAS
    palavras = ['Macaco', 'Borboleta', 'Babuino', 'Pessoa', 'Megafone', 'Tesoura', 'Notebook','Maçã', 'Mouse', 'Teclado', 'Quadro']

    #PEGANDO UMA DAS PALAVRAS
    palavra_secreta = choice(palavras)

    usuario = input('Informe seu nome: ')

    # INFORMAÇÕES
    print('A palavra tem {} letras. Você possui {} chances.'.format(len(palavra_secreta),chances))

    # ESCONDENDO A PALAVRA
    P = ['_'] * len(palavra_secreta)

    # PALAVRAS TENTADAS E ACERTADAS
    t = []
    # MOSTRANDO PALAVRA
    P[0] = palavra_secreta[0]
    print(' '.join(P))

    while True:

        # SOLICITANDO UMA LETRA
        l = input('Informe uma letra: ')

        # VERIFICAÇÃO CASO LETRA JA TENHA SIDO USADA
        if l in t:
            print('\nVocê já tentou esta letra.\n')
            continue
        
        # CONDIÇÃO CASO SEJA INFORMADO MAIS DE UMA LETRA
        if len(l) >= 2:
            print('\nInforme somente uma letra.\n')
            continue

        # CONDIÇÃO CASO O USUARIO NÃO INFORME NADA
        if l == '':
            continue

        # VERIFICAÇÃO SE A LETRA INFORMADA ESTÁ NA PALAVRA E CASO ESTEJA ATRIBUINDO A POSIÇÃO
        if l in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == l:
                    P[i] = palavra_secreta[i]

            # VERIFICAÇÃO CASO TENHA ACERTADO TODAS AS LETRAS E ASSIM GANHANDO
            if '_' not in P:
                print('\nParabéns {} você venceu! a palavra era {}!'.format(usuario, palavra_secreta)) 
                break
            t.append(l)
            print('\nParabéns {} você acertou uma letra!'.format(usuario))
        print(' '.join(t))
        print(' '.join(P))

        # VERIFICAÇÃO CASO A LETRA NÃO ESTEJA NA PALAVRA E ASSIM DIMINUINDO UMA CHANCE
        tx = l in palavra_secreta
        if tx == False:
            chances = chances - 1
            t.append(l)

            if chances == 0:
                print('\nQue pena {} você perdeu.\n'.format(usuario))
                break
            print('\nErrado, Letra não está na palavra. Você tem {} chances\n'.format(chances))

# CHAMANDO FUNÇÃO PARA INICIAR O JOGO
jogo()

# JOGAR NOVAMENTE
while True:
    j_n = input('\nDeseja jogar novamente? 1 - sim 2 - não ')
    if j_n == '1' or j_n == 'sim' or j_n == 's' or j_n == 'SIM' or j_n == 'S' or j_n == 'SI' or j_n == 'si':
        jogo()
    elif j_n == '2' or j_n == 'n' or j_n == 'Não' or j_n == 'N' or j_n == 'NÃO' or j_n == 'NAO' or j_n == 'nao' or j_n == 'no' or j_n == 'NO':
        break
    else:
        print('\nInforme umas das opções.')



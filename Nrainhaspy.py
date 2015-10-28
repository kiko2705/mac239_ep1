__author__ = 'kiko & vitor'

# INSERE DADOS INICIAIS
N = int(input('Entre com o tamanho do tabuleiro : '))
K = int(input('Entre com o número de rainhas já colocadas : '))

tamanho_lista_clausulas = N*N

# define a matriz bidimensional que representa o tabuleiro
matriz_tabuleiro = [[0 for x in range(N)] for x in range(N)]

#----------------------------------------------------------------------------------------------------------------------
#funcao presenca rainha
def gera_clausula_presenca_rainha(N):

    # cláusulas para a presença de uma rainha em cada linha
    # r11 ∨ r12
    # r21 ∨ r22
    # etc...

    # índice linha matriz tabuleiro
    linha = N
    # índice coluna matriz tabuleiro
    coluna = N

    # define a matriz de rainhas bidimensional, que representa cada rainha
    r = [[0 for x in range(N)] for x in range(N)]

    # define lista que conterá cláusulas presenca rainhas
    lista_clausulas = []

    # loop para preencher cláusulas presença rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            r[linha][coluna] = True
            print('r', linha+1, coluna+1, '=', r[linha][coluna])
            # coloca o valor boleano em cada coluna na lista cláusulas
            lista_clausulas.append(r[linha][coluna])
    # coloca o valor boleano em cada linha na lista cláusulas
    r[linha][coluna] = True
    print('r', linha+1, coluna+1, '=', r[linha][coluna])
    lista_clausulas.append(r[linha][coluna])

    #return lista_clausulas
#----------------------------------------------------------------------------------------------------------------------
# função restrição linhas
def gera_clausula_restricao_linhas(N):

    # cláusulas de restrição de não ataque nas linhas:
    # ¬r 11 ∨ ¬r 12
    # ¬r 21 ∨ ¬r 22
    # etc...

    # índice linha matriz tabuleiro
    linha = N
    # índice coluna matriz tabuleiro
    coluna = N

    # define a matriz de rainhas bidimensional, que representa cada rainha
    r = [[0 for x in range(N)] for x in range(N)]

    # define lista que conterá cláusulas restrição linhas
    lista_clausulas = []

    # loop para preencher cláusulas restrição linhas
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            r[linha][coluna] = False
            print('r', linha+1, coluna+1, '=', r[linha][coluna])
            # coloca o valor boleano em cada coluna na lista cláusulas
            lista_clausulas.append(r[linha][coluna])
    # coloca o valor boleano em cada linha na lista cláusulas
    r[linha][coluna] = False
    print('r', linha+1, coluna+1, '=', r[linha][coluna])
    lista_clausulas.append(r[linha][coluna])

    #return lista_clausulas
#----------------------------------------------------------------------------------------------------------------------
# função restrição colunas
def gera_clausula_restricao_colunas(N):

    # cláusulas de restrição de não ataque nas colunas:
    #¬r 11 ∨ ¬r 21
    #¬r 12 ∨ ¬r 22
    # etc...

    # índice linha matriz tabuleiro
    linha = N
    # índice coluna matriz tabuleiro
    coluna = N

    # define a matriz de rainhas bidimensional, que representa cada rainha
    r = [[0 for x in range(N)] for x in range(N)]

    # define lista que conterá cláusulas restrição linhas
    lista_clausulas = []

    # loop para preencher cláusulas restrição linhas
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            r[linha][coluna] = False
            print('r', linha+1, coluna+1, '=', r[linha][coluna])
            # coloca o valor boleano em cada coluna na lista cláusulas
            lista_clausulas.append(r[linha][coluna])
    # coloca o valor boleano em cada linha na lista cláusulas
    r[linha][coluna] = False
    print('r', linha+1, coluna+1, '=', r[linha][coluna])
    lista_clausulas.append(r[linha][coluna])

    #return lista_clausulas
#----------------------------------------------------------------------------------------------------------------------









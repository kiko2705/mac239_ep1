__author__ = 'kiko & vitor'

# INSERE DADOS INICIAIS
N = int(input('Entre com o tamanho do tabuleiro : '))
K = int(input('Entre com o número de rainhas já colocadas : '))

# índice linha matriz tabuleiro
linha = N
# índice coluna matriz tabuleiro
coluna = N

tamanho_lista_clausulas = N*N

# define a matriz bidimensional que representa o tabuleiro
matriz_tabuleiro = [[0 for x in range(N)] for x in range(N)]
# define a matriz de rainhas bidimensional, que representa cada rainha
r = [[0 for x in range(N)] for x in range(N)]

# gera clausula presença
#lista_clausulas_presenca = []
#lista_clausulas_presenca = gera_clausula_presenca_rainha(N)
#for indice_lista_clausula in range(tamanho_lista_clausulas):
    #for linha in range(N):
        #print('r', linha+1, coluna+1, '=', lista_clausulas[indice_lista_clausula])
        #for coluna in range(N):
            #print('r', linha+1, coluna+1, '=', lista_clausulas[indice_lista_clausula])


#----------------------------------------------------------------------------------------------------------------------
#funcao presenca rainha
def gera_clausula_presenca_rainha(N):

    # cláusulas para a presença de uma rainha em cada linha
    # r11 ∨ r12 (c1)
    # r21 ∨ r22 (c2)
    # etc...

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










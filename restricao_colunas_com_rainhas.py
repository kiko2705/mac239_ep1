__author__ = 'kiko'

from pyeda.inter import *

def cnf_restricao_colunas_com_rainhas(N, K, c, pos_rainha_y):

     # cláusulas de restrição de não ataque nas colunas:
        #¬r 11 ∨ ¬r 21
        #¬r 12 ∨ ¬r 22
        # etc...

    # índice linha matriz tabuleiro
    linha = N
    # índice coluna matriz tabuleiro
    coluna = N

    # define matriz r
    r = exprvars('r', N, N)

    # cria disjunções
    disjuncao = 0

    # cria cnf conjunção de disjunções
    cnf_restricao_linhas_rainha = 0

    # define a lista de duplas de disjunções
    c_temp = [0 for x in range(N*N*N)]

    contador_c = 0

    contador_dupla = 0

    cont_global = 0

    # contador do número cláusulas
    cont_clausulas = 0

    for coluna in range(N):
        for cont in range(K):
            # repete o numero de rainhas estes dois loops
            if coluna == pos_rainha_y[cont]:
                c[cont_global] = True
                cont_global += 1
                coluna += 1
        if (coluna < N):
            if (c[cont_global] != True):
                for linha in range(N-1):
                    for aux in range(linha+1, N):
                        disjuncao_temp = ~r[linha][coluna] | ~r[aux][coluna]
                        c_temp[contador_dupla] = disjuncao_temp
                        c[cont_global] = c_temp[contador_dupla]
                        contador_dupla += 1
                        cont_global += 1

    return c
#--------------------------------------------------------------------------------------------------------------------



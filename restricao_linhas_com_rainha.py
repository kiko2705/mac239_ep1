__author__ = 'kiko'

from pyeda.inter import *

def cnf_restricao_linhas_com_rainhas(N, K, c, pos_rainha_x):

    # cláusulas para a restrição de linhas
        # ~r11 ∨ ~r12
        # ~r21 ∨ ~r22
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

    contador_dupla = 0

    cont = 0

    cont_clausulas = 0

    cont_global = 0

    print ("Restrição linha")
    # loop para preencher cláusulas restrição linhas rainha
    for linha in range(N):
        for cont in range(K):
            # repete o numero de rainhas estes dois loops
            if linha == pos_rainha_x[cont]:
                c[cont_global] = True
                cont_global += 1
                linha += 1
        if (linha < N):
            if (c[cont_global] != True):
                for coluna in range(N-1):
                    for aux in range(coluna+1, N):
                        disjuncao_temp = ~r[linha][coluna] | ~r[linha][aux]
                        c_temp[contador_dupla] = disjuncao_temp
                        c[cont_global] = c_temp[contador_dupla]
                        contador_dupla += 1
                        cont_global += 1

    return c
#--------------------------------------------------------------------------------------------------------------------


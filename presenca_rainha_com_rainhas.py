__author__ = 'kiko'

from pyeda.inter import *

def cnf_presenca_com_rainhas(N, K, c, pos_rainha_x):

    cont_global = 0

    linha = N
    coluna = N

    r = exprvars('r', N, N)
    disjuncao = 0

    # cria cnf conjunção de disjunções
    #cnf_presenca_rainha = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]

    cnf_presenca_rainha = [0 for x in range(N*N*N)]

    cont_aux = 0

    # loop para preencher cláusulas presença rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for cont_aux in range(0, K):
            if (linha == pos_rainha_x[cont_aux]):
                c[cont_global] = True
                break
        if (c[cont_global] != True):
            for coluna in range(N):
                if (coluna == 0):
                    disjuncao = r[linha][coluna]
                else:
                    disjuncao = disjuncao | r[linha][coluna]
                c[cont_global] = disjuncao
        cont_global += 1

    # gera lista conjunção de disjunções
    for contador_duplas in range(N):
        cnf_presenca_rainha[contador_duplas] = c[contador_duplas]

    return cnf_presenca_rainha

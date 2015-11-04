__author__ = 'kiko'

from pyeda.inter import *


def restricao_diagonais(N, c):

    # cláusulas de restrição a não ataques nas diagonais
    # ¬r 11 ∨ ¬r 22
    # ¬r 12 ∨ ¬r 21
    # etc...

    linha  = 0
    coluna = 0
    disjuncao = 0
    # define a lista de cláusulas de disjunções temporaria
    c_temp = [0 for x in range(N*N*N)]
    # define a lista de cláusulas de disjunções
    #c = [0 for x in range(N*N*N)]
    # contador do número cláusulas
    r = exprvars('r', N, N)
     # define a lista de cnfs de diagonais
    cnf_diagonais_temp = [0 for x in range(N*N)]
    cnf_diagonais = 0
    aux_c = 0
    aux_l = 0
    contador_c = 0
    contador_dupla = 0

    # diagonais principais

    # diagonal principal e principal superiores
    for cont_d in range(0, N-1):
        for coluna, linha in zip(range(cont_d, N-1), range(N-1)):
            for aux_c, aux_l in zip(range(coluna+1,N), range(linha+1,N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                c[contador_c] = c_temp[contador_dupla]
                contador_c += 1
                contador_dupla += 1

    # diagonal principal inferiores
    for cont_d in range(1, N-1):
        for coluna, linha in zip(range(N-1), range(cont_d, N-1)):
            for aux_c, aux_l in zip(range(coluna+1,N), range(linha+1,N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                c[contador_c] = c_temp[contador_dupla]
                contador_c += 1
                contador_dupla += 1

    # diagonais superiores secundárias
    for cont_d in reversed(range(1, N)):
        for coluna, linha in zip(reversed(range(1, cont_d+1)), range(N-1)):
            for aux_c, aux_l in zip(reversed(range(0, coluna)), range(linha+1, N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                c[contador_c] = c_temp[contador_dupla]
                contador_c += 1
                contador_dupla += 1

    # diagonais inferiores secundárias
    for cont_d in range(1, N-1):
        for coluna, linha in zip(reversed(range(1, N)), range(cont_d, N-1)):
            for aux_c, aux_l in zip(reversed(range(0, coluna)), range(linha+1, N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                c[contador_c] = c_temp[contador_dupla]
                contador_c += 1
                contador_dupla += 1

    return c
#--------------------------------------------------------------------------------------------------------------------


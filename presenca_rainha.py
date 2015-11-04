__author__ = 'kiko'

from pyeda.inter import *

def presenca_rainha(N, cnf_presenca_rainha):
    # cláusulas para a presença de uma rainha em cada linha
        # r11 ∨ r12
        # r21 ∨ r22
        # etc...

    linha = N
    coluna = N

    r = exprvars('r', N, N)
    disjuncao = 0

    # cria cnf conjunção de disjunções
    #cnf_presenca_rainha = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]

    # contador do número cláusulas
    cont_clausulas = 0

    # loop para preencher cláusulas presença rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            if (coluna == 0):
                disjuncao = r[linha][coluna]
            else:
                disjuncao = disjuncao | r[linha][coluna]
        # fim disjunções da cláusula n
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1

    # gera lista conjunção de disjunções
    for contador_cnf_presenca_rainha in range(N):
            cnf_presenca_rainha[contador_cnf_presenca_rainha] = c[contador_cnf_presenca_rainha]

    return cnf_presenca_rainha
#--------------------------------------------------------------------------------------------------------------------



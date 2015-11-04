__author__ = 'kiko'

from pyeda.inter import *

def restricao_linhas(N, c):
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

    contador_c = 0

    contador_dupla = 0

    cont_clausulas = 0

    # loop para preencher cláusulas restrição linhas rainha
    for linha in range(N):
        for coluna in range(N-1):
            for aux in range(coluna+1, N):
                disjuncao_temp = ~r[linha][coluna] | ~r[linha][aux]
                c_temp[contador_dupla] = disjuncao_temp
                if contador_dupla == 0:
                    c[contador_c] = c_temp[contador_dupla]
                    print(c[contador_c])
                else:
                    contador_c += 1
                    c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                    print(c[contador_c])
                contador_dupla += 1

    #return
#--------------------------------------------------------------------------------------------------------------------


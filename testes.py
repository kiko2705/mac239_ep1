__author__ = 'kiko'

from pyeda.inter import *

def for_estilo_java(valor_inicial,condicao,incremento):
    while condicao(valor_inicial):
        yield valor_inicial
        valor_inicial = incremento(valor_inicial)
#------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    N = 4
    linha  = 0
    coluna = 0
    disjuncao = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N)]

    # contador do número cláusulas
    cont_clausulas = 0

    flag_clausulas = 0

    r = exprvars('r', N, N)

    # diagonais principais

    for linha in for_estilo_java(0, lambda linha:linha < N, lambda linha:linha+1):
        for coluna in for_estilo_java(0, lambda coluna:coluna<N-linha, lambda coluna:coluna+1):
            if flag_clausulas == 0:
                disjuncao = ~r[coluna][coluna+linha]
                flag_clausulas = 1
            else:
                negacao = ~r[coluna][coluna+linha]
                disjuncao = disjuncao | negacao
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1
        flag_clausulas = 0
        if linha != 0:
            for coluna in for_estilo_java(0, lambda coluna:coluna<N-linha, lambda coluna:coluna+1):
                #print("([", (coluna + linha), ",", coluna, "])")
                #print("p2")
                if flag_clausulas == 0:
                    disjuncao = ~r[coluna+linha][coluna]
                    flag_clausulas = 1
                else:
                    negacao = ~r[coluna+linha][coluna]
                    disjuncao = disjuncao | negacao
            c[cont_clausulas] = disjuncao
            cont_clausulas += 1
            flag_clausulas = 0


    cont_clausulas = 0
    flag_clausulas = 0

    #contador diagonais superiores secundarias
    cont_ds = 0

    # diagonais superiores secundárias
    for cont_ds in range(0, N-1):
        for coluna, linha in zip(reversed(range(N-cont_ds)), range(0, linha+1)):
            if flag_clausulas == 0:
                disjuncao = ~r[linha][coluna]
                flag_clausulas = 1
            else:
                negacao = ~r[linha][coluna]
                disjuncao = disjuncao | negacao
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1

    # diagonais inferiores secundárias

    #contador diagonais inferiores secundarias
    cont_di = N-1
    flag_clausulas = 0
    N_col = N
    N_lin = N
    inicio = 0

    for cont_di in range(0, N-1):
        print(cont_di)
        for coluna, linha in zip(reversed(range(N_col)), range(inicio, N_lin)):
            if flag_clausulas == 0:
                disjuncao = ~r[linha][coluna]
                flag_clausulas = 1
                print(~r[linha][coluna])
            else:
                negacao = ~r[linha][coluna]
                disjuncao = disjuncao | negacao
                print(~r[linha][coluna])

        inicio = inicio + 1
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1


    # gera lista conjunção de disjunções
    # varre lista
    for contador_cnf_restricao_diagonais_rainha in range(N):
        if contador_cnf_restricao_diagonais_rainha == 0:
            cnf_restricao_diagonais_rainha = c[contador_cnf_restricao_diagonais_rainha]
        else:
            cnf_restricao_diagonais_rainha = cnf_restricao_diagonais_rainha & c[contador_cnf_restricao_diagonais_rainha]
    # no final deste laço cnf_restricao_diagonais_rainha conterá a cnf de restricao diagonais

    #print(cnf_restricao_diagonais_rainha)
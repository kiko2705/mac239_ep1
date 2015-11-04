__author__ = 'kiko'

from pyeda.inter import *

def for_estilo_java(valor_inicial,condicao,incremento):
    while condicao(valor_inicial):
        yield valor_inicial
        valor_inicial = incremento(valor_inicial)
#------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    N = 3
    linha  = 0
    coluna = 0
    disjuncao = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N)]

    # define a lista de cláusulas de disjunções temporaria
    c_temp = [0 for x in range(N*N)]

    # contador do número cláusulas
    cont_clausulas = 0

    flag_clausulas = 0

    r = exprvars('r', N, N)
#-------------------------------------------------------------------------------------
    # diagonais principais

    cont_clausulas = 0
    flag_clausulas = 0

    for linha in for_estilo_java(0, lambda linha:linha < N, lambda linha:linha+1):
        for coluna in for_estilo_java(0, lambda coluna:coluna<N-linha, lambda coluna:coluna+1):
            if flag_clausulas == 0:
                disjuncao = ~r[coluna][coluna+linha]
                flag_clausulas = 1
            else:
                negacao = ~r[coluna][coluna+linha]
                disjuncao = disjuncao | negacao
        # se não é a primeira disjunção
        if(cont_clausulas == 0):
            c_temp[cont_clausulas] = disjuncao
        else:
            c_temp[cont_clausulas] = c_temp[cont_clausulas-1] & disjuncao
        flag_clausulas = 0
        cont_clausulas = cont_clausulas + 1
        if linha != 0:
            for coluna in for_estilo_java(0, lambda coluna:coluna<N-linha, lambda coluna:coluna+1):
                if flag_clausulas == 0:
                    disjuncao = ~r[coluna+linha][coluna]
                    flag_clausulas = 1
                else:
                    negacao = ~r[coluna+linha][coluna]
                    disjuncao = disjuncao | negacao
            if(cont_clausulas == 0):
                c_temp[cont_clausulas] = disjuncao
            else:
                c_temp[cont_clausulas] = c_temp[cont_clausulas-1] & disjuncao
            flag_clausulas = 0
            cont_clausulas = cont_clausulas + 1

    # elimina 2 últimos elementos (2 casas vazias)
    for cont in range(cont_clausulas-2):
        c[cont] = c_temp[cont]

    cnf_diagonais_principais = c[cont]
    print("diagonais principais")
    print(cnf_diagonais_principais)
#--------------------------------------------------------------------------------------------------
    # diagonais superiores secundárias

    cont_clausulas = 0
    flag_clausulas = 0

    #contador diagonais superiores secundarias
    cont_ds = 0

    for cont_ds in range(0, N-1):
        for coluna, linha in zip(reversed(range(N-cont_ds)), range(0, linha+1)):
            if flag_clausulas == 0:
                disjuncao = ~r[linha][coluna]
                flag_clausulas = 1
            else:
                negacao = ~r[linha][coluna]
                disjuncao = disjuncao | negacao
        if(cont_clausulas == 0):
            c[cont_clausulas] = disjuncao
        else:
            c[cont_clausulas] = c[cont_clausulas-1] & disjuncao
        flag_clausulas = 0
        cont_clausulas = cont_clausulas + 1

    #print(c[cont_clausulas-1])
#-----------------------------------------------------------------------------------------
    # diagonais inferiores secundárias

    #contador diagonais inferiores secundarias
    cont_clausulas = 0
    flag_clausulas = 0
    N_col = N
    N_lin = N
    inicio = 0

    for cont_di in range(0, N-1):
        for coluna, linha in zip(reversed(range(N_col)), range(inicio, N_lin)):
            if flag_clausulas == 0:
                disjuncao = ~r[linha][coluna]
                flag_clausulas = 1
            else:
                negacao = ~r[linha][coluna]
                disjuncao = disjuncao | negacao
        inicio = inicio + 1
        if(cont_clausulas == 0):
            c[cont_clausulas] = disjuncao
        else:
            c[cont_clausulas] = c[cont_clausulas-1] & disjuncao
        flag_clausulas = 0
        cont_clausulas = cont_clausulas + 1

    #print(c[cont_clausulas-1])
#---------------------------------------------------------------------------------------


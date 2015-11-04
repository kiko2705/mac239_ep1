__author__ = 'Francisco Santos Nusp 794650,  Vitor Kemada Nusp'

from pyeda.inter import *
from subprocess import call
import os
#-------------------------------------------------------------------------------------------------------------------
def for_estilo_java(valor_inicial,condicao,incremento):
    while condicao(valor_inicial):
        yield valor_inicial
        valor_inicial = incremento(valor_inicial)
#-------------------------------------------------------------------------------------------------------------------
def Export2Image(bdd, fmt, file_name):
    # Exporta o diagrama para o Graphviz (linguagem Dot)
    with open("temp.gv", "w") as hFile:
        hFile.write(bdd.to_dot())
    # Gera o PDF com o diagrama
    call(["dot", "-T" + fmt, "temp.gv", "-o" + file_name])
    os.remove("temp.gv")
#--------------------------------------------------------------------------------------------------------------------
def presenca_rainha(N):
    # cláusulas para a presença de uma rainha em cada linha
        # r11 ∨ r12
        # r21 ∨ r22
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
    cnf_presenca_rainha = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N)]

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
    # no final deste laço c[] conterá o conjunto de cláusulas de disjunções

    # agora juntaremos cada c[] com um & para construir a CNF

    # gera lista conjunção de disjunções
    # varre lista
    for contador_cnf_presenca_rainha in range(N):
        if contador_cnf_presenca_rainha == 0:
            cnf_presenca_rainha = c[contador_cnf_presenca_rainha]
        else:
            cnf_presenca_rainha = cnf_presenca_rainha & c[contador_cnf_presenca_rainha]
    # no final deste laço cnf_presenca_rainha conterá a cnf de presença

    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_presenca_rainha)

    #Export2Image(bdd, "pdf", "bdd_presenca.pdf")

    return cnf_presenca_rainha
#--------------------------------------------------------------------------------------------------------------------
def restricao_linhas(N):
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

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N)]

    # contador do número cláusulas
    cont_clausulas = 0

    # loop para preencher cláusulas restrição linhas rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            if (coluna == 0):
                disjuncao = ~r[linha][coluna]
            else:
                negacao = ~r[linha][coluna]
                disjuncao = disjuncao | negacao
        # fim disjunções da cláusula n
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1
    # no final deste laço c[] conterá o conjunto de cláusulas de disjunções

    # agora juntaremos cada c[] com um & para construir a CNF

    # gera lista conjunção de disjunções
    # varre lista
    for contador_cnf_restricao_linhas_rainha in range(N):
        if contador_cnf_restricao_linhas_rainha == 0:
            cnf_restricao_linhas_rainha = c[contador_cnf_restricao_linhas_rainha]
        else:
            cnf_restricao_linhas_rainha = cnf_restricao_linhas_rainha & c[contador_cnf_restricao_linhas_rainha]
    # no final deste laço cnf_restricao_linhas_rainha conterá a cnf de restrição linhas

    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_restricao_linhas_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_linhas.pdf")

    return cnf_restricao_linhas_rainha
#--------------------------------------------------------------------------------------------------------------------
def restricao_colunas(N):

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
    cnf_restricao_colunas_rainha = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N)]

    # contador do número cláusulas
    cont_clausulas = 0

    # loop para preencher cláusulas restrição colunas rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            if (coluna == 0):
                disjuncao = ~r[coluna][linha]
            else:
                negacao = ~r[coluna][linha]
                disjuncao = disjuncao | negacao
        # fim disjunções da cláusula n
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1
    # no final deste laço c[] conterá o conjunto de cláusulas de disjunções

    # agora juntaremos cada c[] com um & para construir a CNF

    # gera lista conjunção de disjunções
    # varre lista
    for contador_cnf_restricao_colunas_rainha in range(N):
        if contador_cnf_restricao_colunas_rainha == 0:
            cnf_restricao_colunas_rainha = c[contador_cnf_restricao_colunas_rainha]
        else:
            cnf_restricao_colunas_rainha = cnf_restricao_colunas_rainha & c[contador_cnf_restricao_colunas_rainha]
    # no final deste laço cnf_restricao_colunas_rainha conterá a cnf de restrição colunas

    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_restricao_colunas_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")

    return cnf_restricao_colunas_rainha
#--------------------------------------------------------------------------------------------------------------------
def restricao_diagonais(N):

    # cláusulas de restrição a não ataques nas diagonais
    # ¬r 11 ∨ ¬r 22
    # ¬r 12 ∨ ¬r 21
    # etc...

    linha  = 0
    coluna = 0
    disjuncao = 0
    # define a lista de cláusulas de disjunções temporaria
    c_temp = [0 for x in range(N*N)]
    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N)]
    # contador do número cláusulas
    r = exprvars('r', N, N)
     # define a lista de cnfs de diagonais
    cnf_diagonais_temp = [0 for x in range(N*N)]
    cont_clausulas = 0
    flag_clausulas = 0
    cnf_diagonais = 0

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
    cnf_diagonais_temp[0] = cnf_diagonais_principais

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
            #print(c[cont_clausulas])
        else:
            c[cont_clausulas] = c[cont_clausulas-1] & disjuncao
            #print(c[cont_clausulas])
        flag_clausulas = 0
        cont_clausulas = cont_clausulas + 1

    cnf_diagonais_secundarias_superiores = c[cont_clausulas-1]
    cnf_diagonais_temp[1] = cnf_diagonais_secundarias_superiores

    # diagonais inferiores secundárias

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

    cnf_diagonais_secundarias_inferiores = c[cont_clausulas-1]

    cnf_diagonais_temp[2] = cnf_diagonais_secundarias_inferiores

    cnf_restricao_diagonais_rainha = cnf_diagonais_temp[0] & cnf_diagonais_temp[1] & cnf_diagonais_temp[2]

    # no final deste laço cnf_restricao_diagonais_rainha conterá a cnf de restricao diagonais
    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_diagonais)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")

    return cnf_restricao_diagonais_rainha
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # INSERE DADO INICIAL
    N = int(input('Entre com o tamanho do tabuleiro : '))

    # une as restrições
    cnf_presenca_rainha = presenca_rainha(N)

    cnf_restricao_linhas = restricao_linhas(N)

    cnf_restricao_colunas = restricao_colunas(N)

    cnf_restricao_diagonais = restricao_diagonais(N)

    cnf_n_rainhas = cnf_presenca_rainha & cnf_restricao_linhas & cnf_restricao_colunas & cnf_restricao_diagonais

    bdd_cnf_n_rainhas = expr2bdd(cnf_n_rainhas)

    # Testa satisfatibilidade
    print(bdd_cnf_n_rainhas.satisfy_count())
    print(bdd_cnf_n_rainhas.is_zero())

















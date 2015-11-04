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
    c = [0 for x in range(N*N)]

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
    for contador_cnf_presenca_rainha in range(N):
        if contador_cnf_presenca_rainha == 0:
            cnf_presenca_rainha = c[contador_cnf_presenca_rainha]
        else:
            cnf_presenca_rainha = cnf_presenca_rainha & c[contador_cnf_presenca_rainha]
    # no final deste laço cnf_presenca_rainha conterá a cnf de presença

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

    #contador_dupla -= 1
    #return
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
    cnf_restricao_linhas_rainha = 0

    # define a lista de duplas de disjunções
    c_temp = [0 for x in range(N*N*N)]

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]

    contador_c = 0

    contador_dupla = 0

    # contador do número cláusulas
    cont_clausulas = 0

    for coluna in range(N):
        for linha in range(N-1):
            for aux in range(linha+1, N):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux][coluna]
                c_temp[contador_dupla] = disjuncao_temp
                if contador_dupla == 0:
                    c[contador_c] = c_temp[contador_dupla]
                    print(c[contador_c])
                else:
                    contador_c += 1
                    c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                    print(c[contador_c])
                contador_dupla += 1

    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_restricao_colunas_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")

    #return cnf_restricao_colunas_rainha
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
    c_temp = [0 for x in range(N*N*N)]
    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]
    # contador do número cláusulas
    r = exprvars('r', N, N)
     # define a lista de cnfs de diagonais
    cnf_diagonais_temp = [0 for x in range(N*N)]
    cont_clausulas = 0
    flag_clausulas = 0
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
                if contador_dupla == 0:
                    c[contador_c] = c_temp[contador_dupla]
                else:
                    contador_c += 1
                    c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                contador_dupla += 1

    # diagonal principal inferiores
    for cont_d in range(1, N-1):
        for coluna, linha in zip(range(N-1), range(cont_d, N-1)):
            for aux_c, aux_l in zip(range(coluna+1,N), range(linha+1,N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                contador_c += 1
                c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                contador_dupla += 1

    # diagonais superiores secundárias
    for cont_d in reversed(range(1, N)):
        for coluna, linha in zip(reversed(range(1, cont_d+1)), range(N-1)):
            for aux_c, aux_l in zip(reversed(range(0, coluna)), range(linha+1, N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                contador_c += 1
                c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                contador_dupla += 1

    cont_clausulas = 0
    flag_clausulas = 0

    # diagonais inferiores secundárias
    for cont_d in range(1, N-1):
        for coluna, linha in zip(reversed(range(1, N)), range(cont_d, N-1)):
            for aux_c, aux_l in zip(reversed(range(0, coluna)), range(linha+1, N)):
                disjuncao_temp = ~r[linha][coluna] | ~r[aux_l][aux_c]
                c_temp[contador_dupla] = disjuncao_temp
                contador_c += 1
                c[contador_c] = c[contador_c-1] & c_temp[contador_dupla]
                contador_dupla += 1

    #cnf_diagonais_secundarias_inferiores = c[cont_clausulas-1]

    #cnf_diagonais_temp[2] = cnf_diagonais_secundarias_inferiores

    #cnf_restricao_diagonais_rainha = cnf_diagonais_temp[0] & cnf_diagonais_temp[1] & cnf_diagonais_temp[2]

    # no final deste laço cnf_restricao_diagonais_rainha conterá a cnf de restricao diagonais
    # converte em bdd a cnf
    #bdd = expr2bdd(cnf_diagonais)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")

    #return cnf_restricao_diagonais_rainha
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # INSERE DADO INICIAL
    N = int(input('Entre com o tamanho do tabuleiro : '))

    indice_cnf = 0

    # une as restrições

    #bdd_presenca_rainha = expr2bdd(cnf_presenca_rainha)
    cnf_presenca = presenca_rainha(N)
    print(cnf_presenca)

    #bdd_restricao_linhas = expr2bdd(cnf_restricao_linhas)
    #cnf_restricao_linhas = restricao_linhas(N)

    #cnf_restricao_colunas = restricao_colunas(N)
    #bdd_restricao_colunas = expr2bdd(cnf_restricao_colunas)
    #restricao_colunas(N)

    #cnf_restricao_diagonais = restricao_diagonais(N)
    #bdd_restricao_digonais = expr2bdd(cnf_restricao_diagonais)
    #restricao_diagonais(N)

    #cnf_n_rainhas = cnf_presenca_rainha & cnf_restricao_linhas & cnf_restricao_colunas & cnf_restricao_diagonais

    #bdd_cnf_n_rainhas = expr2bdd(cnf_n_rainhas)

    # Testa satisfatibilidade
    #print(bdd_cnf_n_rainhas.satisfy_count())
    #print(bdd_cnf_n_rainhas.is_zero())

















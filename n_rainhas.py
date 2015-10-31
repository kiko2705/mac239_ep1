__author__ = 'kiko'

from pyeda.inter import *
from subprocess import call
import os

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
    bdd = expr2bdd(cnf_presenca_rainha)

    #Export2Image(bdd, "pdf", "bdd_presenca.pdf")

    return(bdd)
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
    bdd = expr2bdd(cnf_restricao_linhas_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_linhas.pdf")

    return(bdd)
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
    bdd = expr2bdd(cnf_restricao_colunas_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")

    return(bdd)
#--------------------------------------------------------------------------------------------------------------------
def restricao_diagonais(N):

    # cláusulas de restrição a não ataques nas diagonais
    # ¬r 11 ∨ ¬r 22
    # ¬r 12 ∨ ¬r 21
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
    cnf_restricao_diagonais_rainha = 0

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N)]

    # contador do número cláusulas
    cont_clausulas = 0

    # loop para preencher cláusulas restrição diagonais rainha
    # número de cláusulas a serem criadas será NxN
    for linha in range(N):
        for coluna in range(N):
            if( (coluna == linha) and coluna == 0 ):
                disjuncao = r[linha][coluna]
            else:
                if (coluna == linha):
                    disjuncao = disjuncao | r[linha][coluna]
        # fim disjunções da cláusula n
        c[cont_clausulas] = disjuncao
        cont_clausulas += 1
    # no final deste laço c[] conterá o conjunto de cláusulas de disjunções

    # agora juntaremos cada c[] com um & para construir a CNF

    # gera lista conjunção de disjunções
    # varre lista
    for contador_cnf_restricao_diagonais_rainha in range(N):
        if contador_cnf_restricao_diagonais_rainha == 0:
            cnf_restricao_diagonais_rainha = c[contador_cnf_restricao_diagonais_rainha]
        else:
            cnf_restricao_diagonais_rainha = cnf_restricao_diagonais_rainha & c[contador_cnf_restricao_diagonais_rainha]
    # no final deste laço cnf_restricao_diagonais_rainha conterá a cnf de restrição das diagonais

    # converte em bdd a cnf
    bdd = expr2bdd(cnf_restricao_diagonais_rainha)

    #Export2Image(bdd, "pdf", "bdd_restricao_colunas.pdf")


    return (bdd)
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # INSERE DADO INICIAL
    N = int(input('Entre com o tamanho do tabuleiro : '))

    # une as restrições
    cnf_presenca_rainha = presenca_rainha(N)

    cnf_restricao_linhas = restricao_linhas(N)

    cnf_restricao_colunas = restricao_colunas(N)

    cnf_n_rainhas = cnf_presenca_rainha & cnf_restricao_linhas & cnf_restricao_colunas

    bdd_expr_cnf_n_rainhas = expr2bdd(cnf_n_rainhas)
    print(bdd_expr_cnf_n_rainhas.satisfy_one())
    print(bdd_expr_cnf_n_rainhas.satisfy_count())














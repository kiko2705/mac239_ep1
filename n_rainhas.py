__author__ = 'Francisco Santos Nusp 794650,  Vitor Kemada Nusp'

from pyeda.inter import *
from subprocess import call
import os
import presenca_rainha
import restricao_linhas
import restricao_diagonais
import restricao_colunas

#-------------------------------------------------------------------------------------------------------------------
def Export2Image(bdd, fmt, file_name):
    # Exporta o diagrama para o Graphviz (linguagem Dot)
    with open("temp.gv", "w") as hFile:
        hFile.write(bdd.to_dot())
    # Gera o PDF com o diagrama
    call(["dot", "-T" + fmt, "temp.gv", "-o" + file_name])
    os.remove("temp.gv")
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # INSERE DADOS INICIAIS ( N = TAMANHO TABULEIRO , K = NÚMERO DE RAINHAS )
    N = int(input('Entre com o tamanho do tabuleiro : '))
    #K = int(input('Entre com o número de rainhas : '))

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]

    cnf_temp = [0 for x in range(N*N*N)]

    cnf = [0 for x in range(N*N*N)]

    temp = 0

    contador_global_clausulas = 0

    # une as restrições

    print("presenças rainha")
    cnf_temp = presenca_rainha.presenca_rainha(N, c)
    #bdd_presenca_rainha = expr2bdd(cnf_presenca_rainha)
    for cont_presenca in range(N):
        cnf[contador_global_clausulas] = cnf_temp[cont_presenca]
        print(cnf[contador_global_clausulas])
        contador_global_clausulas += 1

    print("restrição linhas")
    cnf_temp = restricao_linhas.restricao_linhas(N, c)
    #bdd_restricao_linhas = expr2bdd(cnf_restricao_linhas)
    for cont_restricao_linhas in range(N*N):
        cnf[contador_global_clausulas] = cnf_temp[cont_restricao_linhas]
        print(cnf[contador_global_clausulas])
        contador_global_clausulas += 1

    print("restrição colunas")
    cnf_temp = restricao_colunas.restricao_colunas(N, c)
    #bdd_restricao_colunas = expr2bdd(cnf_restricao_colunas)
    for cont_restricao_colunas in range(N*N):
        cnf[contador_global_clausulas] = cnf_temp[cont_restricao_colunas]
        print(cnf[contador_global_clausulas])
        contador_global_clausulas += 1

    print("restrição diagonais")
    cnf = restricao_diagonais.restricao_diagonais(N, c)
    #bdd_restricao_digonais = expr2bdd(cnf_restricao_diagonais)


    # Testa satisfatibilidade
    #print(bdd_cnf_n_rainhas.satisfy_count())
    #print(bdd_cnf_n_rainhas.is_zero())

    #Export2Image(bdd, "pdf", "bdd_presenca.pdf")


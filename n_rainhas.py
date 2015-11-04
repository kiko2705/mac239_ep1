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

    cnf = [0 for x in range(N*N*N)]

    contador_duplas = 0

    # une as restrições

    print("presenças rainha")
    cnf = presenca_rainha.presenca_rainha(N, c)
    #bdd_presenca_rainha = expr2bdd(cnf_presenca_rainha)
    print(cnf[0])
    print(cnf[1])
    print(cnf[2])

    print("restrição linhas")
    cnf = restricao_linhas.restricao_linhas(N, c)
    #bdd_restricao_linhas = expr2bdd(cnf_restricao_linhas)
    print(cnf[0])
    print(cnf[1])
    print(cnf[2])
    print(cnf[3])
    print(cnf[4])
    print(cnf[5])
    print(cnf[6])
    print(cnf[7])
    print(cnf[8])

    print("restrição colunas")
    cnf = restricao_colunas.restricao_colunas(N, c)
    #bdd_restricao_colunas = expr2bdd(cnf_restricao_colunas)
    print(cnf[0])
    print(cnf[1])
    print(cnf[2])
    print(cnf[3])
    print(cnf[4])
    print(cnf[5])
    print(cnf[6])
    print(cnf[7])
    print(cnf[8])

    print("restrição diagonais")
    cnf = restricao_diagonais.restricao_diagonais(N, c)
    #bdd_restricao_digonais = expr2bdd(cnf_restricao_diagonais)
    print(cnf[0])
    print(cnf[1])
    print(cnf[2])
    print(cnf[3])
    print(cnf[4])
    print(cnf[5])
    print(cnf[6])
    print(cnf[7])
    print(cnf[8])
    print(cnf[9])

    # Testa satisfatibilidade
    #print(bdd_cnf_n_rainhas.satisfy_count())
    #print(bdd_cnf_n_rainhas.is_zero())

    #Export2Image(bdd, "pdf", "bdd_presenca.pdf")


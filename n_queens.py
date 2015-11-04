__author__ = 'Francisco Santos Nusp 794650,  Vitor Kemada Nusp'

from pyeda.inter import *
from subprocess import call
import os
import presenca_rainha_teste
import restricao_linhas_teste
import restricao_diagonais_teste
import restricao_colunas_teste
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

    # une as restrições

    print("presenças rainha")
    cnf = presenca_rainha_teste.presenca_rainha_teste(N, c)
    #bdd_presenca_rainha = expr2bdd(cnf_presenca_rainha)

    print("restrição linhas")
    cnf = restricao_linhas_teste.restricao_linhas_teste(N, c)
    #bdd_restricao_linhas = expr2bdd(cnf_restricao_linhas)

    print("restrição colunas")
    cnf = restricao_colunas_teste.restricao_colunas_teste(N, c)
    #bdd_restricao_colunas = expr2bdd(cnf_restricao_colunas)

    print("restrição diagonais")
    cnf = restricao_diagonais_teste.restricao_diagonais_teste(N, c)
    #bdd_restricao_digonais = expr2bdd(cnf_restricao_diagonais)

    # Testa satisfatibilidade
    #print(bdd_cnf_n_rainhas.satisfy_count())
    #print(bdd_cnf_n_rainhas.is_zero())


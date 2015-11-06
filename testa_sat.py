__author__ = 'kiko'

from pyeda.inter import *

from subprocess import call
import os

def Export2Image(bdd, fmt, file_name):
    # Exporta o diagrama para o Graphviz (linguagem Dot)
    with open("temp.gv", "w") as hFile:
        hFile.write(bdd.to_dot())
    # Gera o PDF com o diagrama
    call(["dot", "-T" + fmt, "temp.gv", "-o" + file_name])
    os.remove("temp.gv")
#--------------------------------------------------------------------------------------------------------------------
def testa_sat(bdd_cnf_n_rainhas):


        # testa se é sat
        if bdd_cnf_n_rainhas.is_zero():
            print("UNSAT")
        else:
            print("SAT")
            print(bdd_cnf_n_rainhas.satisfy_count())
            Export2Image(bdd_cnf_n_rainhas, "pdf", "bdd_presenca.pdf")
        # testa uma solução para gerar impressão tabuleiro
        #  print(bdd_cnf_n_rainhas.satisfy_one())
        # imprime tabuleiro
        #   for cont_rainhas in range(K)
        #       imprime_tabuleiro(N, pos_rainha_x[cont_rainhas], pos_rainha_y[cont_rainhas)

        # exemplo de como imprimir grafo





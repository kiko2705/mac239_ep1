__author__ = 'Francisco Santos Nusp 794650,  Vitor Kemada Nusp'

from pyeda.inter import *
from subprocess import call
import os
import presenca_rainha
import restricao_linhas
import restricao_diagonais
import restricao_colunas
import cnf_to_string
import imprime_tabuleiro

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
    K = int(input('Entre com o número de rainhas : '))

    # define o vetor de posições x de rainha
    pos_rainha_x = [0 for x in range(K)]

    # define o vetor de posições y de rainha
    pos_rainha_y = [0 for x in range(K)]

    # cria o loop que vai entrando com X e Y de cada rainha
    for conta_posicoes in range(K):
        print("Posição X da rainha ", conta_posicoes)
        pos_rainha_x[conta_posicoes] = int(input())
        print("Posição Y da rainha ", conta_posicoes)
        pos_rainha_y[conta_posicoes] = int(input())

    # define a lista de cláusulas de disjunções
    c = [0 for x in range(N*N*N)]

    cnf_temp_rainhas = [0 for x in range(N*N*N*N)]

    cnf_rainhas = [0 for x in range(N*N*N*N)]

    cnf = [0 for x in range(N*N*N*N)]

    temp = 0

    contador_global_clausulas = 0

    # se houverem rainhas colocadas vai para módulo que calcula a cnf reduzida
    #if(K != 0):
    # calcula_cnf_com_rainhas.calcula()

    # calcula a cnf final sem rainhas

    print("presenças rainha")
    cnf_temp_rainhas = presenca_rainha.presenca_rainha(N, c)
    for cont_presenca in range(N):
        cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_presenca]
        print(cnf_rainhas[contador_global_clausulas])
        contador_global_clausulas += 1

    print("restrição linhas")
    cnf_temp_rainhas = restricao_linhas.restricao_linhas(N, c)
    #bdd_restricao_linhas = expr2bdd(cnf_restricao_linhas)
    for cont_restricao_linhas in range(N*N*N):
        if cnf_temp_rainhas[cont_restricao_linhas] == 0:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_linhas]
            contador_global_clausulas += 1
            break
        else:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_linhas]
            print(cnf_rainhas[contador_global_clausulas])
            contador_global_clausulas += 1

    print("restrição colunas")
    cnf_temp_rainhas = restricao_colunas.restricao_colunas(N, c)
    #bdd_restricao_colunas = expr2bdd(cnf_restricao_colunas)
    for cont_restricao_colunas in range(N*N*N):
        if cnf_temp_rainhas[cont_restricao_colunas] == 0:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_colunas]
            contador_global_clausulas += 1
            break
        else:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_colunas]
            print(cnf_rainhas[contador_global_clausulas])
            contador_global_clausulas += 1

    print("restrição diagonais")
    cnf_temp_rainhas = restricao_diagonais.restricao_diagonais(N, c)
    # bdd_restricao_digonais = expr2bdd(cnf_restricao_diagonais)
    for cont_restricao_diagonais in range(N*N*N):
        if cnf_temp_rainhas[cont_restricao_diagonais] == 0:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_diagonais]
            break
        else:
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_diagonais]
            print(cnf_temp_rainhas[cont_restricao_diagonais])
            contador_global_clausulas += 1

    cnf_completa = cnf_rainhas[0]

    cont = 1

    for cont in range(1, contador_global_clausulas):
        cnf_completa = cnf_completa & cnf_rainhas[cont]

    cnf_to_string.cnf_to_string(cnf_completa)

    # transforma a cnf final em bdd
    bdd_cnf_n_rainhas = expr2bdd(cnf_completa)

    # Testa satisfatibilidade e printa tabuleiro se existe solução

    #print(bdd_cnf_n_rainhas.satisfy_one())

    # testa se é satd
    #if bdd_cnf_n_rainhas.satisfy_one():
     #   print("UNSAT")
    #else:
     #   print("SAT")
    # testa uma solução
      #  print(bdd_cnf_n_rainhas.satisfy_one())
    # imprime tabuleiro
    #   for cont_rainhas in range(K)
    #       imprime_tabuleiro(N, pos_rainha_x[cont_rainhas], pos_rainha_y[cont_rainhas)





    # exemplo de como imprimir grafo
    #Export2Image(bdd, "pdf", "bdd_presenca.pdf")


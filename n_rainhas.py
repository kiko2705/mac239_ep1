__author__ = 'Francisco Santos Nusp 794650,  Vitor Kemada Nusp'

from pyeda.inter import *
from subprocess import call
import os
import presenca_rainha
import restricao_linhas
import restricao_diagonais
import restricao_colunas
import presenca_rainha_com_rainhas
import restricao_linhas_com_rainha
import restricao_colunas_com_rainhas
import restricao_diagonais_com_rainhas

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
    #pos_rainha_x = [0 for x in range(K)]
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

    cnf_temp_com_rainhas = [0 for x in range(N*N*N*N)]

    cnf_rainhas = [0 for x in range(N*N*N*N)]

    cnf_com_rainhas = [0 for x in range(N*N*N*N)]

    cnf = [0 for x in range(N*N*N*N)]

    temp = 0

    contador_global_clausulas = 0

    # aqui começa a calcular a cnf final sem rainhas
    if K == 0:
        cnf_temp_rainhas = presenca_rainha.presenca_rainha(N, c)
        for cont_presenca in range(N):
            cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_presenca]
            contador_global_clausulas += 1

        cnf_temp_rainhas = restricao_linhas.restricao_linhas(N, c)
        for cont_restricao_linhas in range(N*N*N):
            if cnf_temp_rainhas[cont_restricao_linhas] == 0:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_linhas]
                contador_global_clausulas += 1
                break
            else:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_linhas]
                contador_global_clausulas += 1

        cnf_temp_rainhas = restricao_colunas.restricao_colunas(N, c)
        for cont_restricao_colunas in range(N*N*N):
            if cnf_temp_rainhas[cont_restricao_colunas] == 0:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_colunas]
                contador_global_clausulas += 1
                break
            else:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_colunas]
                contador_global_clausulas += 1

        cnf_temp_rainhas = restricao_diagonais.restricao_diagonais(N, c)
        for cont_restricao_diagonais in range(N*N*N):
            if cnf_temp_rainhas[cont_restricao_diagonais] == 0:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_diagonais]
                break
            else:
                cnf_rainhas[contador_global_clausulas] = cnf_temp_rainhas[cont_restricao_diagonais]
                contador_global_clausulas += 1

        cnf_completa = cnf_rainhas[0]

        cont = 1

        for cont in range(1, contador_global_clausulas):
            if cnf_rainhas[cont] == 0:
                cnf_rainhas[cont] = 1
            else:
                cnf_completa = cnf_completa & cnf_rainhas[cont]

        # transforma a cnf final em bdd
        bdd_cnf_n_rainhas = expr2bdd(cnf_completa)

        # Testa satisfatibilidade e printa tabuleiro se existe solução

        # testa se é satd
        if bdd_cnf_n_rainhas.is_zero():
            print("UNSAT")
        else:
            print("SAT")
            print(bdd_cnf_n_rainhas.satisfy_count())
        # testa uma solução
        #  print(bdd_cnf_n_rainhas.satisfy_one())
        # imprime tabuleiro
        #   for cont_rainhas in range(K)
        #       imprime_tabuleiro(N, pos_rainha_x[cont_rainhas], pos_rainha_y[cont_rainhas)

        # exemplo de como imprimir grafo
        #Export2Image(bdd, "pdf", "bdd_presenca.pdf")

    # aqui começa a calcular a cnf final com rainhas
    else:
        # calcula cnf de presença com rainhas
        cnf_temp_com_rainhas = presenca_rainha_com_rainhas.cnf_presenca_com_rainhas(N, K, c, pos_rainha_x)



        for cont_presenca in range(N):
            cnf_com_rainhas[contador_global_clausulas] = cnf_temp_com_rainhas[cont_presenca]
            #print(cnf_com_rainhas[contador_global_clausulas])

        # calcula cnf de restrição de linhas com rainhas

        cnf_temp_com_rainhas = restricao_linhas_com_rainha.cnf_restricao_linhas_com_rainhas(N, K, c, pos_rainha_x)

        for cont_restricao_linhas in range(N):
            cnf_com_rainhas[contador_global_clausulas] = cnf_temp_com_rainhas[cont_restricao_linhas]
            #print(cnf_com_rainhas[contador_global_clausulas])

        # calcula cnf de restrição de colunas com rainhas

        cnf_temp_com_rainhas = restricao_colunas_com_rainhas.cnf_restricao_colunas_com_rainhas(N, K, c, pos_rainha_y)

        for cont_restricao_colunas in range(N):
            cnf_com_rainhas[contador_global_clausulas] = cnf_temp_com_rainhas[cont_restricao_colunas]
            #print(cnf_com_rainhas[contador_global_clausulas])

        # calcula cnf de restrição de diagonais com rainhas

        cnf_temp_com_rainhas = restricao_diagonais_com_rainhas.cnf_restricao_diagonais_com_rainhas(N, K, c, pos_rainha_x, pos_rainha_y)

        for cont_restricao_diagonais in range(N):
            cnf_com_rainhas[contador_global_clausulas] = cnf_temp_com_rainhas[cont_restricao_diagonais]
            #print(cnf_com_rainhas[contador_global_clausulas])

        # juntar as quatro clausulas com rainhas





__author__ = 'Francisco Santos Nusp 794650,  Vítor Kei Taira Tamada 8516250'

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
import testa_sat
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # INSERE DADOS INICIAIS ( N = TAMANHO TABULEIRO , K = NÚMERO DE RAINHAS )
    print("Este programa não funciona como esperado se 2 ou mais Rainhas estiverem nas mesmas linhas, colunas ou diagonais")
    print("Então por favor não provoque tal situação na entrada das coordenadas das Rainhas")
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

        # testa se é sat
        testa_sat.testa_sat(bdd_cnf_n_rainhas)

    # aqui começa a calcular a cnf final com rainhas
    elif (K > 0):
        # calcula cnf de presença com rainhas
        cnf_temp_com_rainhas = presenca_rainha_com_rainhas.cnf_presenca_com_rainhas(N, K, c, pos_rainha_x)

        # calcula cnf de restrição de linhas com rainhas

        cnf_temp_com_rainhas = restricao_linhas_com_rainha.cnf_restricao_linhas_com_rainhas(N, K, c, pos_rainha_x)

        # calcula cnf de restrição de colunas com rainhas

        cnf_temp_com_rainhas = restricao_colunas_com_rainhas.cnf_restricao_colunas_com_rainhas(N, K, c, pos_rainha_y)

        # calcula cnf de restrição de diagonais com rainhas

        cnf_temp_com_rainhas = restricao_diagonais_com_rainhas.cnf_restricao_diagonais_com_rainhas(N, K, c, pos_rainha_x, pos_rainha_y)

        # juntar as quatro clausulas com rainhas

    else:
        print ("Valor de K inválido")





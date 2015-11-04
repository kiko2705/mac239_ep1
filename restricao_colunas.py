__author__ = 'kiko'

from pyeda.inter import *

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


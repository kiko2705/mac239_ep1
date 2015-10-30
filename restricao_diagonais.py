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

# cláusulas de restrição a não ataques nas diagonais
# ¬r 11 ∨ ¬r 22
# ¬r 12 ∨ ¬r 21
# etc...

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))

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

print(cnf_restricao_diagonais_rainha)

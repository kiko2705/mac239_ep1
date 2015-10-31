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
# cláusulas para a restrição linhas
    # ~r11 ∨ ~r12
    # ~r21 ∨ ~r22
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
            disjuncao =  disjuncao | negacao
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

print(cnf_restricao_linhas_rainha)

# converte em bdd a cnf
bdd = expr2bdd(cnf_restricao_linhas_rainha)

#Export2Image(bdd, "pdf", "bdd_restricao_linhas.pdf")



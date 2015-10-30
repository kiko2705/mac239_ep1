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

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))

# cláusulas para a presença de uma rainha em cada linha
# r11 ∨ r12 (C1)
# r21 ∨ r22 (C2)
# etc...

linha  = 0
coluna = 0
numero_casas = N*N
contador_numero_casas = 1

# string cada casa tabuleiro (r11, r12, etc..)
nome_casa = "r"

# define string CNF
cnf = ""
cnf_final = ""

# número de cláusulas a serem criadas será NxN
for linha in range(N):
    for coluna in range(N):
        if coluna == 0:
            cnf = cnf + "("
        nome_casa = "r" + str(linha+1) + str(coluna+1)
        cnf = cnf + nome_casa
        if coluna != (N-1):
            cnf = cnf + "|"
    cnf = cnf + ")"
    cnf = cnf + "&"

if cnf.endswith('&'):
    cnf = cnf[:-1]

# converte em bdd a cnf
#bdd = expr2bdd(f)

#Export2Image(bdd, "pdf", "bdd1.pdf")



__author__ = 'kiko'

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))

# cláusulas de restrição a não ataques nas diagonais
# ¬r 11 ∨ ¬r 22
# ¬r 12 ∨ ¬r 21
# etc...

linha  = 0
coluna = 0
numero_casas = N*N
contador_numero_casas = 1

# string cada casa tabuleiro (r11, r12, etc..)
nome_casa = "r"

# define string CNF
cnf = ""

# número de cláusulas a serem criadas será NxN
for linha in range(N):
    contador_numero_casas = contador_numero_casas + 1
    for coluna in range(N):
        contador_numero_casas = contador_numero_casas + 1
        if coluna == 0:
            cnf = cnf + "("
        nome_casa = "~r" + str(linha+1) + str(coluna+1)
        cnf = cnf + nome_casa
        if coluna != (N-1):
            cnf = cnf + " | "
    cnf = cnf + ")"
    cnf = cnf + " & "
print(cnf)

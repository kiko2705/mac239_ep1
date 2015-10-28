__author__ = 'kiko'

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))
tamanho_lista_clausulas = N*N

# cláusulas de restrição a não ataques nas diagonais
# ¬r 11 ∨ ¬r 22
# ¬r 12 ∨ ¬r 21

# índice linha matriz tabuleiro
num_linhas = N
# índice coluna matriz tabuleiro
num_colunas = N

# define matriz cláusula ( C1, C2, etc... )
c = [0 for x in range(N*N)]
# define matriz temp cláusula ( C1, C2, etc... )
c_temp = [0 for x in range(N*N)]

indice_clausula = 0
linha  = 0
coluna = 0

# define a matriz de rainhas bidimensional, que representa cada rainha
r = [[0 for x in range(N)] for x in range(N)]

# loop para preencher dicionario presença rainha
# número de cláusulas a serem criadas será NxN
for linha in range(N):
    for coluna in range(N):
        r[linha][coluna] = int(input())
        print('r', linha+1, coluna+1, '=', r[linha][coluna])
        c_temp[indice_clausula] = r[linha][coluna]
        c[indice_clausula] = c[indice_clausula] | c_temp[indice_clausula]
        print('C', indice_clausula+1, '=', c[indice_clausula])
    indice_clausula = indice_clausula + 1

# define dicionario que conterá cláusulas presenca rainhas
# do tipo dic = { "r11 V r12": C1, "r21 V r22": C2}
dicionario_clausulas_presenca = {}

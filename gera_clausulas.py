__author__ = 'kiko'

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))
tamanho_lista_clausulas = N*N

# cláusulas para a presença de uma rainha em cada linha
# r11 ∨ r12 (C1)
# r21 ∨ r22 (C2)
# etc...
# índice linha matriz tabuleiro
num_linhas = N
# índice coluna matriz tabuleiro
num_colunas = N
# define matriz cláusula ( C1, C2, etc... )
#c = []
#c.append(0)
c = [0 for x in range(N*N)]
# define matriz temp cláusula ( C1, C2, etc... )
c_temp = [0 for x in range(N*N)]
#c_temp.append(0)
indice_clausula = 0

valor  = 0
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

# print('r', linha+1, coluna+1, '=', r[linha][coluna])
# define dicionario que conterá cláusulas presenca rainhas
# do tipo dic = { "r11 V r12": C1, "r21 V r22": C2}
dicionario_clausulas_presenca = {}

#----------------------------------------------------------------------------------------------------------------------


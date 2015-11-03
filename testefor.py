__author__ = 'kiko'

from pyeda.inter import *

N = 4
N_col = N
N_lin = N
inicio = 0
coluna = 0
linha = 0
r = exprvars('r', N, N)

for cont_di in range(0, N-1):
    for coluna, linha in zip(reversed(range(N_col)), range(inicio, N_lin)):
            print(r[linha][coluna])
    inicio = inicio + 1




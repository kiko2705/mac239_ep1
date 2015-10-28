__author__ = 'kiko'

# INSERE DADO INICIAL
N = int(input('Entre com o tamanho do tabuleiro : '))

# cláusulas para a presença de uma rainha em cada linha
# r11 ∨ r12 (C1)
# r21 ∨ r22 (C2)
# etc...

linha  = 0
coluna = 0

numero_clausulas = 0

# string cada casa tabuleiro (r11, r12, etc..)
nome_casa = "r"

# define dicionario que conterá cláusulas presenca rainhas
# do tipo dic = { "r11 V r12": C1, "r21 V r22": C2}
dicionario_clausulas_presenca = {}

# loop para preencher dicionario presença rainha
# número de cláusulas a serem criadas será NxN
for linha in range(N):
    for coluna in range(N):
        # coloca todos os componentes da primeira cláusula ( " r11 V r12 V etc... )
        nome_casa = nome_casa + str(linha+1) + str(coluna+1) + " V "
        print(nome_casa)
        nome_casa = "r"
    print("(C", numero_clausulas+1, ")")
    numero_clausulas = numero_clausulas + 1





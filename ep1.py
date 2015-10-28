from pyeda.inter import *

X = exprvars('x', 8, 8)

R = And(*[OneHot(*[X[r, c] for c in range(8)]) for r in range(8)])
C = And(*[OneHot(*[X[r, c] for r in range(8)]) for c in range(8)])

starts = [(i, 0) for i in range(8-2, 0, -1)] + [(0, i) for i in range(8-1)]
lrdiags = []

for r, c in starts:
    lrdiags.append([])
    ri, ci = r, c
    while ri < 8 and ci < 8:
        lrdiags[-1].append((ri, ci))
        ri += 1
        ci += 1

DLR = And(*[OneHot0(*[X[r, c] for r, c in diag]) for diag in lrdiags])

starts = [(i, 8-1) for i in range(8-2, -1, -1)] + [(0, i) for i in range(8-2, 0, -1)]
rldiags = []

for r, c in starts:
    rldiags.append([])
    ri, ci = r, c
    while ri < 8 and ci >= 0:
        rldiags[-1].append((ri, ci))
        ri += 1
        ci -= 1

DRL = And(*[OneHot0(*[X[r, c] for r, c in diag]) for diag in rldiags])

S = DLR
print(S.is_cnf())
print(len(S.xs))

S = DRL
print(S.is_cnf())
print(len(S.xs))

S = R
print(S.is_cnf())
print(len(S.xs))

S = C
print(S.is_cnf())
print(len(S.xs))

S = DLR & DRL
print(S.is_cnf())
print(len(S.xs))


def display(point):
    chars = list()
    for r in range(8):
        for c in range(8):
            if point[X[[r, c]]]:
                chars.append("Q")
            else:
                chars.append(".")
        if r != 7:
            chars.append("\n")
    print("".join(chars))












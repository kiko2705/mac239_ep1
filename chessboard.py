"""
================================================
NQueens - Produce nice LaTeX outputs for the
N-Queens puzzle, based on the 'chessboard' package
<https://www.ctan.org/tex-archive/macros/latex/contrib/chessboard>.
Crated for the discipline MAC0239 - Introdução à
Lógica e Verificação de Programas
------------------------------------------------
Author: Luiz Carlos Vieira (October 2015)
================================================

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
import argparse
from argparse import RawTextHelpFormatter


##########################################
# Return the Standard Algebraic Notation
# (SAN) for the given board square.
# Parameters:
#    row Number of the row in which the
#        square is on the board.
#    col Number of the column in which the
#        square is on the board.
# Return:
#    The SAN code for just the square po-
#    sition (that is, without the piece).
##########################################
def SAN(row, col):
    code = '%s%d' % ('abcdefghijklmnopqrstuvwxyz'[col - 1], row)
    return code


##########################################
# Main
##########################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description='Produce nice LaTeX outputs for the N-Queens puzzle, based on the \'chessboard\'\n'
                                                 'package <https://www.ctan.org/tex-archive/macros/latex/contrib/chessboard>.',
                                     epilog=u'Created for the discipline MAC0239 (Introdução à Lógica e Verificação\n'
                                            'de Programas). Author: Luiz Carlos Vieira (October 2015).\n'
                                            'Licensed under GNU General Public License <http://www.gnu.org/licenses/>.')

    parser.add_argument('-i', '--infile', metavar='FILENAME',
                        help='Use FILENAME as the input text file;\n'
                             'if not provided, input data is read from stdin.\n\n'

                             'The input format must have the following pattern:\n\n'

                             '.  .  Q  .\n'
                             'Q  .  .  .\n'
                             '.  .  .  Q\n'
                             '.  Q  .  .\n\n'

                             'Where a dot (.) means an empty square and\n'
                             'Q means a square with a queen piece.\n'
                             'The size of the board is inferred from the pattern\n'
                             'dimensions, hence the number of rows must be equal\n'
                             'to the number of columns. The smallest dimension is\n'
                             '2 x 2 and the biggest one is 26x26.'
                        )
    parser.add_argument('-o', '--outfile', metavar='FILENAME',
                        help='Use FILENAME as the output LaTeX file;\n'
                             'if not provided, output data is written to stdout')
    parser.add_argument('-c', '--complete', action='store_true',
                        help='Produce a complete LaTeX document;\n'
                             'if not provided, only the chess board code is produced')

    args = parser.parse_args()

    # Read the input data (either from a file or from the stdin)
    n = 0
    try:
        file = open(args.infile) if args.infile != None else sys.stdin

        board = []
        for line in file:
            cells = line.split()
            board.append(cells)
            if n == 0:
                n = len(cells)
            else:
                if n != len(cells):
                    raise ValueError('Input format error: columns do not have the same length')

        file.close()

        if n != len(board):
            raise ValueError('Input format error: rows and columns in the board do not have the same length')
        if n < 2 or n > 26:
            raise ValueError('Input format error: invalid board dimension %d x %d' % (n, n))

    except IOError:
        if args.infile != None:
            print("Could not read file: %s" % args.infile)
        else:
            print("Could not read stdin")
        sys.exit(1)
    except Exception as details:
        print(details)
        sys.exit(2)

    n = len(board)  # board dimensions is n x n

    # Build the code from the board
    try:

        file = open(args.outfile, 'w') if args.outfile != None else sys.stdout

        if args.complete:
            file.write(r'\documentclass{article}' + '\n')
            file.write(r'\usepackage{chessboard}' + '\n')
            file.write('\n')
            file.write(r'\begin{document}' + '\n')

        file.write(r'    \setchessboard{' + '\n')
        file.write(r'        showmover = false,' + '\n')
        file.write(r'        labelleftwidth=1.5ex,' + '\n')
        file.write(r'        clearboard' + '\n')
        file.write(r'    }' + '\n')
        file.write('\n')
        file.write(r'    \chessboard[' + '\n')
        file.write('        maxfield=%s,\n' % SAN(n, n))

        # Add the pieces
        total = sum([i.count('Q') for i in board])

        if total > 0:
            file.write(r'        setpieces={' + '\n')
            cnt = 1
            for r, row in zip(range(1, n + 1), reversed(board)):
                for c, cell in zip(range(1, n + 1), row):
                    if cell == 'Q':
                        san = SAN(r, c)
                        file.write('            q%s%s\n' % (san, ',' if cnt < total else ''))
                        cnt += 1
            file.write(r'        }' + '\n')

        file.write(r'    ]' + '\n')

        if args.complete:
            file.write(r'\end{document}' + '\n')

        file.close()

    except IOError:
        if args.outfile != None:
            print("Could not write to file: %s" % args.outfile)
        else:
            print("Could not write to stdout")
        sys.exit(3)
    except Exception as details:
        print(details)
        sys.exit(4)

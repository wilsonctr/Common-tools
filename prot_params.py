from sys import argv
from Bio import SeqIO

script, input_file = argv

output = open('out.csv', 'w')
output.write("Gene name,Extinction Coefficient,Molecular Weight,Number of residues,Protein sequence \n")

with open(input_file) as x:
    for i in SeqIO.parse(x, "fasta"):
        G = i.seq.count('G')
        A = i.seq.count('A')
        V = i.seq.count('V')
        L = i.seq.count('L')
        I = i.seq.count('I')
        M = i.seq.count('M')
        W = i.seq.count('W')
        F = i.seq.count('F')
        P = i.seq.count('P')
        S = i.seq.count('S')
        T = i.seq.count('T')
        C = i.seq.count('C')
        Y = i.seq.count('Y')
        N = i.seq.count('N')
        Q = i.seq.count('Q')
        D = i.seq.count('D')
        E = i.seq.count('E')
        K = i.seq.count('K')
        R = i.seq.count('R')
        H = i.seq.count('H')

        ext_coef = W * 5500 + Y * 1490 + C * 125
        M_W      = A * (89 - 18) + \
                   R * (174 - 18) + \
                   N * (132 - 18) + \
                   D * (133 - 18) + \
                   C * (121 - 18) + \
                   E * (147 - 18) + \
                   Q * (146 - 18) + \
                   G * (75 - 18) + \
                   H * (155 - 18) + \
                   I * (131 - 18) + \
                   L * (131 - 18) + \
                   K * (146 - 18) + \
                   M * (149 - 18) + \
                   F * (165 - 18) + \
                   P * (115 - 18) + \
                   S * (105 - 18) + \
                   T * (119 - 18) + \
                   W * (204 - 18) + \
                   Y * (181 - 18) + \
                   V * (117 - 18) + 18
        no_a_a   = A + R + N + D + C + E + Q + G + H + I + \
                   L + K + M + F + P + S + T + W + Y + V
        name = i.id
        protein_sequence = i.seq
        output.write("%s," % name)
        output.write("%s," % ext_coef)
        output.write("%s," % M_W)
        output.write("%s," % no_a_a)
        output.write("%s,\n" % protein_sequence)

output.close()

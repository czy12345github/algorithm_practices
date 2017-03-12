from collections import defaultdict

def main():
    line = raw_input("Input dimension sequence, split with ',':\n")
    p = [int(x) for x in line.split(',')]
    matrix_chain_order(p)

def matrix_chain_order(p):
    n = len(p) - 1
    m = defaultdict(lambda:defaultdict(lambda:0))
    s = defaultdict(lambda:defaultdict(lambda:0))
    for i in range(2,n + 1):
        for j in range(1,n - i + 2):
            m[j][j+i-1] = m[j+1][j+i-1] + p[j-1]*p[j]*p[j+i-1]
            s[j][j+i-1] = j
            for k in range(j + 1,j + i - 1):
                if m[j][k] + m[k+1][j+i-1] + p[j-1]*p[k]*p[j+i-1] < m[j][j+i-1]:
                    m[j][j+i-1] = m[j][k] + m[k+1][j+i-1] + p[j-1]*p[k]*p[j+i-1]
                    s[j][j+i-1] = k
    print m[1][n]

main()

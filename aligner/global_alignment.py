s = ''
t = ''
match = 0
mismatch = 0
indel = 0
dp_matrix = []

def print_matrix():
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            print(' ' + str(dp_matrix[i][j]), end='')
        print('')


def calculate():
    global dp_matrix
    for i in reversed(range(len(s))):
        dp_matrix[i][len(t)] = dp_matrix[i + 1][len(t)] + indel
    for i in reversed(range(len(t))):
        dp_matrix[len(s)][i] = dp_matrix[len(s)][i + 1] + indel
    for i in reversed(range(len(s))):
        for j in reversed(range(len(t))):
            v_h = dp_matrix[i][j + 1] + indel
            v_d = 0
            if s[i] == t[j]: 
                v_d = dp_matrix[i + 1][j + 1] + match
            else:
                v_d = dp_matrix[i + 1][j + 1] + mismatch
            v_v = dp_matrix[i + 1][j] + indel
            dp_matrix[i][j] = max(v_v, v_h, v_d)
            
def print_result():
    find_align(0, 0, '', '')

def optimal_score():
    return dp_matrix[0][0]

def find_align(row, col, align_s, align_t):
    if row < len(s) or col < len(t):
        #vertical checking
        if row < len(s) and dp_matrix[row][col] - indel == dp_matrix[row + 1][col]:
            find_align(row+1, col, align_s + s[row], align_t + '_')
        #horizontal checking
        if col < len(t) and dp_matrix[row][col] - indel == dp_matrix[row][col + 1]:
            find_align(row, col+1, align_s + '_', align_t + t[col])
        #diagonal checking
        if row < len(s) and col < len(t):
            if ((s[row] == t[col] and dp_matrix[row][col] - match ==
                dp_matrix[row + 1][col + 1]) or
                    (s[row] != t[col] and dp_matrix[row][col] - mismatch ==
                        dp_matrix[row + 1][col + 1])):
                find_align(row + 1, col+1, align_s + s[row], align_t + t[col])
    else:
        print('s: {}'.format(align_s))
        print('t: {}'.format(align_t))

def initialize(a1, a2, a3, a4, a5):
    global s, t, match, mismatch, indel, dp_matrix
    s = a1
    t = a2
    match = a3
    mismatch = a4
    indel = a5
    dp_matrix = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 6:
        print('Invalid arguments')
        sys.exit(0)
    else:
        initialize(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))

    calculate()
    print_matrix()
    print('optimal alignment score: {}'.format(dp_matrix[0][0]))
    print_result()

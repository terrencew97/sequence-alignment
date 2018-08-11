s = ''
t = ''
match = 0
mismatch = 0
indel = 0
max_row = 0
max_col = 0
dp_matrix = []

def print_matrix():
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            print(' ' + str(dp_matrix[i][j]), end='')
        print('')


def calculate():
    global max_row, max_col
    for i in reversed(range(len(s))):
        for j in reversed(range(len(t))):
            v_h = dp_matrix[i][j + 1] + indel
            v_v = dp_matrix[i + 1][j] + indel
            v_d = 0
            if s[i] == t[j]: 
                v_d = dp_matrix[i + 1][j + 1] + match
            else:
                v_d = dp_matrix[i + 1][j + 1] + mismatch
            dp_matrix[i][j] = max(v_v, v_h, v_d, 0)
            if dp_matrix[i][j] >= dp_matrix[max_row][max_col]:
                max_row = i
                max_col = j

def print_result():
    find_align(max_row, max_col, '', '', max_row, max_col)

def optimal_score():
    return dp_matrix[max_row][max_col]

def find_align(row, col, align_s, align_t, m_r, m_c):
    if row <= len(s) or col <= len(t):
        if dp_matrix[row][col] == 0:
            print('{} {} {}'.format(m_r+1, align_s, row))
            print('{} {} {}'.format(m_c+1, align_t, col))
            print('')
        #vertical checking
        if row < len(s) and dp_matrix[row][col] - indel == dp_matrix[row + 1][col]:
            find_align(row+1, col, align_s + s[row], align_t + '_', m_r, m_c)
        #horizontal checking
        if col < len(t) and dp_matrix[row][col] - indel == dp_matrix[row][col + 1]:
            find_align(row, col+1, align_s + '_', align_t + t[col], m_r, m_c)
        #diagonal checking
        if row < len(s) and col < len(t):
            if ((s[row] == t[col] and dp_matrix[row][col] - match ==
                dp_matrix[row + 1][col + 1]) or
                    (s[row] != t[col] and dp_matrix[row][col] - mismatch ==
                        dp_matrix[row + 1][col + 1])):
                find_align(row + 1, col+1, align_s + s[row], align_t + t[col],
                        m_r, m_c)
        if (dp_matrix[row][col] == dp_matrix[m_r][m_c] and row != m_r and
                col != m_c):
            find_align(row, col, '', '', row, col)

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
    print('optimal alignment score: {}'.format(optimal_score()))
    if optimal_score() > 0:
        find_align(max_row, max_col, '', '', max_row, max_col)


def levenshtein_distance(token1, token2):

    m = len(token1) + 1    # row
    n = len(token2) + 1    # column
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        matrix[i][0] = i
    for j in range(n):
        matrix[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            ins_cost = matrix[i][j - 1] + 1
            del_cost = matrix[i - 1][j] + 1
            sub_cost = matrix[i - 1][j - 1] + cost
            matrix[i][j] = min(ins_cost, del_cost, sub_cost)

    return matrix[m - 1][n - 1]


token1 = 'yu'
token2 = 'you'
print(levenshtein_distance(token1, token2))

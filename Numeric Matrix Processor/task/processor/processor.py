
def input_matrix():
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        row = input().split(' ')
        matrix.append(row)
    return (matrix, n, m)

def matrix_add(a, b):
    result = []
    for y in range(len(a)):
        rowa = a[y]
        rowb = b[y]
        result.append([int(rowa[i]) + int(rowb[i]) for i in range(len(rowa))])
    return result

def matrix_mul_c(a, const):
    result = []
    # for y in range(len(a)):
    for row in a:
        result.append([int(i) * int(const) for i in row])
    return result

a, ya, xa = input_matrix()
b = input()
# b, yb, xb = input_matrix()

# if ya != yb or ya != yb:
#     print('ERROR')
# else:
#     c = matrix_add(a , b)
c = matrix_mul_c(a, b)
for row in c:
    # print(row)
    print(' '.join(str(x) for x in row))

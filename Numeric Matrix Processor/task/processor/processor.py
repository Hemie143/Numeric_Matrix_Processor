

def input_matrix(count=None):
    if count:
        print(f'Enter size of {count} matrix:')
    else:
        print(f'Enter size of matrix:')
    n, m = list(map(int, input().split()))
    matrix = []
    int_check = True
    for _ in range(n):
        row = input().split(' ')
        row = [float(x) for x in row]
        int_check = int_check and all([x.is_integer() for x in row])
        matrix.append(row)
    if int_check:
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
    return (matrix, n, m)


def matrix_add(a, b):
    result = []
    for y in range(len(a)):
        rowa = a[y]
        rowb = b[y]
        result.append([rowa[i] + rowb[i] for i in range(len(rowa))])
    return result

def matrix_mul_c(a, const):
    result = []
    # for y in range(len(a)):
    for row in a:
        result.append([i * const for i in row])
    return result

def matrix_mul(a, b):
    result = []
    num_colb = len(b[0])
    for i, rowa in enumerate(a):
        row = []
        for j in range(num_colb):
            colb = [rowb[j] for rowb in b]
            row.append(sum(list([x * y for x, y in zip(rowa, colb)])))
        result.append(row)
    return result


def matrix_print(m):
    for row in m:
        print(' '.join(str(x) for x in row))


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('0. Exit')
    choice = input('Your choice:')
    if choice == '1':
        a, ya, xa = input_matrix('first')
        b, yb, xb = input_matrix('second')
        result = matrix_add(a, b)
        matrix_print(result)
    elif choice == '2':
        a, ya, xa = input_matrix('first')
        b = int(input())
        result = matrix_mul_c(a, b)
        matrix_print(result)
    elif choice == '3':
        a, ya, xa = input_matrix('first')
        b, yb, xb = input_matrix('second')
        result = matrix_mul(a, b)
        matrix_print(result)
    elif choice == '4':
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice = input('Your choice:')
        a, ya, xa = input_matrix('')
        result = matrix_transpose(a, choice)
        matrix_print(result)
    elif choice == '0':
        exit()

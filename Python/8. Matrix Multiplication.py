while True:
    A = []
    B = []

    row1 = int(input("How many row(s) does A matrix have: "))
    col1 = int(input("How many column(s) does A matrix have: "))
    row2 = int(input("How many row(s) does B matrix have: "))
    col2 = int(input("How many column(s) does B matrix have: "))


    if col1 == row2:
        print("\nA x B = [",row1,"x",col2,"]\n")


        for row in range(row1):
            a = []
            for col in range(col1):
                item = int(input(f'Enter {col+1}-col of {row+1}-row of A: '))
                a.append(item)
            A.append(a)
        print(f'A matrix equal to {A}\n\n\n')


        for row in range(row2):
            b = []
            for col in range(col2):
                item = int(input(f'Enter {col+1}-col of {row+1}-row of B: '))
                b.append(item)
            B.append(b)
        print(f'B matrix equal to {B}\n\n\n')

        C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k]*B[k][j]
        print(f'Result equal to {C}\n\n\n')
        
    else:
        print("\nTo multiply an m×n matrix by an n×p matrix,\nthe ns must be the same,\nand the result is an m×p matrix.\n")


    input()
A = [[1,6,3,4],
     [9,2,3,3],
     [7,4,3,4],
     [1,2,3,9]]

B = [[1,2,3,4],
     [1,4,3,4],
     [1,2,5,4],
     [1,1,3,4]]

def ADD(A, B):
     Column = []
     Result = []
     result = []
     for i in range(len(A)):
          for m in range(len(A)):
               rowA, rowB = A[i], B[i]
               result = rowA[m] + rowB[m]
               Column.append(result)
          Result.append(Column)
          Column = []
     return Result

def SUB(A, B):
     Column = []
     Result = []
     result = []
     for i in range(len(A)):
          for m in range(len(A)):
               rowA, rowB = A[i], B[i]
               result = rowA[m] - rowB[m]
               Column.append(result)
          Result.append(Column)
          Column = []
     return Result

def MUL(A, B):
     Column = []
     Result = []
     result = []
     for i in range(len(A)):
          for m in range(len(A)):
               rowA, rowB = A[i], B[i]
               result = rowA[m] * rowB[m]
               Column.append(result)
          Result.append(Column)
          Column = []
     return Result

def Minor(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )

def DET(A):
    det = 0
    for col in range(4):
        minor = [
            [A[i][j] for j in range(4) if j != col]
            for i in range(1, 4)
        ]
        cofactor = (-1) ** col * A[0][col] * Minor(minor)
        det += cofactor
    return det

def INV(A):
    det = DET(A)
    if det == 0:
        return "The matrix is not invertible."

    # Calculate the cofactor matrix
    cofactors = []
    for i in range(4):
        cofactor_row = []
        for j in range(4):
            # Get the minor matrix excluding row i and column j
            minor = [
                [A[x][y] for y in range(4) if y != j]
                for x in range(4) if x != i
            ]
            cofactor = (-1) ** (i + j) * Minor(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    # Transpose the cofactor matrix to get the adjoint
    adjoint = [[cofactors[j][i] for j in range(4)] for i in range(4)]

    # Divide each element of the adjoint matrix by the determinant
    inverse = [[adjoint[i][j] / det for j in range(4)] for i in range(4)]
    return inverse

# Example usage of the new INV function:

print("1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Deteminant\n5 = Invers")
userinput = int(input("Enter the operation that you want to do: "))
if userinput == 1:
     print(ADD(A,B))
elif userinput == 2:
     print(SUB(A,B))
elif userinput == 3:
     print(MUL(A,B)) 
elif userinput == 4:
     print(DET(A))
elif userinput == 5:
     print(INV(A))
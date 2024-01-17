import numpy as np

def advanced_numpy_operations():
    #create matrices
    matrix1=np.array([[2,4,6],[1,2,0],[3,8,6]])
    matrix2=np.array([[7,2,9],[3,6,1],[6,6,3]])

    print(matrix1)
    print(" ")
    print(matrix2)
    
    #matric multiplication
    mat_mul=np.dot(matrix1,matrix2)

    #transpose of matrix
    mat_trans1=np.transpose(matrix1)
    mat_trans2=np.transpose(matrix2)

    #matrix Eigenvalues and vectors
    eigenvalues,eigencvectors=np.linalg.eig(matrix1)

    print("multiplcation is :",mat_mul)
    print("Transpose is :",mat_trans1 ,"\n and",mat_trans2)
    # print("multiplcation is :",mat_mul)
    print("eigen values :",eigenvalues)
    print("eigen vectors :",eigencvectors)

    eigenval=np.linalg.eig(mat_mul)
    print(eigenval)
    # print(eigenvec)
advanced_numpy_operations()





import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A=np.array(A) ## convert input A into a numpy array
    N,M = A.shape # it will extract dimension of the matrix , where n is rows and m is column 
    A_T=np.zeros((M,N), dtype=A.dtype) # it will create a zero matrix 

    for i in range(N):
        for j in range(M):
            A_T[j,i]=A[i,j]
    return A_T
    
    pass

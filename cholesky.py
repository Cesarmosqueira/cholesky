import numpy as np
import random as rnd


def is_positive_definite(A): 
    return np.all(np.linalg.eigvals(A) > 0)

def get_random_matrix(n):
    A = np.random.randint(low=-10,high=10,size=(n,n))
    return np.dot(A, A.transpose())

def AXAT(mat): ### AxA'
    print(mat)
    if len(mat) <= 0 or len(mat[0]) <= 0: return []
    else:
        a = np.array(mat, dtype=np.float)
        return np.dot(a,a.transpose())
        
def fact_cholesky(a): 
    a = np.array(a, float)
    n = len(a)
    L = np.zeros(shape=(n,n))

    for col in range(n):
        for row in range(col, n):
            sumk = 0
            if row == col:
                for k in range(col):
                    sumk += L[row][k]**2
                L[row][col] = np.sqrt(a[row][col] - sumk)
            else:
                for k in range(col):
                    sumk += (L[row][k] * L[col][k])
                L[row][col] = (a[row][col] - sumk) / L[col][col]

    return L

#  coding:utf-8
import numpy as np  
import random
def squared_frobenius_norm(A,B):
    norm=0
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(A)[1]):
            norm+=pow(A[i,j]-B[i,j],2)
    return norm
def normalize_V(U,V):
    for i in range(np.shape(V)[0]):
        total=0
        for j in range(np.shape(V)[1]):
            total+=V[i,j]
        for j in range(np.shape(V)[1]):
            V[i,j]/=total
        for k in range(np.shape(U)[0]):
            U[k,i]*=total
    return U,V
def factorize(A,dim=10,iteration_num=100,seed=0):
    dim_row,dim_column=np.shape(A)
    random.seed(seed)
    U=np.matrix([[random.random() for j in range(dim)] for i in range(dim_row)])
    V=np.matrix([[random.random() for j in range(dim_column)] for i in range(dim)])
    for i in range(iteration_num):
        cost=squared_frobenius_norm(A,np.dot(U,V))
        if i%10==0: print (cost)
        if cost==0: break
        U = np.array(U) * np.array(np.dot(A, V.T) /np.dot(np.dot(U, V), V.T))  
        V = np.array(V) * np.array(np.dot(U.T,A) / np.dot(U.T,np.dot(U, V))) 
    return normalize_V(U,V)
 

U  = np.matrix([[1,0],[1,1],[1,0],[0,1]])
V  = np.matrix([[1,1,2,1,3],[1,2,1,3,1]])
A = U*V
 
U,V = factorize(A,dim=2,iteration_num = 100,seed=0)
print(U)
print()
print(V)
print()
print(np.dot(U,V))
print()
print(A)

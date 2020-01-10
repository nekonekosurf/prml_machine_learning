# coding:utf-8
import numpy as np  
from numpy import *
def squared_frobenius_norm(A,B):
    norm=0
    for i in range(shape(A)[0]):
        for j in range(shape(A)[1]):
            norm+=pow(A[i,j]-B[i,j],2)
    return norm
def normalize_V(U,V):
    for i in range(shape(V)[0]):
        total=0
        for j in range(shape(V)[1]):
            total+=V[i,j]
        for j in range(shape(V)[1]):
            V[i,j]/=total
        for k in range(shape(U)[0]):
            U[k,i]*=total
    return U,V
def factorize_S(A,dim=10,iteration_num=100,seed=0,min_imp=0.1):
    dim_row,dim_column=shape(A)
    random.seed(seed)
    U=matrix([[random.random() for j in range(dim)] for i in range(dim_row)])
    V=matrix([[random.random() for j in range(dim_column)] for i in range(dim)])
    cost_pre = 0
    for i in range(iteration_num):
        cost=squared_frobenius_norm(A,np.dot(U,V))
        if cost_pre - cost < min_imp and  cost_pre - cost >0 : #値が正で最小値よりも小さい
          break
        cost_pre = cost
        if i%10==0: print (cost)
        if cost==0: break
        U = array(U) * array(np.dot(A, V.T) /np.dot(np.dot(U, V), V.T))     
        V = array(V) * array(np.dot(U.T,A) / np.dot(U.T,np.dot(U, V)))
    return normalize_V(U,V)




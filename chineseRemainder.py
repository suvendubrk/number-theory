"""
@Author : Suvendu Barik
"""
import numpy as np

#Returns Solution as (smallest soln., n [For which modulo is given])
def chiRemSolver(A,N):
    #To make sure that the arrays are numpy based
    #If redundant, users are free to remove the code    
    A=np.array(A)
    N=np.array(N)
    #-----------------------------------------------
    PN=1 #Product of all ni terms
    for i in range(len(N)):
        PN*=N[i]
    NI=PN/N #All the Ni terms here..
    XI=[] #Getting xi terms...
    #This is the code for getting xi's to XI   
    for i in range(len(N)):
        for j in range(1,N[i]):
         if((NI[i]*j-1)%N[i]==0):
             XI.append(j)
             break
    #This is the collection of ai*Ni*xi terms    
    PRODUCT=A*NI*XI
    SUM=0 #Summation of all the values in PRODUCT
    for i in range(len(PRODUCT)):
        SUM+=PRODUCT[i]
    small = SUM%PN
    return(small,PN)

print(chiRemSolver([1,2,3],[5,6,7])) 

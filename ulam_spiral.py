#Sorry for not commenting much within codes, but
#most of the process here is easily understood.

#This method generates a 2D matrix consisting of natural numbers
#Arranged in ulam's spiral [Square spiral], having parameter
#n as size of spiral

def ulam_spiral_matrix(n):   
    M=1 
    space = [[0 for x in range(n)] for x in range(n)]   
    if(n%2!=0):
     X=int((n+1)/2)
     Y=X
    if(n%2==0):
        Y=int(n*0.5)
        X=n-Y+1
    space[X-1][Y-1]=M
    M+=1
    step=0
    size=0
    close=False
    while(M<=n**2):
        if(M%500==0):
            print(M/500," step 500 process done")
        step+=1
        if(step%2!=0):
            size+=1
            for t in range(size):
                if(M>n**2):
                    close=True
                    break
                Y+=1
                space[X-1][Y-1]=M
                M+=1
            if(close):
                break
            for t in range(size):
                X-=1
                space[X-1][Y-1]=M
                M+=1     
        if(step%2==0): 
            size+=1
            for t in range(size):
                if(M>n**2):
                    break
                Y-=1
                space[X-1][Y-1]=M
                M+=1                
            for t in range(size):
                if(M>n**2):
                    break
                X+=1
                space[X-1][Y-1]=M
                M+=1     
    return space 


#This one plots the outcome. 
def ulam_spiral_grapher(n):
 #Imports
 import matplotlib.pyplot as plt
 import numpy as np
 import sympy as sp
 #----------------------------------
 spiral=ulam_spiral_matrix(n)
 X=[x for x in range(n)]
 Y=[x for x in range(n)]
 X,Y=np.meshgrid(X,Y)
 Z=[[0 for x in range(n)]for x in range(n)]
 for i in range(n):
     for j in range(n):
         if(sp.isprime(spiral[i][j])):
             Z[i][j]=1
         else:
             Z[i][j]=0
 plt.scatter(X,Y,Z)    

#If you need to see the outcome
#ulam_spiral_grapher(100) 
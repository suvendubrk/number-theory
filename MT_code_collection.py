# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 00:39:16 2016

@author: Suvendu Barik
Roll : 1510110412
Stream : B.Sc (Research) - Physics

"""
import numpy as np
import sympy as sp

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

#These are the set of functions.... consider them as one program
def DivisorSum(f,n):
    sum=0
    for i in range(1,n+1):
        if(n%i==0):
           sum+=f(i)
    return sum

#Finding GCD of two numbers
def gcd(a,b):
    r=max(a,b)%min(a,b)
    if(r==0):
        return min(a,b)
    else:
        return gcd(r,min(a,b))

#Number therotic functionsz
def U(n):
    return 1

def N(n):
    return n

def I(n):
    if(n==1):
        return 1
    else:
        return 0
        
def tau(n):
 return DivisorSum(U,n)
 
def rho(n):
 return DivisorSum(N,n)

def phi(n):
    count=0
    for i in range(1,n+1):
        if(gcd(n,i)==1):
            count+=1
    return count        

 
#----Working on perfect numbers----
def checkPerfect(n):
    return rho(n)==(2*n)

#Returns the value n for the perfect number of form (2^n(2^(n-1)-1)).
#And, this one is not so good enough right now
def getMersenePower(m,sC=1e6):
    if(m%2!=0):
        return "~"
    if(not checkPerfect(m)):
        return "~"
    n=0
    temp=m
    while(temp%2==0):
        temp=temp/2
        n+=1
        if (n>sC):
            return "Maximum limit reached"
    return(n+1)  

#-------------------------- 

#This program will return list of primitive roots modulo n
def priRoots(n):
    output=[]
    totient_n = sp.ntheory.totient(n)
    for a in range (1,n):
      if(gcd(a,n)==1):
         if(sp.ntheory.n_order(a,n)==totient_n):
              output.append(a)
    return output          
#Well, that's simple enough
#print(priRoots(15))    
    
 
#This one finds quadratic residues and non-quadratic residues (Obviously, modulo p)
#as a set [[set of quadratic residues],[set of non-quadratic residues]]. Used gauss lemma
#which is better than euler criteria in  computation
def quadResidue(p):
   #Check whether p is prime and odd
    if(not sp.isprime(p)):
        return "~"
    if(p%2==0):
        return "~"
    #This are the variables storing outputs
    quadR=[]
    quadNR=[]
    #Making array S with numeral count 1 to (p-1)/2
    S=[]
    #This iss... the loop process for making S when a=1
    for j in range(1,int((p-1)/2)+1):
        S.append(j)
    #This operation is required for 
    #numpy based functionalities    
    S=np.array(S) 
    #Iterating for each a less than p, greater than 1   
    for a in range(1,p):
       SNew=S*a #Makes life easy, as we can make S with any a
       SNew%=p #Left reminders
       n=0 #Count of remainders greater than p/2
       #For the count of n, so to get the power
       for i in range(len(SNew)):
           if(SNew[i]>(p/2)):
               n+=1
       #Lengndre symbol operation        
       if((-1)**n==1):
           quadR.append(a)
       else:
           quadNR.append(a)
    return[quadR,quadNR]    


#Visual programs...
#There's a program, making graph between n and phi(n)
def grapher_totient(n):
    import matplotlib.pyplot as plt
    X=[]
    Y=[]  
    
    for i in range(1,n+1):
        X.append(i)
        Y.append(sp.totient(i))
        if(i%500==0):
            print(i," segment "," covered")
    plt.plot(X,Y)

#Why not with tau?!!
def grapher_tau(n):
    import matplotlib.pyplot as plt
    X=[]
    Y=[]  
    
    for i in range(1,n+1):
        X.append(i)
        Y.append(tau(i)+sp.totient(i))
        if(i%500==0):
            print(i," segment "," covered")
    plt.plot(X,Y)

#grapher_totient(100)
#grapher_tau(100)
#print(sp.totient(10),tau(10))
'''
Observation - 
1. totient returns number of coprimes
2. tau returns number of divisors
3. totient + tau returns what?
'''

#This one creates Ulam's spirals in arrays.

#Here n is the size of the spiral (square)
def ulam_spiral_matrix(n): 
    M=1
    space = [[0 for x in range(n)] for x in range(n)] 
    
    def val(M):
        if(sp.isprime(M)):
            return 1
        else:
            return 0
            
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
        step+=1
        
        if(step%2!=0):
            size+=1
            for t in range(size):
                if(M>n**2):
                    close=True
                    break
                Y+=1
                space[X-1][Y-1]= val(M)
                M+=1
            if(close):
                break
            for t in range(size):
                X-=1
                space[X-1][Y-1]=val(M)
                M+=1 
                
        if(step%2==0): 
            size+=1
            for t in range(size):
                if(M>n**2):
                    break
                Y-=1
                space[X-1][Y-1]=val(M)
                M+=1                
            for t in range(size):
                if(M>n**2):
                    break
                X+=1
                space[X-1][Y-1]=val(M)
                M+=1  
                
    return space 

#This one plots the Ulam Spiral (n is length of side of ulam spirals)
#Means, n^2 numbers will be plotted in the spiral
def ulam_spiral_grapher(n):
 import matplotlib.pyplot as plt
 Z=ulam_spiral_matrix(n)
 X=[x for x in range(n)]
 Y=[x for x in range(n)]
 X,Y=np.meshgrid(X,Y)
 print("This one is done... hopefully")
 plt.scatter(X,Y,Z)   

#ulam_spiral_grapher(2000)         
             
 
       


            
        
        
    

    

 


 
    

     
        
        
        
            
        
        
        


 


 
 
    
           
    
    

        
         
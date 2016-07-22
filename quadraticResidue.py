import numpy as np
import sympy as sp

#This one finds quadratic residues and non-quadratic residues (Obviously, modulo p)
#as a set [[set of quadratic residues],[set of non-quadratic residues]]. Used gauss lemma
#which is better than euler criteria
 
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
    #This iss the loop process for making S when a=1
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
   
print(quadResidue(11))

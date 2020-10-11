# THIS PROGRAM IS COMPUTATIONALY 
# VERY Cheap AND VERY VERY Fast
# TAKES Small MEMORY AND TIME
# A GOOD ALGORITHM
from datetime import datetime
import time

#0-0-1-2-3-4-7
# this is the code to find the series
def fibonocchi_full_series(nterms):
    n1,n2 = 0,1
    count = 0
    if nterms <=0:
        return
    elif nterms == 1 :
        print(n1)
    else:
        while count <= nterms:
            print(n1)
            n1,n2 = n2,n1+n2
            count+=1

#fibonocchi_full_series(15)

def fibonacchi(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid")
    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            a,b = b,a+b
        return b ## b is the last point of the array

print(fibonacchi(50))


def fib_with_list(n):
    l=[]                    ## define an empty list
    a = 0                   ## set two initial value
    b = 1
    l.append(a)             ## push the initial value 
    l.append(b)             ## push the initial value
    if n <0:                ## in negative stop
        return 
    if n==0:                ## if 0 then the firstelement
        return l[a]     
    if n==1:                ## if 1 then the second element
        return l[b]
    else:
        for item in range(2,n+1):
            l.append(l[item-1]+l[item-2])
            # for every position add the sum of the value of he previous 
            # index value and the value of its preious
            # push it to the array

    print(l.pop()) ## pop the last element to see the last result


fib_with_list(50)

   

        
            

        

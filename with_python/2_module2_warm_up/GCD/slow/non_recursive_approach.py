## this is a slow Approach
## take huge time
## inefficent


# 100/30 = (5x2x5x2)/(5x3x2) = (10/3) = GCD=>10
# 100/50 = (4,2) = 25
# 500,200,200 = (5,2,2) = 100
## remember this the GCD will of course lower than the 
## small number of two number that are input

def gcd_slow(number1,number2):
    biggest_number = 0 ## set the GCD numbe rinitial value 0
    low = min(number1,number2)  ## find the minimum number because ne ned to apply loop upto this
    for item in range(1,low):   ## loop througn it but dont include 0 cant devide with 0
        if number1%item == 0 and number2 % item ==0: ## if both are divisible then
            biggest_number = max(biggest_number,item) ## find if the numbe ris bigger than the crrent that are in the varibale
                                                      ## if it is then set the big value to the current value
    print(biggest_number)

#gcd_slow(100,50) 

def gcd_with_list(numbers):
    biggest_number = 0  ## set the biggest number to 0
    low = min(numbers)  ## find the minimum
    #print(low)

    for item in numbers: ## for every number in the list
        for i in range(1,low): ## check if it divisible with the number startting from 0 up to this -1
            if item%i ==0:
                biggest_number = max(biggest_number,i)  ## same store the biggest
    print(biggest_number)

gcd_with_list([500,200,100])
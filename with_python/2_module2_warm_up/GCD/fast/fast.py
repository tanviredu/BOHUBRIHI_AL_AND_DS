## THIS IS LIMITED TO TWO NUMBER
## EXTREMELY FAST

## This is the algorithm
## take the two number
## find the minimum
## devide the max with the min
## then replace the max position with the min
# and min with the reminder
# when the reminder becomes the zeo
# then in that point the divider will be the ans


# what the lemman behind this 
#Let a, b, q, and r be integers such that a = bq + r and b 6= 0. Then gcd(a, b) =
#gcd(b, r).



def gcd_ecludian(a,b):
    while b:
        a,b = b,a%b
    return b 
    # why a isnt it showud be b. Yes but we already assigned b to a up to this point
    # and we b is changed to a%b
    # because we already give b to a
    # so a is the result

print(gcd_ecludian(500,200))
## ans should be 200
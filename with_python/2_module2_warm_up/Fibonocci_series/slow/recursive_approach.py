# THIS PROGRAM IS COMPUTATIONALY 
# VERY EXPENSIVE AND VERY VERY SLOW
# TAKES HUGE MEMORY AND TIME
# NOT A GOOD ALGORITHM
from datetime import datetime
import time

def recursive_febo(n):
    if n<=1:
        return n
    else:
        return recursive_febo(n-1)+recursive_febo(n-2)

def test():
    ## this test will test the time
    test_case = [1,2,3,4,5,6,7,8,8,9,10,11,12,13,14,15]
    for item in test_case:
        print("[+] position :{} Value :{}".format(item,recursive_febo(item)))
    print("[+] Finished")

start_time = datetime.now()
test()
end_time = datetime.now()
print("[+] execution time : {}".format(end_time-start_time))


from datetime import datetime
import time
import random

def naieve_test(a):
    max_product = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)): ## dont multiply with itself its pair wise multiplication
            max_product = max(max_product,a[i]*a[j])
    return max_product

def test():
    correct_result = [81,72,4000, 400000, 40000000, 4000000000, 400000000000, 40000000000000]
    result = []
    array_list = [[9,8,9,8,5],[1,2,3,4,5,6,7,8,9],[10,30,40,100],[100,300,400,1000],[1000,3000,4000,10000],[10000,30000,40000,100000],[100000,300000,400000,1000000],[1000000,3000000,4000000,10000000]]
    for ar in array_list:
        result.append(naieve_test(ar))
    
    for itrue,itest in zip(correct_result,result):
        assert(itrue==itest)
    print("[+] Test Passed")
start_time = datetime.now()
test()
end_time = datetime.now()
print("[+] execution time : {}".format(end_time-start_time))
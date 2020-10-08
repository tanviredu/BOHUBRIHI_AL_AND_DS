from datetime import datetime
import time 
import random

def sum_of_two(number1,number2):
    return int(number1)+int(number2)


def test():
    correct_result = [3, 5, 9, 700000000]
    result = []
    mylist = [[1,2],[2,3],[4,5],[300000000,400000000]]
    for item in mylist:
        result.append(sum_of_two(item[0],item[1]))
    
    for itrue,ires in zip(correct_result,result):
        assert(itrue==ires)
    print("[+] Test Passed")

start_time = datetime.now()
test()
end_time = datetime.now()
print("[+] execution time : {}".format(end_time-start_time))   

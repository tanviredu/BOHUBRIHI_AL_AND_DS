from datetime import datetime

def max_pair_wise_product(input_list):
    max_1 = max(input_list)
    input_list.remove(max_1)
    max_2 = max(input_list)
    m_product = max_1*max_2
    return m_product

def test():
    correct_result = [72,4000, 400000, 40000000, 4000000000, 400000000000, 40000000000000]
    result = []
    array_list = [[1,2,3,4,5,6,7,8,9],[10,30,40,100],[100,300,400,1000],[1000,3000,4000,10000],[10000,30000,40000,100000],[100000,300000,400000,1000000],[1000000,3000000,4000000,10000000]]
    for ar in array_list:
        result.append(max_pair_wise_product(ar))
    for itrue,itest in zip(correct_result,result):
        assert(itrue==itest)
    print("[+] Test Passed")

start_time = datetime.now()
test()
end_time = datetime.now()
print("[+] execution time : {}".format(end_time-start_time))    




from datetime import datetime

def max_pair_wise_product(input_list):
    input_list = set(input_list)
    max_1 = max(input_list)
    input_list.remove(max_1)
    max_2 = max(input_list)
    m_product = max_1*max_2
    return m_product

def test():
    correct_result = [20]
    array_list = [[5,5,4]]
    result =[]
    for ar in array_list:
        result.append(max_pair_wise_product(ar))
    for itrue,itest in zip(correct_result,result):
        assert(itrue==itest)
    print("[+] Test Passed")

start_time = datetime.now()
test()
end_time = datetime.now()
print("[+] execution time : {}".format(end_time-start_time))    




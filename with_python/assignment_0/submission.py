def max_pairwise_product(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    m_product = max_1*max_2
    return m_product



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))




#    your solution    
# ----------------
# 1) 39999200004      
# 2) 39999600001      
# 3) 39999200004      
# 4) 40000000000      
# 5) 39996800064      
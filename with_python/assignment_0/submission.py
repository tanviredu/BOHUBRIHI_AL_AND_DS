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


#    your solution    naieve solution
# --------------------------------
# 1) 39974204004      39974204004
# 2) 39961403762      39961403762
# 3) 39987200768      39987200768
# 4) 39964007524      39964007524
# 5) 39946606480      39946606480
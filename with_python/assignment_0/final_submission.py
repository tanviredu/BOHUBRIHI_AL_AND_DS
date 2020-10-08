def max_pairwise_product(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    m_product = max_1*max_2
    return m_product


def process_data(file_path):
    data = open(file_path)
    df = data.readlines()
    df = (df[0].split(' '))
    result = []
    for item in df:
        result.append(int(item))
    return result


def main():
    ## there was a new line after the first number in the data file
    ## i changed it so that i can split

    filePath_list = ['data/1','data/2','data/3','data/4','data/5']
    for path in filePath_list:
        numbers = process_data(path)
        print(max_pairwise_product(numbers))

main()
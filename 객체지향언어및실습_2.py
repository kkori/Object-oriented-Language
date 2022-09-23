from collections import Counter
from collections import OrderedDict
import itertools

def pb1(word):
    num_list = Counter(word).most_common() #모두 출력
    result = []

    for i in range(0, len(num_list)):
        if num_list[i][1] is num_list[0][1]:
            result.append(num_list[i][0])

    result = sorted(result)

    return print(''.join(result))

def pb2(num):
    uni_list = list(OrderedDict.fromkeys(num))

    return uni_list

def pb3(two_list):
    res_list = list(itertools.chain(*two_list))
    return res_list

if __name__ == "__main__":
    # 1번 문제
    check = 0
    while check < 1:
        word = list(input("문자열을 입력하시오 >> ").lower())
        if len(word) >= 1 and len(word) <= 100:
            check += 1
    pb1(word)

    # 2번 문제
    number = list(map(int,input("enter integer number >> ").split()))
    print(f'{number} ---> {pb2(number)}')

    # 3번 문제
    ori_list = []
    for _ in range(3):
        ori_list.append(list(map(int,input("one list input >> ").split())))

    print(f'2차원 리스트: {ori_list} \n1차원 리스트: {pb3(ori_list)}')
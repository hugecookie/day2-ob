import random

# chap 3
# print(2 * 2 * 2 * 2 * 2)
# print(2**5)
# print(pow(2, 5))
# print(divmod(9, 5))
# print(type(divmod(9, 5)))
# print(type((1, 2)))
# test = (1, 2)
# # packing 하나의 tuple로 묶는다.
# print(type(test))
# print(test)
# print(test[1])
# a, b = test
# # unpacking 하나씩 할당
# print(a, b)
#
# # 2진수 8진수 16진수
# number = 32
# print(bin(number))
# print(oct(number))
# print(hex(number))
# print(ord(number))

# Chap 4
# 4-1 주석달기

# print(ord('a'))
# print(hex(ord('a')))

# 4-2 if
# a = []
# print(bool(a))
# a.append(5)
# print(bool(a))
# print(bool([set()]))
# print(bool([dict()]))
# print(bool(''))


# 4-5 multiple comparison

# vowels = 'aeiou'
# letter = 'o'
# if letter in vowels:
#     print("실행 됨!")
limits = 20
tweets = "pass" * random.randint(1, 10)
# 1에서 10 사이의 정수가 임의로 발생
diff = limits - len(tweets)
# if diif >= 0:

if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)}초과')



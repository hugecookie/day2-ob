import random

# chap 2
# 파이썬은 객체다
# 타입 이름을 정하는 대에는 여러 종류가 존재한다. 굳이 외울 필요는 없고 검색하거나 중요한 몇개만 간추리면 된다.
# 특별히 외워야 할 것은 딕셔너리인데 "준석:남자, 연수:여자"이런 형태로 만들어져 있다.
# 파이썬에서 객체는 값을 변경할 수 있지만 타입은 변경할 수 없다.(변경 시엔 함수 사용)
# 변수는 할당이 가능하며 = 기호를 사용한다. 이 내용은 print를 이용해 출력할 수 있다.
# 타입을 알아 내는 함수는 type함수를 사용하나 특정 함수인지 판단하는 함수는 isinstance를 쓴다.
#
# 2.1
# prince = 99
# print(prince)
# 2.2
# type(5)
# 2.3
# type(2.0)
# 2.4
# type(5+ 2.0)
#
#
# chap 3
# [3-1 boolean]
# bool(45)
# [3-2-1 literal integer]
# 1_000_000
# [3-2-2 operator]
# +, -, *, **, /, //, %
# [3-2-3]
# temp = 95
# print(temp)
# temp = temp - 3
# print(temp)
# temp -= temp - 3
# temp += temp - 3
# temp *= temp - 3
# temp /= temp - 3
# divod(9,5)
# [3-2-4]
# -5 ** 2
# (-5) ** 2
# [3-2-5 base]
# 0b, 0o, 0x
# bin(), oct(), hex() 2, 8, 16
# chr()
# ord() ascii code
# [3-2-6 type exchange]
# int(), bool(), int('10', 2)
#
# print(2 * 2 * 2 * 2 * 2)
# print(2**5)
# print(pow(2, 5))
# 다 같은 32를 구하는 법
# print(divmod(9, 5))
# print(type(divmod(9, 5)))
# print(type((1, 2)))
# test = (1, 2)
# packing 하나의 tuple로 묶는다.
# print(type(test))
# print(test)
# print(test[1])
# a, b = test
# unpacking 하나씩 할당하여 tuple이 아니다.
# print(a, b)
#
# 3-6 1. sec = min*60, min = 60*hour
#        hour = 1
#     2. seconds_per_hour =  sec
#     3. day = seconds_per_hour * 24
#     4. seconds_per_day = day
#     5. seconds_per_day/seconds_per_hour
#     6. seconds_per_day//seconds_per_hour
#
# Chap 4 if
# [4-1 #]
# seconds_per_day = 86400 # 60 sec/min * 60 min/hr * 24 hr/day
# [4-2 \]
# sum = 1 + \
# 2 + \
# 3 + \
# 4
#
# [4-3 if, elif, else]
# furry = True
# large = True
# if furry:
#     if large:
#         print("It's a yeti.")
#     else:
#         print("It's a cat!")
# else:
#     if large:
#         print("It's a yeti.")
#     else:
#         print("It's a human. Or a hairless cat.")
# print(ord('a'))
# print(hex(ord('a')))
#
# ==, !=, <, <=, >, >=
#
# [4-4 True, False]
# none, 0, 0.0, ' ', [ ], { }, set( )
#
# 4-5 multiple comparison
#
# vowels = 'aeiou'
# letter = 'o'
# if letter in vowels:
#     print("실행 됨!")
# limits = 20
# tweets = "pass" * random.randint(1, 10)
# 1에서 10 사이의 정수가 임의로 발생
# diff = limits - len(tweets)
# if diif >= 0:
#
# if diff >= 0:
#     print(tweets)
# else:
#     print(f'글자 수 {abs(diff)}초과')
#
#

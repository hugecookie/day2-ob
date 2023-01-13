# 4-1
import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)
print(secret, guess)

if secret == guess:
    print('just right!')
elif secret > guess:
    print('too high!')
elif secret < guess:
    print('too low!')

# 이후에 반복해서 이를 비교하여 secret을 구하는 법을 알고 싶습니다.

# 4-2
small = False
green = True

if small == True:
    if green == True:
        print("pea")
    else:
        print("cherry")
else:
    if green == True:
        print("watermelon")
    else:
        print("pumpkin")
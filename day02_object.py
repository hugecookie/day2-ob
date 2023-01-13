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
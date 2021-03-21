import random

tries = 0
print("---Welcome To The GuessNum Finder Game---\n")
try:
    RANGE = str(input("Enter The Range Of Your Number (ex: 1-100): "))
except:
    print("\nInput Isn't a Number")
    exit()

MAX_NUM = int(RANGE.split("-")[1])
MIN_NUM = int(RANGE.split("-")[0])
MAIN = MAX_NUM - MIN_NUM
while True:
    tries += 1
    if abs(MAX_NUM - MIN_NUM) > 10:
        half = int(MAX_NUM - (MAX_NUM - MIN_NUM) / 2)
        Q = input(f"Is Your Number Bigger Than {int(half)}? Y/N ")
        if Q == "Y" or Q == "y":
            MIN_NUM = int(half)
        else:
            MAX_NUM = int(half)
    else:
        guessed = []
        for i in range(int(MAX_NUM - MIN_NUM)):
            tries += 1
            guess = random.choice([i for i in range(MIN_NUM, MAX_NUM) if i not in guessed])
            guessed.append(guess)
            Q = input(f"Is Your Number = {guess}? y/n ")
            if Q == "Y" or Q == "y":
                input(f"Total Tries: {tries - 1}")
                exit()
            else:
                pass
        input("Sry Couldn't Find Your Number!")
        break

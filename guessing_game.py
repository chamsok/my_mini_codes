import random

def get_level():
    while True:
        try:
            level = int(input("Please enter a level (positive integer): "))
            if level > 0:
                return level
        except ValueError:
            print("Invalid Input!")
            pass

def get_guess(number):
    while True:
        try:
            guess = int(input("Please guess the number: "))
            if guess > 0:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    return
        except ValueError:
            print("Invalid Input!")
            pass

def main():
    level = get_level()
    number = random.randint(1, level)
    get_guess(number)

if __name__ == "__main__":
    main()

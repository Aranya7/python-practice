import random

def main():
    guessNum = str(input("Enter a three digit number: "))
    randomNum = str(random.randrange(100,1000))
    print("The lotery number is " + randomNum)
    if guessNum == randomNum:
        print("You have won $10,000!")
    else:
        if all((guessNum[0] in randomNum, guessNum[1] in randomNum, guessNum[2] in randomNum)):
            print("You have won $3,000!")
        elif any((guessNum[0] in randomNum, guessNum[1] in randomNum, guessNum[2] in randomNum)):
            print("You have won $1,000!")
        else:
            print("You Lose!")
if __name__ == "__main__":
    main()

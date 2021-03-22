def divide(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: divide by zero is not accepted')

print(divide(42))
print(divide(0))


cats = input('How many cats do you have?')
def catReview(cats):
    try:
        if int(cats) >= 5:
            print('That\'s a lot of cats!')

        elif int(cats) <0:
            print("Are you crazy??")
        elif int(cats) == 0:
            print("You should have one... I love cats ughhh")
        else:
            print('That\'s not too many... I\'m not impressed')
    except ValueError:
        print("The value is not acceptable")

catReview(cats)

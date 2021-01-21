# number checker

valid = False
while not valid:

    error = "Please enter a number that is more than zero"

    try:
        number_to_check = float(input("Number: "))

        if number_to_check <= 0:
            print(error)
        else:
            print(number_to_check)
            valid = True

    except ValueError:
        print(error)



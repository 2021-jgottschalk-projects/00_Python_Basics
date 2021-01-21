# number checker


# Function Code
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:
            number_to_check = float(input(question))

            if number_to_check <= 0:
                print(error)
            else:
                return number_to_check

        except ValueError:
            print(error)


# Main Routine
width = num_check("Width: ")
height = num_check("Height: ")
print()
print("Width: {}".format(width))
print("Height: {}".format(height))



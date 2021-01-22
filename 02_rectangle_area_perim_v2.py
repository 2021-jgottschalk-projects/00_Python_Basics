# calculates the area and perimeter of a rectangle
# v2 - loops


# Functions go here
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


# Main routine starts here
keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    print()

    # calculate Area
    area = width * height
    perimeter = 2 * (width + height)

    # Output area and perimeter
    print("Area: {:.2f} square units".format(area))
    print("Perimeter: {:.2f} units".format(perimeter))

    print()
    keep_going = input("Press <enter> to go again or "
                       "any key to quit")
    print()


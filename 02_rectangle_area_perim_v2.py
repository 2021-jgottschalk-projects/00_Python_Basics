# calculates the area and perimeter of a rectangle
# v2 - loops

keep_going = ""
while keep_going == "":

    # Get width and height
    width = float(input("Width: "))
    height = float(input("Height: "))

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


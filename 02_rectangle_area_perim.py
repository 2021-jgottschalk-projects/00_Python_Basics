# calculates the area and perimeter of a rectangle

# Get width and height
width = float(input("Width: "))
height = float(input("Height: "))

# calculate Area
area = width * height
perimeter = 2 * (width + height)

# Output area and perimeter
print("Area: {:.2f} square units".format(area))
print("Perimeter: {:.2f} units".format(perimeter))


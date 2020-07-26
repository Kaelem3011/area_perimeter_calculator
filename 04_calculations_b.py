# math function "pi"
from math import pi


# int only function
def int_only(question, error):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            # If response is blank, print error
            if response == "":
                print(error)
                continue
            else:
                return response
        except ValueError:
            print(error)
            continue


# string checker function
def string_checker(question):
    valid = False
    while not valid:
        # list of valid shapes for the component
        shapes_list = ["circle", "square", "rectangle", "half_circle", "parallelogram"]
        response = input(question).lower()

        for item in shapes_list:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Your response may only be equal to one of the given options")


# calculations for user shape function
def calculate(shape):
    # if user shape is a square
    if shape == "square":
        # user side 1 input
        side_1 = int_only("What value is one of your squares sides? ",
                          "Your response may only be a number")
        # square calculations
        area = side_1 * side_1
        perimeter = side_1 * 4

    # if user shape is a circle
    if shape == "circle":
        # user radius input
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        # circle calculations
        area = pi * radius * radius
        perimeter = 2 * pi * radius

    # if user shape is a rectangle
    if shape == "rectangle":
        # user side 1 input
        side_1 = int_only("What value is your rectangles first side? ",
                          "Your response may only be a number")
        # user side 2 input
        side_2 = int_only("What value is your rectangles second side? ",
                          "Your response may only be a number")
        # rectangle calculations
        area = side_1 * side_2
        perimeter = side_1 * 2 + side_2 * 2

    # if user shape is a half circle
    if shape == "half_circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        # half circle calculations
        area = (pi * radius * radius) / 2
        perimeter = (pi * radius + (2 * radius))

    # if user shape is a parallelogram
    if shape == "parallelogram":
        # user side 1 input
        side_1 = int_only("What value is your parallelograms first side? ",
                          "Your response may only be a number")
        # user side 2 input
        side_2 = int_only("What value is your parallelograms second side? ",
                          "Your response may only be a number")
        # parallelogram calculations
        area = side_1 * side_2
        perimeter = 2 * side_1 + 2 * side_2

    # calculations print statement
    print("Your {} area is {:.2f}".format(shape, area))
    print("Your {} perimeter is {:.2f}".format(shape, perimeter))


# Main routine
# user shape input
user_shape = string_checker("What is your chosen shape? ")
# user dimensions input
dimensions = calculate(user_shape)

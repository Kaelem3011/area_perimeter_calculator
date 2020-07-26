# math pi function
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

        # list of valid shapes
        shapes_list = ["circle", "square", "rectangle", "half_circle", "parallelogram", "triangle"]
        response = input(question).lower()

        for item in shapes_list:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Your response may only be equal to one of the given options")


# calculation function (also gathers areas, shapes and perimeters for list)
def calculate(shape, shape_list=[], area_list=[], perimeter_list=[]):
    # history is defined as the shape, area, and perimeter
    history = [shape_list, area_list, perimeter_list]

    # if shape is a square
    if shape == "square":
        # user side 1 input
        side_1 = int_only("What value is one of your squares sides? ",
                          "Your response may only be a number")
        # square calculations
        area = side_1 * side_1
        perimeter = side_1 * 4

    # if shape is a circle
    if shape == "circle":
        # user radius input
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        # circle calculations
        area = pi * radius * radius
        perimeter = 2 * pi * radius

    # if shape is a rectangle
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
        # user radius input
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

    # if shape is a triangle
    if shape == "triangle":
        # user base input
        base = int_only("What value is your triangles base? ",
                        "Your response may only be a number")
        # user height input
        height = int_only("What value is your triangles height? ",
                          "Your response may only be a number")
        # user side 1 input
        side_1 = int_only("What value is your triangles first other side? ",
                          "Your response may only be a number")
        # user side 2 input
        side_2 = int_only("What value is your triangles second other side? ",
                          "Your response may only be a number")
        # triangle calculations
        area = base / 2 * height
        perimeter = base + side_1 + side_2

    # users area and perimeter print statement
    print()
    print("==========================")
    print("Your {} area is {:.2f}".format(shape, area))
    print("Your {} perimeter is {:.2f}".format(shape, perimeter))
    print("==========================\n")

    # history order
    history[0].append(shape)
    history[1].append(area)
    history[2].append(perimeter)

    # loops component
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Press enter to keep going or any key to access game summary")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    loop = input("")
    print("")

    if loop == "":
        return loop
    else:
        # history print statement
        i = 0
        while i < len(history[0]):
            print("-----------------")
            print("{} Area is {:.2f}".format(history[0][i], history[1][i]))
            print("{} Perimeter is {:.2f}".format(history[0][i], history[2][i]))
            print("-----------------")
            i += 1
            print()

# Main routine
# uses loop


# instructions
print("Welcome to the Area | Perimeter calculator\n"
      "The shapes available to be calculated are...\n"
      "Square\n"
      "Rectangle\n"
      "Circle\n"
      "Half Circle\n"
      "parallelogram\n"
      "triangle\n")

loop = ""
while loop == "":
    # user shape input
    user_shape = string_checker("What is your chosen shape? ")
    # user dimensions input
    dimensions = calculate(user_shape)

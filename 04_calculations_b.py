from math import pi


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


def string_checker(question):
    valid = False
    while not valid:

        shapes_list = ["circle", "square", "rectangle", "half_circle", "parallelogram"]
        response = input(question).lower()

        for item in shapes_list:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Your response may only be equal to one of the given options")


def calculate(shape):
    if shape == "square":
        side_1 = int_only("What value is one of your squares sides? ",
                          "Your response may only be a number")
        area = side_1 * side_1
        perimeter = side_1 * 4

    if shape == "circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        area = pi * radius * radius
        perimeter = 2 * pi * radius

    if shape == "rectangle":
        side_1 = int_only("What value is your rectangles first side? ",
                          "Your response may only be a number")
        side_2 = int_only("What value is your rectangles second side? ",
                          "Your response may only be a number")
        area = side_1 * side_2
        perimeter = side_1 * 2 + side_2 * 2

    if shape == "half_circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        area = (pi * radius * radius) / 2
        perimeter = (pi * radius + (2 * radius))

    if shape == "parallelogram":
        side_1 = int_only("What value is your parallelograms first side? ",
                          "Your response may only be a number")
        side_2 = int_only("What value is your parallelograms second side? ",
                          "Your response may only be a number")
        area = side_1 * side_2
        perimeter = 2 * side_1 + 2 * side_2

    print("Your {} area is {:.2f}".format(shape, area))
    print("Your {} perimeter is {:.2f}".format(shape, perimeter))


# Main routine
user_shape = string_checker("What is your chosen shape? ")
dimensions = calculate(user_shape)

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


def calculate(shape, shape_list=[], area_list=[], perimeter_list=[]):
    history = [shape_list, area_list, perimeter_list]

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
    history[0].append(shape)
    history[1].append(area)
    history[2].append(perimeter)

    keep_going = input("Press enter to keep going or any key to exit\n")
    if keep_going == "":
        return keep_going
    else:
        i = 0
        while i < len(history[0]):
            print("-------")
            print("{} Area is {:.2f}".format(history[0][i], history[1][i]))
            print("{} Perimeter is {:.2f}".format(history[0][i], history[2][i]))
            print("-------")
            i += 1


# Main routine

# instructions
print("Welcome to the Area | Perimeter calculator\n"
      "The shapes available to be calculated are...\n"
      "Square\n"
      "Rectangle\n"
      "Circle\n"
      "Half Circle\n"
      "parallelogram\n")

keep_going = ""
while keep_going == "":

    user_shape = string_checker("What is your chosen shape? ")
    dimensions = calculate(user_shape)

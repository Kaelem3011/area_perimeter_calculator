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


def shape_dimensions(shape):

    if shape == "square":
        side_1 = int_only("What value is one of your squares sides? ",
                          "Your response may only be a number")
        print("All of the squares sides are equal to {}".format(side_1))

    if shape == "circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        print("Your circles radius is equal to {}".format(radius))

    if shape == "rectangle":
        side_1 = int_only("What value is your rectangles first side? ",
                          "Your response may only be a number")
        side_2 = int_only("What value is your rectangles second side? ",
                          "Your response may only be a number")
        print("Your rectangles side 1 is equal to {}\n"
              "Your rectangles side 2 is equal to {}".format(side_1, side_2))

        if shape == "parallelogram":
            side_1 = int_only("What value is your parallelograms first side? ",
                              "Your response may only be a number")
            side_2 = int_only("What value is your parallelograms second side? ",
                              "Your response may only be a number")
            print("Your parallelograms side 1 is equal to {}\n"
                  "Your parallelograms side 2 is equal to {}".format(side_1, side_2))

    if shape == "half_circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")
        print("Your half circles radius is equal to {}".format(radius))


# Main routine
user_shape = string_checker("What is your chosen shape? ")
dimensions = shape_dimensions(user_shape)

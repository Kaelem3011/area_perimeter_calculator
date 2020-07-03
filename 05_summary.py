

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
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Your response may only be equal to one of the given options")


# main routine
keep_going = ""
while keep_going == "":

    shapes_list = ["circle", "square", "rectangle", "triangle"]
    a_p_list = ["area", "perimeter", "both"]
    user_shape = string_checker("What is your chosen shape? ", shapes_list)

    if user_shape == "square":
        side_1 = int_only("What value is one of your squares sides? ",
                          "Your response may only be a number")

        print("Your squares area is {}".format(float(side_1 * side_1)))
        print("Your squares perimeter is {}".format(float(side_1 * 4)))

    if user_shape == "circle":
        radius = int_only("What value is your circles radius? ",
                          "Your response may only be a number")

        print("Your circles area is {}".format(float(3.14 * radius * radius)))
        print("Your circles perimeter is {}".format(float(3.14 * radius * radius)))

    if user_shape == "rectangle":
        side_1 = int_only("What value is your rectangles first side? ",
                          "Your response may only be a number")
        side_2 = int_only("What value is your rectangles second side? ",
                          "Your response may only be a number")

        print("Your rectangles area is {}".format(float(side_1 * side_2)))
        print("Your rectangles perimeter is {}".format(float(side_1 * 2 + side_2 * 2)))

    if user_shape == "triangle":
        print("Make sure that your response is area(a), perimeter(p), or both(b)")
        a_p = string_checker("are you trying to look for your triangles area, perimeter or both? ", a_p_list)

        if a_p == "area":
            base = int_only("what is your triangles base? ",
                            "Your response may only be a number")
            height = int_only("what is your triangles height? ",
                              "Your response may only be a number")

            print("Your triangles area is {}".format(float(0.5 * base * height)))

        elif a_p == "perimeter":
            base = int_only("what is your triangles base? ",
                            "Your response may only be a number")
            side_1 = int_only("what is your triangles first other side? ",
                              "Your response may only be a number")
            side_2 = int_only("what is your triangles second other side? ",
                              "Your response may only be a number")

            print("Your triangles perimeter is {}".format(float(base + side_1 + side_2)))

        elif a_p == "both":
            base = int_only("what is your triangles base? ",
                            "Your response may only be a number")
            height = int_only("what is your triangles height? ",
                              "Your response may only be a number")
            side_1 = int_only("what is your triangles first other side? ",
                              "Your response may only be a number")
            side_2 = int_only("what is your triangles second other side? ",
                              "Your response may only be a number")

            print("Your triangles area is {}".format(float(0.5 * base * height)))
            print("Your triangles perimeter is {}".format(float(base + side_1 + side_2)))

    keep_going = input("press <enter> to repeat the programme or any key to quit")

print("")




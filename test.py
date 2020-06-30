def int_operator(question, low=None, high=None):

    # sets up an error message
    if low is None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
        print()
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
        print()
    else:
        error = "\n" \
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n" \
                "Please make sure that you enter a number between 1 and 4 when choosing a shape \n" \
                "make sure your chosen dimensions are numbers \n" \
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" \
                "\n"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

PI = 3.14

print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print()

print("This programme calculates your chosen shapes area\n"
      "Follow the instructions to get through without errors")

print()
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print()

keep_going = ""
while keep_going == "":

    shape = int_operator("What is your shape? enter 1 for square, enter 2 for rectangle, enter 3 for circle, enter 4 "
                         "for triangle ", 1, 4)

    print()
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print()

    if shape == 1:
        base = int_operator("what is your squares base? ")

        height = int_operator("what is your squares height? ")

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Your squares area is {}".format(int(base) * (int(height))))
        print("Your squares perimeter is {}".format(int(base) + int(height)))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    if shape == 2:
        base = int_operator("what is your rectangles base? ")

        height = int_operator("what is your rectangles height? ")

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Your rectangles area is {}".format(int(base) * int(height)))
        print("Your rectangles perimeter is {}".format(int(base) + int(height)))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    if shape == 3:
        radius = int_operator("what is your circles radius? ")

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Your circles area is {}".format(PI * int(radius) * int(radius)))
        print("Your circles perimeter is {}".format(int(2) * PI * int(radius)))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    if shape == 4:
        base = int_operator("what is your triangles base? ")

        height = int_operator("what is your triangles height? ")

        length1 = int_operator("what is your triangles 1st length? ")

        length2 = int_operator("what is your triangles 2nd length? ")

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Your triangles area is {}".format(int(0.5) * int(base) * int(height)))
        print("Your triangles perimeter is {}".format(int(base) + int(length1) + int(length2)))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    else:
        print()
        keep_going = input("press <enter> to repeat the programme or any key to quit")
        print()
        print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
        print()
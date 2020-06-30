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
shapes_list = ["circle", "square", "rectangle", "triangle"]

user_shape = string_checker("What is your chosen shape? ", shapes_list)

dimension_1 = int_only("What is your shapes first dimension? ",
                       "Your response may only be a number")

dimension_2 = int_only("What is your shapes second dimension? ",
                       "Your response may only be a number")


# all print statements
print()
print("Your chosen shape is a {}".format(user_shape))
print("Your shapes first dimension is {}".format(dimension_1))
print("Your shapes second dimension is {}".format(dimension_2))
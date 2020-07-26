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
# list of valid shapes for component
shapes_list = ["circle", "square", "rectangle", "triangle"]
# user shape type input
user_shape = string_checker("What is your chosen shape? ", shapes_list)

print()
# users chosen shape input
print("Your chosen shape is a {}".format(user_shape))
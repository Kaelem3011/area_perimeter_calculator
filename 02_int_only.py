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

# main routine
dimension_1 = int_only("What is your shapes first dimension? ",
                       "Your response may only be a number")

dimension_2 = int_only("What is your shapes second dimension? ",
                       "Your response may only be a number")

print("Your shapes first dimension is {}".format(dimension_1))
print("Your shapes second dimension is {}".format(dimension_2))


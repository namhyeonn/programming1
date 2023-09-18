def get_integer_input():
    user_input = input("Enter integers separated by spaces (type 'done' to exit): ").split()

    if user_input[0].lower() == 'done':
        print("Program terminated. Goodbye!")
        exit()

    integers = []
    for item in user_input:
        try:
            integer = int(item)
            integers.append(integer)
        except ValueError:
            print("Must enter integers separated by spaces.")
            return get_integer_input()

    if len(integers) < 2:
        print("Must enter more than one integer.")
        return get_integer_input()

    return integers

def calculate_sum(integers):
    if len(integers) == 1:
        return integers[0]
    else:
        return integers[0] + calculate_sum(integers[1:])

if __name__ == '__main__':
    while True:
        input_integers = get_integer_input()
        result = calculate_sum(input_integers)
        print("The sum of the input integers is ==> {}".format(result))

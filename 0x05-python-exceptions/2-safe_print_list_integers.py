#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        for _ in range(x):
            value = next(iterator)
            if type(value) == int:
                print("{:d}".format(value), end="")
                count += 1
        print()
        return count
    except StopIteration:
        print()
        return count

# Uncomment the following lines to test the function
# my_list = [1, 2, 3, 4, 5]
# nb_print = safe_print_list_integers(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
#
# my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
# nb_print = safe_print_list_integers(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
#
# nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))

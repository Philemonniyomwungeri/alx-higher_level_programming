#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Uncomment the following lines to test the function
# value = 89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = -89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

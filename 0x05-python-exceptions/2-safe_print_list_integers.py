#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    i = 0

    while printed_count < x:
        try:
            item = my_list[i]
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                printed_count += 1
        except IndexError:
            break
        i += 1

    print()
    return printed_count

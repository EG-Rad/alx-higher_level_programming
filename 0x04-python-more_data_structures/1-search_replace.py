#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list by iterating through the input list
    new_list = [replace if item == search else item for item in my_list]
    return new_list

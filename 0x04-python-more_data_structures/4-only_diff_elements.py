#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric_difference method to find elements
    # that are in one set but not in both
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set

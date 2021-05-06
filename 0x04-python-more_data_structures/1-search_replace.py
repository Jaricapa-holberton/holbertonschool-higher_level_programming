#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = list(map(lambda x: replace if x == search else x, my_list))
    return list2

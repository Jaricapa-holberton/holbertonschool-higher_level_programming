#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for n in range(list_length):
        result = 0
        try:
            result = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            list_result.append(result)
    return (list_result)

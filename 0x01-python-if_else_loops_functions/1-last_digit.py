#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
""" check the minimal settings """
if number < 0:
    last_number = (abs(number) % 10) * -1
else:
    last_number = number % 10
print("Last digit of {} is {} and is".format(number, last_number), end=" ")
""" check the what digit is the last number """
if (last_number > 5):
    print("and is greater than 5")
elif (last_number < 6 and last_number != 0):
    print("and is less than 6 and not 0")
else:
    print("and is 0")

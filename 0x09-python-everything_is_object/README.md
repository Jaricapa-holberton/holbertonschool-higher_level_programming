# 0x09. Python - Everything is object

### Content:

0. Who am I?
What function would you use to print the type of an object?
1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
2. Right count
a = 89 and b = 100 point to the same object?
3. Right count =
a = 89 and b = 89 point to the same object?
4. Right count =
a = 89 and b = a point to the same object?
5. Right count =+
a = 89 and b = a + 1 point to the same object?
6. Is equal
If s1 = s2, what do print s1 == s2?
7. Is the same
If s1 = s2, what do print s1 is s2?
8. Is really equal
If s1 = "C" and s2 = "C", what do print s1 == s2?
9. Is really the same
If s1 = "C" and s2 = "C", what do print s1 is s2?
10. And with a list, is it equal
If l1 = [1] and l2 = [1], what do print l1 == l2?
11. And with a list, is it the same
If l1 = [1] and l2 = [1], what do print l1 is l2?
12. And with a list, is it really equal
If l1 = [1] and l2 = l1, what do print l1 == l2?
13. And with a list, is it really the same
If l1 = [1] and l2 = l1, what do print l1 is l2?
14. List append
If l1 = [1, 2, 3] and l2 = l1, and l1.append(2), what do print l2??
15. List add
If l1 = [1, 2, 3] and l2 = l1, and l1 = l1 + [2], what do print l2??
16. Integer incrementation
If a = 1 and increment(a), what print a?
def incremente(n):
    n += 1
17. List incrementation
If l = [1, 2, 3, 4] and increment(l), what print l?
def incremente(n):
    n.append(4)
18. List assignation
If l1 = [1, 2, 3, 4] and l2 = [4, 5, 6] and assign_value(l1, l2), wat do print l1?
def incremente(n):
    n.append(4)
19. Copy a list object
A function def copy_list(l): that returns a copy of a list.
20. Tuple or not?
If a = (), a is a tuple?
21. Tuple or not?
If a = (1, 2), a is a tuple?
22. Tuple or not?
If a = (1), a is tuple?
23. Tuple or not?
If a = (1, ), a is tuple?
24. Who I am?
If a = (1) and b = (1), what do print a is b?
25. Tuple or not
If a = (1, 2) and b = (1, 2), what do print a is b?
26. Empty is not empty
If a = () and b = (), what do print a is b?
27. Still the same?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
28. Same or not?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
30. #pythonic
A function magic_string() that returns a string “Holberton” n times the number of the iteration.
31. Low memory cost
A class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
32. int 1/3
a = 1
b = 1
line1: How many int objects are created by the execution of the first line of the script?
line2: How many int objects are created by the execution of the second line of the script?
33. int 2/3
a = 1024
b = 1024
del a
del b
c = 1024
line1: How many int objects are created by the execution of the first line of the script?
line2: How many int objects are created by the execution of the second line of the script?
line3: After the execution of line 3, is the int object pointed by a deleted?
line4: After the execution of line 4, is the int object pointed by b deleted?
line5: How many int objects are created by the execution of the last line of the script?
-->

34. int 3/3
print("I")
print("Love")
print("Python")
line1: Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory?
35. Clear strings
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
line1: How many string objects are created by the execution of the first line of the script?
line2: How many string objects are created by the execution of the second line of the script
line3: After the execution of line 3, is the string object pointed by a deleted?
line4: After the execution of line 4, is the string object pointed by b deleted?
line5: How many string objects are created by the execution of the last line of the script?

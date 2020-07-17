'''
TODO Complete this file by following the instructions in the lab exercise.
'''

integers = [1, 2, 3, 4, 5]

integers.append(6)

print(sum(integers))

sum = 0;
for i in integers:
    sum += i
print(sum)


# print(sum(integers))
# Traceback (most recent call last):
#  File "integers.py", line 17, in <module>
#    print(sum(integers))
# TypeError: 'int' object is not callable


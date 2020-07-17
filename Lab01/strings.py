'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']
x = ""

for i in strings:
	x += i  + " "

print(x[:-1])

print(' '.join(strings))

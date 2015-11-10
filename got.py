import collections as c
num = int(raw_input('Number: >  '))
path = c.OrderedDict()
while num != 1:
	if num % 3 == 0:
		path[num] = 3
		num /= 3
	elif num % 3 == 2:
		a = num + 1
		b = num - 2
		if (a / 3) % 3 == 0:
			path[num] = 1
			num = a
		elif (b / 3) % 3 == 0:
			path[num] = -2
			num = b
		else:
			path[num] = -2
			num = b
	else:
		a = num + 2
		b = num - 1
		if (a/3) % 3 == 0:
			path[num] = 2
			num = a
		elif (b/3) % 3 == 0:
			path[num] = -1
			num = b
		else:
			path[num] = -1
			num = b
for key, val in path.items():
	print '[%d, %d]' % (key, val)
#Pares desde el 20 hasta 60
n = 20
h = ''
while n <= 60:
	if n % 2 == 0:
		h += ' %i' % n
	n += 1
print(h)

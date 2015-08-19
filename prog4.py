#Numeros impares desde el 100 hasta el 1 e indicar la suma de estos
n = 100
h = ''
m = 0
while n >= 1:
	if n%2 != 0:
		h += ' %i' % n
	m += n
	n -= 1		
print (h,'\nSu suma es ',m) 

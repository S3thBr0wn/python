'''
Quadratic equation root calculator
'''
def roots(a, b, c):
	D = (b*b - 4*a*c)**0.5
	x_1 = (-b + D)/(2*a)
	x_2 = (-b - D)/(2*a)
	
	print ('x1: {0}'.format(x_1))
	print ('x2: {0}'.format(x_2))
	
if __name__ == '__main__':
	a = input('Enter a: ')
	b = input('Enter b: ')
	c = input('Enter c: ')
	roots(float(a), float(b), float(c))

'''
console output
seth@sSeth:~/python$ python quadratics.py
Enter a: 5
Enter b: 1
Enter c: 3
x1: (-0.09999999999999995+0.7681145747868607j)
x2: (-0.10000000000000005-0.7681145747868607j)

'''

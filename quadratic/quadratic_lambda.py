def quadtratic_function(a,b,c):
	return lambda x: a*(x**2) + b*x + c
	
a1 = quadtratic_function(1,2,1)
print(a1(1))
print("Input a,c and c from a quadratic equation in the form of ")
print("x = ax^2 + bx + c")
a = input("Input a ")
b = input("Input b ")
c = input("Input c ")
x = input("Input x ")
a2 = quadtratic_function(a,b,c)
fx = a2(1)
print("f(x) = ",fx)

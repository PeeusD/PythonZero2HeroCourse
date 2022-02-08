
''' Day 6 Assignment -
 WAP for Floor divison  using Decorators.'''

# This is actual wrapper function.....
def mydeco(myfunc):
	def myres(n1, n2):
		if n1 < n2 :
			n1, n2 = n2, n1
		return myfunc(n1, n2)
	return myres

# this is decorator definition	
@mydeco
def innerfunc_div(a, b):
	return  a // b
# writing all conditions on single line using conceopt of List Comprehension
a, b = (int(i) for i in input("Enter two Nunbers: ").split())

# Printing by calling inner function and passing args
print(innerfunc_div(a, b))

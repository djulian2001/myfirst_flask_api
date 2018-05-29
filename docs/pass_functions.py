# pass_functions


def methodception(another):
	return another()


def add_two_numbers():
	return 35+77

print(methodception(add_two_numbers))


print(methodception(lambda: 35 + 77))



# functional equivilent
print((lambda x: x * 3)(5))

def f(x):
	return x * 3

print(f(5))

# lets make a functional program to remove all even numbers
my_list = [1, 4, 12, 55, 13, 21, 223, 5, 5134, 9, 8, 7]
print( 
	my_list
)
# using the filter technique with a lambda function
print(list(filter(lambda x: x%2 != 0, my_list)))
# using with list comprehension
print([x for x in my_list if x%2 != 0 ])

# a method and for loop
def odd(x):
	if x%2 != 0:
		return True
odds=[]
for x in my_list:
	if odd(x):
		odds.append(x)
print(odds)
# just the for loop
odds=[]
for x in my_list:
	if x%2 != 0:
		odds.append(x)
print(odds)
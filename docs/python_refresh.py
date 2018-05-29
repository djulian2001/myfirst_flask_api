# variables
a = 5
b = 10
my_variable = 56

string_variable = "hello"

print(my_variable)


def my_print(arg1):
	print(arg1)

def my_method_times(arg1, arg2):
	return arg1 * arg2

my_print(my_method_times(2,4))


# lists
grades = [58,33,46,20,66,34,99]
tuple_grades = (100,34)



print(len(grades))
print(sum(grades))
print(sum(grades)/len(grades))

# tuples


# sets
my_set={213,334,1,2,1}
my_other_set={334,1,2,115,323}
my_print(my_set.intersection(my_other_set))
my_print(my_set.union(my_other_set))

my_print({2,3,5,1,44}.difference(my_other_set))

if arg1 < 23:
	pass
elif arg1 > 34:
	pass
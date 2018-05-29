# decorators

# a decorator is a function that gets called before another function.
# here is a template for a decorator without arguments

import functools

def my_decorator(func_this):
	@functools.wraps(func_this)
	def function_that_runs_func_this():
		print("In the decorator!")
		func_this()  # this has to be here else my_function will not run.
		print("Should be after function")

	return function_that_runs_func_this


@my_decorator
def my_function():
	print("I'm the function!")

my_function()


# a more advanced look at decorators
# template with arguments
# lets pass args to the decorators
def decorator_with_args(a_number):
	def my_decorator(func):
		@functools.wraps(func)
		def function_that_runs_func(*args, **kwargs):
			print("decorator function running!")
			if a_number != 56:
				func(*args, **kwargs)
			else:
				print("Condition fails to run function!!!")
			print("decorator post func run!")
		return function_that_runs_func
	return my_decorator

@decorator_with_args(56)
def my_function_too(x, y):
	print("hello from my_function_too...")
	print(x,y)

my_function_too(1,"abc")

@decorator_with_args(55)
def my_function_too(a, b, c):
	print("hello from my_function_too...")
	print(a,b,c)

my_function_too(c='bde',a=2,b=['my','list'])

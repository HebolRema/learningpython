#return a function as a value
'''def greeting(name):
	def hello():
		return 'Hello' '+name+'!
	return hello
greet=greeting('Hebol')
print(greet())'''
'''def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner
def ordinary():
	print('I am ordinary')
# decorate ordinary function
decorated_func=make_pretty(ordinary)
decorated_func()'''
def my_decorator(func):
	def wrap_func():
		func()
	return wrap_func
@my_decorator
def hello():
	print('helloooo')
hello()
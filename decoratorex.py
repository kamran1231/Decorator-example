
#Function returning fuction (closure) practice:

# def to_power(x):
#     def cal_power(n):
#         return n**x
#     return cal_power
#
# cube = to_power(3)
# print(cube(4))


#---------------------Decorator part 1-------------------------------

# Decorator - enhance  the functionality of other functions
#
# def decorator(f):
#     def wrapper_func():
#         print('this is awesome function')
#         f()
#     return wrapper_func
#
#
#
# def func1():
#     print('hello func1')
#
#
# def func2():
#     print('hello func2')

# var = decorator(func1)
# var()

# Output - this is awesome function
# hello func1

#----second method we can also acces this function with the use of @decorator

# @decorator
# def func3():
#     print('hello func3')
#
# func3()

# Output - this is awesome function
# hello func3

# def decorator_func(any_func):
#     def wrapper_func():
#         print('this is awesome function')
#         any_func()
#     return wrapper_func
#
# @decorator_func
# def func1():
#     print('hello func1')
# func1()
#
# @decorator_func
# def func2():
#     print('hello func2')
#
# func2()

# Output - this is awesome function
# hello func1
# this is awesome function
# hello func2

#-----------------Decorator part 2-------------------

# def decorator_func(any_func):
#     def wrapper_func(*args,**kwargs):
#         print('this is awesome function')
#         return any_func(*args,**kwargs)
#     return wrapper_func
#
# @decorator_func
# def fuc1(a):
#     print(f'this is function with argument {a}')
#
# fuc1(5)

# Output - this is awesome function
# this is function with argument 5

# @decorator_func
# def add(a,b):
#     return a + b
#
# print(add(5,5))

# Output - this is awesome function
# this is function with argument 5
# this is awesome function
# 10


#-----------------Decorator part 3--------------------

# from functools import wraps
# def decorator_func(any_func):
#     @wraps(any_func)
#     def wrapper_func(*args,**kwargs):
#         '''this is wrapper function'''
#         print('This is awesome function')
#         return any_func(*args,*kwargs)
#     return wrapper_func
#
# @decorator_func
# def func1():
#     '''hi kamran where are you'''
#     return 'hi func1 how are you'
#
#
# print(func1.__doc__)
# print(func1.__name__)

# Output - hi kamran where are you
# func1

#----------Practice Decorator-----------

# from functools import wraps
# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapped_func(*args,**kwargs):
#         print(f'you are calling {wrapped_func.__name__} function')
#         print(f'{any_function.__doc__}')
#         return any_function(*args,**kwargs)
#     return wrapped_func
#
# @print_function_data
# def add(a,b):
#     '''this function takes two numbers as arguments and return there sum'''
#     return a + b
# print(add(4,5))

# Output - you are calling add function
# this function takes two numbers as arguments and return there sum
# 9

#----------Decorator Excercise------------

# import time
#
# def calculate_time(any_func):
#     def wrap_func(*args,**kwargs):
#         t1 = time.time()
#         returned_value = any_func(*args,**kwargs)
#         t2 = time.time()
#         total_time = t2-t1
#         print(f'this program took {total_time}')
#         return returned_value
#     return wrap_func
#
# @calculate_time
# def square_finder(n):
#     return [i**2 for i in range(1,n+1)]
#
# square_finder(1000000)

# Output - this program took 0.6999900341033936
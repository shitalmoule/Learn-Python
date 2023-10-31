#Decorator
# def my_decorator(func):
#     def wrap_func():
#         print('---------')
#         func()
#         print('---------')
#     return wrap_func

# @my_decorator
# def hello():
#     print('Hello')

# hello()
# new_hello = my_decorator(hello)
# new_hello()

# def my_decorator(func):
#     def wrap_func(a, b):
#         print("********")
#         func(a, b)
#         print("********")
#     return wrap_func

# @my_decorator
# def hello(greet, emoji):
#     print(greet, emoji)
# hello('Good Morning', ':)')


# by using *args, **kwargs
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print("********")
#         func(*args, **kwargs)
#         print("********")
#     return wrap_func

# # @my_decorator
# def hello(greet, emoji):
#     print(greet, emoji)
# hello_morn = my_decorator(hello)
# print(hello_morn('Good Morning', ':)'))


#Authenticated
# user_One = {
#     'name':'Shital',
#     'valid':True   
# }

# def authenticated(func):
#     def wrap(user):
#         if user['valid'] is True:
#             print("User Validated")
#             # return func(user)
#         else:
#             print("Invalid User")
#     return wrap

# @authenticated
# def my_user(user):
#     print("User Authentication Done!!")
# my_user(user_One)
#1
# def generator_function(num):
#     for i in range(num):
#         yield i*2

# for item in generator_function(12):
#     print(item)

#2
# def generator_function(num):
#     for i in range(num):
#         yield i*2

# g = generator_function(10)
# print(next(g))

# 3
# def gen_fun(num):
#     for i in range(num):
#         yield i

# for item in gen_fun(100):
#     print(item)

#4
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break

# print(special_for([1, 2, 3]))

# 6
# class MyGen():
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current +=1
#             return num
#         raise StopIteration
    
# gen = MyGen(0, 10)
# for i in gen:
#     print(i)

# 6
# def fib(num):
#     n1 = 0
#     n2 = 1
#     for i in range(10):
#         yield n1
#         temp = n1
#         n1 = n2
#         n2 = temp + n2
    
# for x in fib(10):
#     print(x)


# 7(Without using Generators)
# def fib(num):
#     n1 = 0
#     n2 = 1
#     result = []
#     for i in range(num):
#         result.append(n1)
#         temp = n1
#         n1 = n2
#         n2 = temp + n2
#     return result
    
# print(fib(10))

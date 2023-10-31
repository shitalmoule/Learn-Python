# import re

# string = 'search inside of this text please!'
# a = re.search('thIs', string)
# print(a.group())

# pattern = re.compile('search')
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(d)

# print('search' in string)


# 2 Gmail
# import re
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'shital@gmail.com'
# a = pattern.search(string)
# print(a)

# 3
# import re

# pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d" )
# string = "Shital@342"
# a = pattern.search(string)
# print(a)

# 4 Password Validation(End with a number)
import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}[0-9]")
string = "Shital@376"
a = pattern.search(string)
print(a)
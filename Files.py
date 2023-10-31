try:
    with open("Test.txt", mode='x') as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print("file doen't exists")
    raise err
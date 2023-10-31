class SuperList(list):
    def __len__(self):
        return 100

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
super_list1.append(10)
super_list1.append(20)
print(super_list1[2])
print(issubclass(SuperList, list))
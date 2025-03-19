list1 = []

list1.append("Gabriela")
list1.append("Steven")
list1.append("Keneth")
list1.append(130)
list1.append(True)
print(type(list1))
print(list1)

list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2)

list3 = list(range(1,21))
print(list3)

list4 = list()
list4.append(1)
list4.append(list1)
list4.append(list3)
print(list4)

tam = len(list4)
print(tam)
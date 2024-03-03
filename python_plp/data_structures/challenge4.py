list1 = input("enter first set1: ") 
list1=[int(x) for x in list1.split(',')]
list2 = input("enter second set1: ") 
list2=[int(x) for x in list2.split(',')]
set1 = set(list1)
set2 = set(list2)

print("the common values in the set1s are:",set1.intersection(set2))

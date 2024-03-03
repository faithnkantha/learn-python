list_a =[1,2,3,4,5]
print(list_a)
print(list_a[4])
list_a[0]=10
print(list_a)
print(len(list_a))
list_a.append(7)
list_a.insert(len(list_a),6)
list_a.extend([8,9]) #takes only one arguement
list_a.pop(8)
del list_a[7]
for item in list_a:
 print(item)
 '''other functions
 remove()
 clear()
 index()
 count()
 sort()
 reverse()
 copy()
 '''


list_b = [ 3.4,1, "John",True]

list_c = ["Arthur","Purity","Nkatha"]

list_d = [1,2,3,[4,5,6],7,8,9]
#make a list with increasing power of 2
numbers = [number*number for number in range(1,6)]
print(numbers)

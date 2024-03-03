number = input("enter a number: ") 
number=[int(x) for x in number.split(',')]
total=0
for num in number:
    total +=num
print("the sum is" ,total)
print(number)

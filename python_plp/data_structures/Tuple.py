#tuples can have any number of items of different data types
var1 = "hello" # spot the difference
print(type(var1))
var2 = "hello",
print(type(var2))
var3 = ("hello",)
print(type(var3))

letters = ("p","p","j","k","r","d","g","b","o",)
print(letters[0])
print(letters[4])
#negative indexing
print(letters[-1])
print(letters[-3])
#tuple methods
print(letters.count('p'))
print(letters.index('o'))

'''set can not have duplicate values(unique data)
A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
Sets are mutable. However, since they are unordered, indexing has no meaning
We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.


'''
empty_set = set()
numbers = {2,4,2,6,7,8}
print(numbers)
numbers.add(32)
print(numbers)
# update
companies={"safaricom","equity","consolidated"}
tech_companies = ["Microsoft","apple","amazon"]
companies.update(tech_companies)
print(companies)
companies.discard("Microsoft")
print(companies)
#iterate
for company in companies:
    print(company)
'''
union()
intersection()
difference()
symmetric_difference()

all()
any()
enumerate()
len()
max()
min()
sorted()
sum()

'''
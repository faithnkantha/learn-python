'''
dict is an ordered collection of items
its stores value in key/value pairs
keys are identifiers to each values
We can have keys and values of different data types.
'''
Women_governors ={"Meru":"Kawira Mwangaza","Homabay":"Gladys wanga","Nakuru":"susan Kihika"}
print(Women_governors)
Women_governors["Embu"]="cecily mutitu mbarire"
print(Women_governors)
Women_governors["Embu"] = "cecily mutitu"
print(Women_governors)
print(Women_governors["Embu"])
del Women_governors["Nakuru"]
print(Women_governors)
#Membership test-test if keys in dict is using keywords or not
print("Meru" in Women_governors)
print("Nakuru" in Women_governors)
# iterations through dict
for i in Women_governors:
    print(Women_governors[i])


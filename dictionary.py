cabinet = {3:"A", 5:"B"}
print(cabinet[3])
print(cabinet[5])

print(cabinet.get(5))

print(cabinet.get(1))
print(cabinet.get(1, "useable"))

print(3 in cabinet)  #True

cabinet = {"A-3" :"김성인", " C-20": "John"}
print(cabinet["A-3"])

#Add dic
cabinet["D-1"] = "kevin"
print(cabinet)

#Erase cabinet
del cabinet["A-3"]
print(cabinet)

#print Key
print(cabinet.keys())

#print value
print(cabinet.values())

#print ALL
print(cabinet.items())

cabinet.clear()
print(cabinet)
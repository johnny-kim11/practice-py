#set
#does not accept overlap
#do not think about order
my_set = {1,2,3,3,3}
print(my_set)

java = {"a","b", "c","k"}
python = set(["a", "b", "c", "d", "e"])

#and
print(java & python)
print(java.intersection(python))

#or
print(java | python)
print(java.union(python))

#cha 
print(java - python)
print(java.difference(python))

#add people
python.add("x")
print(python)

#delete people
java.remove("a")
print(java)
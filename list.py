subway = [10, 20, 30]
print(subway)

subway = ["a", "b", "c"]
print(subway)

#where is b?
print(subway.index("b"))

#"d" rode from next station
subway.append("d")
print(subway)


#insert "k"
subway.insert(1, "k")
print(subway)
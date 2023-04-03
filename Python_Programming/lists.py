import pdb

countries = ["USA", "Mexico", "Canada", "India", "Germany", "Japan"]
print(countries)
print(type(countries))
print(len(countries))
pdb.set_trace()
countries.append("china")
print(countries)
countries.remove("Canada")
print(countries)


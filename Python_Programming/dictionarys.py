capitals = {"USA": "Washington", "France": "Paris", "Turkey": "Ankara"}
print(type(capitals))

france_capital = capitals["France"]
print(france_capital)
france_capital2 = capitals.get("France")
print(france_capital2)
all_keys = capitals.keys()
all_values = capitals.values()
print(all_keys)
print(all_values)

employee = {
    "name": "Al-Amin",
    "age": "28",
    "phone": "01629674872",
    "skills": ["AWS", "Python", "Java", "Docker"]
}
e_name = employee['name']
e_age = employee['age']
e_skills = employee['skills']
print(type(e_skills))
user_skill_count = len(e_skills)
print(f"user has {user_skill_count} skills")
print("User has {} skills ".format(user_skill_count))

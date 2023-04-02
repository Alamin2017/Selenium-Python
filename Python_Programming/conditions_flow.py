a = 1
b = 3
if a < b:
    print("a is less than b")
else:
    print("N\A")

shows = ["Friends", "The Office", "Breaking Bad", "Stranger Things"]
movies = ["Rocky", "Batman", ""]
my_choice = "The Office"
if my_choice in shows:
    print("Your choice is a show")
elif my_choice in movies:
    print("Your choice is a movie")
else:
    print("Your choice is unknown")

theater_name = "XYZ"
age_limit = 17
print(f"Welcome to {theater_name} theaters!!!")
user_input = input("Enter your age:")
print(f"User input is :{user_input}")

if int(user_input) >= age_limit:
    print("Enjoy the movie")
else:
    adult_present = input("Is another adult with you ? Yes sor No:")
    if adult_present == "yes":
        print("Enjoy the movie")
    else:
        print("You must be 17 to watch the movie")

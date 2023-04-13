my_list = ['house', 'car', 'bike', 'boat']
for i in my_list:
    print(i)
    print('-------')

quote = "Give a man a program, frustrate him for a day. Teach a man to program ,frustrate him for a lifetime."
words_list = quote.split()
print(words_list)
for i in words_list:
    if len(i) <= 3:
        print(i)
    else:
        pass

for i in range(5):
    print(i)
print("Again Loop")
for i in range(2, 5):
    print(i)

my_list = []
for i in range(10):
    my_list.append('abc')
print(my_list)
print(len(my_list))

counter = 1
while counter < 10:
    print(counter)
    counter = counter + 1

main_number = 8
user_input = 0
while user_input != main_number:
    user_input = input("Enter a number 0 to 10: ")
    user_input=int(user_input)

    print(f"You entered:{user_input}")
print("Done")

main_number = 15
while True:
    user_input = input("Enter a number 0 to 20: ")
    print(f"You entered:{user_input}")
    if int(user_input) == main_number:
        break

print("Done")

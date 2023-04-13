my_string = "I love to program in python Languages"
my_f = open('sample_output.txt', 'w')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.close()
with open('programming_file_output.txt', 'w') as my_f:
    my_f.write(my_string)

my_l = ['user1', 'user2', 'user3', 'user4']
with open('sample_output3.txt', 'w') as my_f:
    for i in my_l:
        my_f.write(i + '\n')

my_langs = ['Python', 'Java', 'PHP', 'Ruby']
with open('sample_output3.csv', 'w') as my_f:
    for i in my_langs:
        my_f.write(i + '\n')


import random
import string

list_of_domains = ['superqa.com', 'gmail.com', 'yahoo.com']

length_of_email = 10
letters = string.ascii_lowercase

all_emails = []

for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        email = f"{random_string}@{domain}"
        all_emails.append(email)
        print(email)

print(all_emails)

with open('output_file_csv.csv', 'w') as f:
    f.write(',\n'.join(all_emails))

with open('output_file_csv.csv', 'r') as fa:
    emails_raw = fa.readlines()
    print(emails_raw)

import pdb

import pdb

sample_file = 'programming_file_input.txt'
my_file = open(sample_file, 'r')
content = my_file.read()
print(content)

my_content_list = content.split('\n')
print(my_content_list)
my_file = open(sample_file, 'r')

content2 = my_file.readline()
print(content2)

my_file = open(sample_file, 'r')
content = my_file.read()
print(content)
print('-----')

with open(sample_file, 'r') as f:
    content = f.read()

print(content)

list_of_c = [i.strip() for i in content]
print(list_of_c)

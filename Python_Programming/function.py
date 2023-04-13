def my_adder(a, b):
    total = a + b
    return total


sum_a_b = my_adder(3, 4)
print(sum_a_b)


def has_no_sales_tax(state):
    states_with_no_sales_tax = ['AK', 'DE', 'MT', 'NH', 'OR']

    # no_tax = None
    if state in states_with_no_sales_tax:
        no_tax = True
        return no_tax
    else:
        no_tax = False
        return no_tax

    # return no_tax


user_state = 'AKa'

print(has_no_sales_tax(user_state))


def get_count_of_small_words(input_string, max_size=3):
    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)

    return len(small_words)


my_joke_1 = "In Python are used to."
num_small = get_count_of_small_words(my_joke_1)
print(num_small)

# %%

# TASK 1:
def add(x, y):
    return x + y


print(add(3, -4))


# %%

# TASK 2:
def count_string(string, letter):
    return string.lower().count(letter.lower())


print(count_string("HeLlO, mY nAmE iS MiKkEl!", "m"))


# %%
# TASK 3:

# a)

def isEven(i):
    return i % 2 == 0


print(isEven(7))


# b)

def isEvenList(listing):
    return len([x for x in listing if isEven(x)])


print(isEvenList([1, 2, 3, 4, 5, 6, 7, 8]))

# %%
# TASK 4:


def find_max(listing):
    current_max = listing[0]
    for element in listing:
        if element > current_max:
            current_max = element
    return current_max


print(find_max([1, 2, 3, 4, 136, 6, 7, 8]))


# %%

# TASK 5:

def print_word(word):
    while word:
        print(word)
        word = word[:-1]


# ALTERNATIVE RECURSIVE FUNCTION
def print_word_rec(word):
    if word:
        print(word)
        word = word[:-1]
        print_word_rec(word)


print_word("hello")
print_word_rec("hello")
# %%


# TASK 6:
def get_keys(dic):
    return list(dic.keys())


print(get_keys({"tommy": 2, "tim": 3}))

# %%

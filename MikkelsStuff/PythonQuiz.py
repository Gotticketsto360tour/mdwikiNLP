# %%

# TASK 1:
def add(x, y):
    return x + y


# %%

# TASK 2:
def count_string(string, letter):
    return string.lower().count(letter.lower())


# %%
# TASK 3:

# a)

def isEven(i):
    return i % 2 == 0


# b)

def isEvenList(listing):
    return len([x for x in listing if isEven(x)])


# %%
# TASK 4:

def find_max(listing):
    current_max = listing[0]
    for element in listing:
        if element > current_max:
            current_max = element
    return current_max


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


# %%

# TASK 6:
def get_keys(dic):
    return list(dic.keys())

# %%

word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]

# List comprehension to create a list of palindromes
print([word for word in word_list if word == word[::-1]])

# List comprehension to create a list of words with 'uu'
print([word for word in word_list if "UU" in word])

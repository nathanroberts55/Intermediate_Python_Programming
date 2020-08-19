import scrabble

# Go through the words in sowpods
# Find the value of the letters in each word
# Compare it to the value of the word with the highest point value

# Storage for the word with the most points and its value
most_points = 0
most_points_word = ""

for word in scrabble.word_set:
    word_value = 0
    for letter in word:
        word_value += scrabble.scores[letter]
    if word_value > most_points:
        most_points = word_value
        most_points_word = word

print("The word that gets the most points is:", most_points_word)
print("The value of the word is: %d points" % most_points)
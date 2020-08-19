import scrabble
import string

# Print all of the letters that do not appeared doubled

for letter in string.ascii_lowercase:
    found = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            found = True
            break
    if not found:
        print('There are no English words with a double ' + letter)

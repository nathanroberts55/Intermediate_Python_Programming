import scrabble

longest = ''
for word in scrabble.wordlist:
    if word ==  word[::-1] and len(word) > len(longest):
        longest = word

print(longest) 
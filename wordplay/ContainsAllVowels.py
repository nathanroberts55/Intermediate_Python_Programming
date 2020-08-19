import wordplay.scrabble

# Words that contains all vowels (a,e,i,o,u)

vowels = 'aeiou'

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
import sys
def solveSpellingBee(letters):
	from nltk.corpus import words
	allWords = words.words();
	requiredLetter = letters[0];
	for word in allWords:
		if(requiredLetter in word and (all(x in letters for x in word)) and len(word) >= 3):
			print(word)

solveSpellingBee(sys.argv[1])
def InputSentence():
    senInput = str(input("Enter a Sentence: "))
    text = senInput
    return text

def CountWords(text):
    countSpace = 0
    for space in text:
        if space == ' ':
            countSpace = countSpace + 1
            countWords = countSpace + 1
    if countSpace == 0:
        countWords = 1
    return countWords

def CountVowels(text):
    countVowels = 0
    for vowels in text:
        if vowels in "aeiouAEIOU":
            countVowels = countVowels + 1
    return countVowels

def CountConsonants(text):
    countConsonants = 0
    for consonants in text:
        if consonants in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            countConsonants = countConsonants + 1
    return countConsonants

def DisplayOutput(countWords, countVowels, countConsonants):
    print(f"\nNumber of Words: {countWords}")
    print(f"Number of Vowels: {countVowels}")
    print(f"Number of Consonants: {countConsonants}")

text = InputSentence()

countWords = CountWords(text)
countVowels = CountVowels(text)
countConsonants = CountConsonants(text)

DisplayOutput(countWords, countVowels, countConsonants)



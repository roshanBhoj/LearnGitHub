def isWhiteSpace(character):
    return character == ' ' or character == '\n'

def slice(sentence):
    words = []
    beginningOfWord = 0
    currentCharacter = 0
    for character in sentence:
        if isWhiteSpace(character):
            word = sentence[beginningOfWord:currentCharacter]
            words.append(word.lower())
            beginningOfWord = currentCharacter + 1
        elif currentCharacter == len(sentence) - 1:
            word = sentence[beginningOfWord:len(sentence)]
            words.append(word.lower())

        currentCharacter = currentCharacter + 1
    return words

def countWords(sentence):
    wordCount = {}
    words = slice(sentence)
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    print wordCount

countWords("Hello this is my sentence sentence is my word hello")

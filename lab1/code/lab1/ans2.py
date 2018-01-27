
"input from user"
sentence=input("Enter input sentence:")

"list of words"
words=sentence.split(" ")

'variable declaration'
maxLength=0
longestWord=""
wordsLen=len(words)
index=0
middleLengthIndex=0
reverseSentence=list()
middleWords=[]

"get middle index of middle words"
if wordsLen%2==0:
    middleLengths = [wordsLen//2-1, wordsLen//2]
else:
    middleLengths=[wordsLen//2]

"iterator for words"
for word in words:
    wordLen=len(word)

    "get max length word"
    if wordLen>maxLength:
        maxLength, longestWord = wordLen,word

    "get middle words"
    if len(middleLengths)>middleLengthIndex and index==middleLengths[middleLengthIndex]:
        middleWords.append(word)
        middleLengthIndex +=1
    word=word[::-1]
    reverseSentence.append(word)
    index += 1

"joining words"
reverseSentence=' '.join(reverseSentence)
middleWords=' '.join(middleWords)

"print answer"
print("Middle words:",middleWords)
print("Longest word:",longestWord)
print("Sentence with reverse words:",reverseSentence)
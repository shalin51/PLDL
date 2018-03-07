import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

import re
import urllib.request


with open("input.txt",'r') as f:
    content = f.read()

#Tokenization

from nltk.stem import WordNetLemmatizer
print("\n\n")
print("LEMMATIZATION")
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize(content))


frequencies = Counter([])
token = word_tokenize(content)
bigrams = ngrams(token, 2)
frequencies += Counter(bigrams)

topFiveBG=list()
for i in range (0,5) :
    topFiveBG.append(" ".join(re.findall("[a-zA-Z]+",str(frequencies).split(":")[i])))
print(frequencies)

print("top five words")
print(topFiveBG)

lines={}
for line in content.split("."):
    for word in topFiveBG:
        if word in line:
            if line in lines:
                pass
            else:
                lines[line]=""

result=list()
for line in lines:
    result.append(line+".")

print("Final Result")
print(result)
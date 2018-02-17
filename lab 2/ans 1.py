"input form user"
rng=input ("Enter range separated by space:")

'books dictionary'
bookDic={
    "python":40,
    "web development":50,
    "C":30,
    "java":70,
    "javascript":55,
    "R":75
}

'split to get start and end range'
rng=rng.split(" ")

'get dictionaries in specific range'
resultDic=dict((k,v) for k, v in bookDic.items() if  int(rng[0])<v<int(rng[1]))

'print result'
print("You can purchase following books:")
for book in resultDic:
    print(book,":",resultDic[book])


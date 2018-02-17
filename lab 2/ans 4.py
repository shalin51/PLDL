import numpy as np

'generate an array of int in range 1 to 20'
arr=np.random.randint(1,20,15,int)

'print array'
print("Generated Array:")
print(arr)
print("Most frequent number is")

'count most frequent number'
counts = np.bincount(arr)
print(np.argmax(counts))

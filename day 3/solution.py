import string

#open input file
inputFile = open('input.txt')    

#split every line into a string
itemList = inputFile.read().split()

alphabets = list(string.ascii_letters)

class myDictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

dictObj = myDictionary()

for i in range(len(alphabets)):
    dictObj.key = alphabets[i]
    dictObj.value = i+1
    dictObj.add(dictObj.key, dictObj.value)

count = 0
#define splices in order to divide the string into 2 equal parts and find the common char
for item in range(len(itemList)):
    string1 = slice(0, len(itemList[item])//2)
    string2 = slice(len(itemList[item])//2, len(itemList[item]))
    commonChar = ''.join(set(itemList[item][string1]).intersection(itemList[item][string2]))
    count = count + dictObj.get(commonChar)

print(count)
inputFile.close()
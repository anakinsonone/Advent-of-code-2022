import string
import itertools

#open input file
inputFile = open('input.txt')   

#create a list of alphabets
alphabets = list(string.ascii_letters)

#create dictionary
class myDictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

#create an object of the dictionary
dictObj = myDictionary()

#add priorities to each alphabet
for i in range(len(alphabets)):
    dictObj.key = alphabets[i]
    dictObj.value = i+1
    dictObj.add(dictObj.key, dictObj.value)

#split every line into a string
itemList = inputFile.read().split()

#part 1

#define splices to divide the string into 2 equal parts and find the common char
count = 0
for item in range(len(itemList)):
    string1 = slice(0, len(itemList[item])//2)
    string2 = slice(len(itemList[item])//2, len(itemList[item]))
    commonChar = ''.join(set(itemList[item][string1]).intersection(itemList[item][string2]))
    count = count + dictObj.get(commonChar)

print('Sum of all priorities:', count)

#part 2

#define a function to create groups of three
def grouper(n, iterable):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

groups = list(grouper(3, itemList))

badge = 0
#compare strings within each group and find the common item
for string in range(len(groups)):
    string1 = groups[string][0]
    string2 = groups[string][1]
    string3 = groups[string][2]
    commonItem = ''.join(set(string1).intersection(string2).intersection(string3))
    badge = badge + dictObj.get(commonItem)

print("Sum of common badge priorities:", badge)
inputFile.close()
#open the input file
inp = open('input.txt')

#convert inputs to a list of strings separated by double 'new-lines'
splitInp = inp.read().split("\n\n")

newList = []
for i in splitInp:
    newList.append(i.split('\n'))

sumList = []
for j in newList:
    sumList.append(sum(list(map(int, j))))

maxCalories = max(sumList)
print(maxCalories)

secSumList = set(sumList)

secSumList.remove(max(secSumList))
secondMax = max(secSumList)

thirdSumList = set(secSumList)

thirdSumList.remove(max(thirdSumList))
thirdMax = max(thirdSumList)

print("sum of top three: ", maxCalories + secondMax + thirdMax)
inp.close()
#open input file
inputFile = open('input.txt')

#read the file and split at new-line to determine the pairs
pairList = inputFile.read().split()

#new list to split up assigned sections for each elf
newList = []
for pair in range(len(pairList)):
    newList.append(pairList[pair].split(','))

count = 0
for i in range(len(newList)):
    #variables to determine the range
    p1e1 = int(newList[i][0].split('-')[0])
    p1e2 = int(newList[i][0].split('-')[1])
    p2e1 = int(newList[i][1].split('-')[0])
    p2e2 = int(newList[i][1].split('-')[1])

    #part 1
    if((p1e1 <= p2e1) and (p1e2 >= p2e2)):
        count = count + 1
    elif((p1e1 >= p2e1) and (p1e2 <= p2e2)):
        count = count + 1
    
    #part 2
    elif((p1e1 <= p2e1 and p2e1 <= p1e2 and p1e2 <= p2e2)):
        count = count + 1
    elif((p2e1 <= p1e1 and p1e1 <= p2e2 and p2e2 <= p1e2)):
        count = count + 1

print('number of subsets: ', count)
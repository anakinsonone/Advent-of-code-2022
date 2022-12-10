#read the input file
inputSignal = open('input.txt').read()

p1 = False
p2 = False
for i in range(len(inputSignal)):
    if (not p1) and i-3>=0 and len(set([inputSignal[i-j] for j in range(4)])) == 4:     #create sets of consecutive 4 chars and the first set with length 4 is the answer
        print(i + 1)
        p1 = True
    if (not p2) and i-13>=0 and len(set([inputSignal[i-j] for j in range(14)])) == 14:  #similar to part 1, instead of a set of 4 distict characters, check for the first set with 14 distinct characters
        print(i + 1)
        p2 = True

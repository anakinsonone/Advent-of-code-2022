# import re
#read the input file
inputSignal = open('input.txt').read()

charList = [inputSignal[i:i +4] for i in range(0, len(inputSignal), 4)]
# charList1 = re.findall('....?', inputSignal)

print(charList1 == charList)
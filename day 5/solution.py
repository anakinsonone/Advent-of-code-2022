movesInput = open('moves.txt')

moves = movesInput.read().strip();
cmd = [x.strip() for x in moves.split('\n')]

initStack = [
    [],
    ['W', 'L', 'S'],
    ['Q', 'N', 'T', 'J'],
    ['J', 'F', 'H', 'C', 'S'],
    ['B', 'G', 'N', 'W', 'M', 'R', 'T'],
    ['B', 'Q', 'H', 'D', 'S', 'L', 'R', 'T'],
    ['L', 'R', 'H', 'F', 'V', 'B', 'J', 'M'],
    ['M', 'J', 'N', 'R', 'W', 'D'],
    ['J', 'D', 'N', 'H', 'F', 'T', 'Z', 'B'],
    ['T', 'F', 'B', 'N', 'Q', 'L', 'H']
]

#part 1
for eachMove in cmd:    
    words = eachMove.split()                                            #split every move into a list
    qty_ = int(words[1])                                                #number of crates to be moved
    from_ = int(words[3])                                               #the stack 'from' which crates are to be moved
    to_ = int(words[5])                                                 #the stack 'to' which creates are to be moved                
    move = initStack[from_][:qty_]                                      #slice the number of crates according to the quantity
    initStack[from_] = initStack[from_][qty_:]                          #remove the crates from the 'from' stack
    initStack[to_] = list(reversed(move)) + initStack[to_]              #add the crates to the 'to' stack while reversed
print("part 1: ", ''.join([i[0] for i in initStack if len(i) > 0]))     #print the top-most element of the stack, from each stack

#part 2
for eachMove in cmd:
    words = eachMove.split()
    qty_ = int(words[1])
    from_ = int(words[3])
    to_ = int(words[5])
    move = initStack[from_][:qty_]
    initStack[from_] = initStack[from_][qty_:]
    initStack[to_] = move + initStack[to_]                              #same steps as above, but instead of reversing the crate, just add it as it is
print("part 2: ", ''.join([i[0] for i in initStack if len(i) > 0]))
movesInput.close()
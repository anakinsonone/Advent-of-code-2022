#A, X -> ROCK -> 1 point
#B, Y -> PAPER -> 2 points
#C, Z -> SCISSOR -> 3 points
#if win, result: value(move) + 6 else, result: value(move)

inp = open('input.txt')
splitRounds = inp.read().split("\n")
splitPlays = []
for i in splitRounds:
    splitPlays.append(i.split(" "))
# print(splitPlays)

count = 0

#PART 1
for j in splitPlays:
    if(j[0] == 'A' and j[1] == 'X'):
        count = count + 4
    elif(j[0] == 'A' and j[1] == 'Y'):
        count = count + 8
    elif(j[0] == 'A' and j[1] == 'Z'):
        count = count + 3
    elif(j[0] == 'B' and j[1] == 'X'):
        count = count + 1
    elif(j[0] == 'B' and j[1] == 'Y'):
        count = count + 5
    elif(j[0] == 'B' and j[1] == 'Z'):
        count = count + 9
    elif(j[0] == 'C' and j[1] == 'X'):
        count = count + 7
    elif(j[0] == 'C' and j[1] == 'Y'):
        count = count + 2
    elif(j[0] == 'C' and j[1] == 'Z'):
        count = count + 6

print(count)

#PART 2
#X -> lose, Y -> draw, z -> win
# A, X -> rock, lose -> rock, scissor => 0 + 3 = 3
# a, y -> rock, draw -> rock, rock => 1 + 3 = 4
# a, z -> rock, win -> rock, paper => 2 + 6 = 8
# b, x -> paper, lose -> paper, rock => 1 + 0 = 1
# b, y -> paper, draw -> paper, paper => 2 + 3 = 5
# b, z -> paper, win -> paper, scissor => 3 + 6 = 9
# c, x -> scissor, lose -> scissor, paper => 2 + 0 = 2
# c, y -> scissor, draw -> scissor, scissor => 3 + 3 = 6
# c, z -> scissor, win -> scissor, rock => 1 + 6 = 7
count2 = 0
for j in splitPlays:
    if(j[0] == 'A' and j[1] == 'X'):
        count2 = count2 + 3
    elif(j[0] == 'A' and j[1] == 'Y'):
        count2 = count2 + 4
    elif(j[0] == 'A' and j[1] == 'Z'):
        count2 = count2 + 8
    elif(j[0] == 'B' and j[1] == 'X'):
        count2 = count2 + 1
    elif(j[0] == 'B' and j[1] == 'Y'):
        count2 = count2 + 5
    elif(j[0] == 'B' and j[1] == 'Z'):
        count2 = count2 + 9
    elif(j[0] == 'C' and j[1] == 'X'):
        count2 = count2 + 2
    elif(j[0] == 'C' and j[1] == 'Y'):
        count2 = count2 + 6
    elif(j[0] == 'C' and j[1] == 'Z'):
        count2 = count2 + 7

print(count2)

inp.close()

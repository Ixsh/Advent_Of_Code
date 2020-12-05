import math as m

with open('C:/Users/durha/Desktop/input.txt', 'r', encoding='utf-8') as f:
  arr = f.read().splitlines()

f.close()

def find_seat_ID(boardingPasses, op = 'max'):

    seatIDs = []
    for boardingPass in boardingPasses:
        rowMin = 0
        rowMax = 127
        colMin = 0
        colMax = 7
        for char in boardingPass:
            if char == 'F':
                rowMax -= int(m.ceil((rowMax - rowMin) / 2.0))
            elif char == 'B':
                rowMin += int(m.ceil((rowMax - rowMin) / 2.0))
            elif char == 'L':
                colMax -= int(m.ceil((colMax - colMin) / 2.0))
            elif char == 'R':
                colMin += int(m.ceil((colMax - colMin) / 2.0))
        seatIDs.append(rowMax * 8 + colMax)

    # Returns the max seatID or the missing seatID for the op
    if op == 'max':
        return max(seatIDs)
    if op == 'missing':
        return sorted(set(range(min(seatIDs), max(seatIDs))) - set(seatIDs)).pop()
    
    # Returns seatIDs by default if op is not set correctly
    return seatIDs


#print(find_seat_ID(arr, 'max'))
print(find_seat_ID(arr, 'missing'))

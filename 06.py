def union(x: int, y: int, bands: list, moves: dict) -> tuple:
    for i in range(len(bands)):
        if x in bands[i] and y in bands[i]:
            return bands, moves
        if x in bands[i]:
            x_mas_index = i
        elif y in bands[i]:
            y_mas = bands[i]
    for i in range(len(y_mas)):
        bands[x_mas_index].append(y_mas[i])
    for i in range(len(bands[x_mas_index])):
        moves[bands[x_mas_index][i]] += 1
    bands.remove(y_mas)
    return bands, moves
            

def find(x: int, y: int, bands: list) -> str:
    for i in range(len(bands)):
        if x in bands[i] and y in bands[i]:
            return 'YES'
    return 'NO'

n, m = map(int, input().split())
bands = []
moves = {}
for i in range(1, n+1):
    moves[i] = 1
    bands.append([i])
results = []


for _ in range(m):
    query = input().split()
    match query[0]:
        case '1':
            x, y = map(int, query[1:])
            bands, moves = union(x, y, bands, moves)
        case '2':
            x, y = map(int, query[1:])
            result = find(x, y, bands)
            results.append(result)
        case '3':
            x = int(query[1])
            results.append(moves[x])
    #print(bands)

for result in results:
    print(result)




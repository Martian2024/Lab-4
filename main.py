import csv

SPACE = 9
with open('data.tsv') as file:
    parsed_data = list(map(lambda x: x[1:], csv.reader(file, delimiter='\t')))[1:]

matrix = [[(0, []) for _ in range(SPACE + 1)] for _ in range(len(parsed_data) + 1)]

for y in range(1, len(matrix)):
    for x in range(1, len(matrix[0])):
        if int(parsed_data[y - 1][1]) <= x:
            if matrix[y - 1][x][0] > int(parsed_data[y - 1][2]) + matrix[y - 1][max(0, x - int(parsed_data[y - 1][1]))][0]:
                matrix[y][x] = matrix[y - 1][x]
            else:
                matrix[y][x] = (int(parsed_data[y - 1][2]) + matrix[y - 1][max(0, x - int(parsed_data[y - 1][1]))][0], matrix[y - 1][max(0, x - int(parsed_data[y - 1][1]))][1] + [parsed_data[y - 1][0]])
        else:
            matrix[y][x] = matrix[y - 1][x]
        #matrix[y][x] = max(matrix[y - 1][x], int(parsed_data[y - 1][2]) + matrix[y - 1][max(0, x - int(parsed_data[y - 1][1]))] if int(parsed_data[y - 1][1]) <= x else 0)

#for i in matrix:
#    print(list(map(lambda x: x[0], i)))

inventory = []
for item in matrix[-1][-1][1]:
    inventory += [item] * int(list(filter(lambda x: x[0] == item, parsed_data))[0][1])

print('Максимальная ценность предметов в инвентаре 3х3:', matrix[-1][-1][0])

for i in range(0, 9, 3):
    print(' '.join(inventory[i:i + 4]))
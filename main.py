import csv


def func(space, parsed_data):
    matrix = [[(0, []) for _ in range(space + 1)] for _ in range(len(parsed_data) + 1)]

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

    return matrix

def assemble_inventory(lst, parsed_data):
    inventory = []
    for item in lst:
        inventory += [item] * int(list(filter(lambda x: x[0] == item, parsed_data))[0][1])
    return inventory

if __name__ == '__main__':
    SPACE = 9
    STARTING_POINTS = 15
    with open('data.tsv') as file:
        parsed_data = list(map(lambda x: x[1:], csv.reader(file, delimiter='\t')))[1:]
    max_points = sum(map(lambda x: int(x[2]), parsed_data))

    matrix = func(SPACE, parsed_data)

    print(f'Конечное количество очков: {matrix[-1][-1][0] - (max_points - matrix[-1][-1][0]) + STARTING_POINTS}')
    if matrix[-1][-1][0] - (max_points - matrix[-1][-1][0]) + STARTING_POINTS > 0:
        print('Ура! Мы не умрем!')
    else:
        print('О-о нет...')

    for i in range(0, 9, 3):
        print(' '.join(assemble_inventory(matrix[-1][-1][1], parsed_data)[i:i + 3]))
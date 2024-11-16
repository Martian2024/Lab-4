from main import func, assemble_inventory
import csv

if __name__ == '__main__':
    SPACE = 7
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
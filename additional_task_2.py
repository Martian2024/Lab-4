from main import func, assemble_inventory
import csv

def check(combination, lst):
    for i in lst:
        if set(i) == set(combination):
            return True
    return False

if __name__ == '__main__':
    SPACE = 9
    STARTING_POINTS = 15
    with open('data.tsv') as file:
        parsed_data = list(map(lambda x: x[1:], csv.reader(file, delimiter='\t')))[1:]
    max_points = sum(map(lambda x: int(x[2]), parsed_data))


    matrix = func(SPACE, parsed_data)
    list_of_combinations = []
    counter = 1
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x][0] * 2 - max_points + STARTING_POINTS > 0 and not check(matrix[y][x][1], list_of_combinations):
                print(f'{counter}. Количество очков: {matrix[y][x][0] * 2 - max_points + STARTING_POINTS}')
                for i in range(0, 9, 3):
                    print(' '.join(assemble_inventory(matrix[y][x][1], parsed_data)[i:i + 3]))
                print()
                list_of_combinations.append(matrix[y][x][1])
                counter += 1


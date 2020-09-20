number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][0])  # accessing the index 1 List

for row in number_grid:
    for col in row:  # print each letter
        print(col)

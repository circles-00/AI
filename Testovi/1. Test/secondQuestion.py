def mine_sweeper(table):
    # Initially set the '-'' items to 0
    for rows in range(len(table)):
        for columns in range(len(table)):
            if table[rows][columns] == '-':
                table[rows][columns] = int('0')

    # Counting all of the mines
    for rows in range(len(table)):
        for columns in range(len(table)):
            if table[rows][columns] == '#':
                continue
            if rows < n - 1 and table[rows + 1][columns] == '#':
                table[rows][columns] += 1
            if rows > 0 and table[rows - 1][columns] == '#':
                table[rows][columns] += 1
            if columns > 0 and table[rows][columns - 1] == '#':
                table[rows][columns] += 1
            if columns < n - 1 and table[rows][columns + 1] == '#':
                table[rows][columns] += 1
            if rows > 0 and columns > 0 and table[rows - 1][columns - 1] == '#':
                table[rows][columns] += 1
            if rows > 0 and columns < n - 1 and table[rows - 1][columns + 1] == '#':
                table[rows][columns] += 1
            if rows < n - 1 and columns > 0 and table[rows + 1][columns - 1] == '#':
                table[rows][columns] += 1
            if rows < n - 1 and columns < n - 1 and table[rows + 1][columns + 1] == '#':
                table[rows][columns] += 1

    # Using list comprehension to convert every element from integer to string
    res_table = [[str(row) for row in column] for column in table]

    return res_table


if __name__ == "__main__":
    # Take user's input
    n = int(input())
    mine_table = []
    for i in range(n):
        mine_table.append([j for j in input().split("   ")])

    # Print the resulting list (minesweeper)
    new_table = mine_sweeper(mine_table)
    for i in range(n):
        for j in range(n):
            print(new_table[i][j] + "   ", end="")
            # print((3*str(" ")).join(new_table[i][j]), end="") // doesn't work
        print("")

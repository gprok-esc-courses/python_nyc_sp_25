import random

def get_alive_neighbors(row, col, curr):
    n = 0
    n += curr[row-1][col-1] if (size > row-1 >= 0) and (size > col-1 >= 0) else 0
    n += curr[row-1][col] if (size > row-1 >= 0) and (size > col >= 0) else 0
    n += curr[row-1][col+1] if (size > row-1 >= 0) and (size > col+1 >= 0) else 0
    n += curr[row][col-1] if (size > row >= 0) and (size > col-1 >= 0) else 0
    n += curr[row][col+1] if (size > row >= 0) and (size > col+1 >= 0) else 0
    n += curr[row+1][col-1] if (size > row+1 >= 0) and (size > col-1 >= 0) else 0
    n += curr[row+1][col] if (size > row+1 >= 0) and (size > col >= 0) else 0
    n += curr[row+1][col+1] if (size > row+1 >= 0) and (size > col+1 >= 0) else 0
    return n

size = int(input("Size: "))

current = []
next = []

# Create and polulate the initial, 1st generation
generation = 1
for r in range(size):
    row = [] 
    for c in range(size):
        row.append(random.randint(0,1))
    current.append(row)
    next.append([0]*size)

answer = 'y'

while answer == 'y':
    # Display generation
    print("===== GEN", generation, " ====")
    for r in range(size):
        for c in range(size):
            if current[r][c] == 1:
                print('X', end=' ')
            else:
                print('-', end=' ')
        print()

    answer = input("Next? (y/n): ")

    if answer == 'y':
        # Calculate next
        for r in range(size):
            for c in range(size):
                n = get_alive_neighbors(r, c, current)
                # identyfy next state 
                next_state = 0
                if current[r][c] == 1 and (n == 2 or n == 3):
                    next_state = 1
                elif current[r][c] == 1:
                    next_state == 0
                elif current[r][c] == 0 and n == 3:
                    next_state = 1
                else:
                    next_state = 0
                next[r][c] = next_state
        # Copy next to current
        for r in range(size):
            for c in range(size):
                current[r][c] = next[r][c]
        generation += 1
    else:
        print("Bye!")
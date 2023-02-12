INPUT_FILE_PATH = 'data/test-input.txt'

CRT_WIDTH = 40
CRT_HEIGTH = 6

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().strip().split('\n')

    # Part 1 ---------------------------------------------------------------
    X = [1] # X[i] is the value of X at the end of cycle i (cycle from 1 to N)(X[0] only for inizialization) 
       
    for line in lines:
        instruction = line.split()
        if instruction[0] == 'addx':
            X.append(X[-1])
            X.append(X[-1] + int(instruction[1]))
        else:
            X.append(X[-1])

    total_signal_strengths = 0
    for i in {20,60,100,140,180,220}:
        total_signal_strengths += get_signal_strength(X, i)

    print(total_signal_strengths) # <Part 1>

    # Part 2 ---------------------------------------------------------------
    CRT = [ [['?'] for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGTH)]

    for row in range(CRT_HEIGTH):
        for col in range(CRT_WIDTH):
            cycle = CRT_WIDTH * row + col + 1 # or counter
            if abs(X[cycle - 1] - col) <= 1: # col == X[cycle-1] or col == X[cycle-1]+1 or col == X[cycle-1]-1:
                CRT[row][col] = "#"
            else:
                CRT[row][col] = "."

    for row in CRT:
        print("".join(row)) # <Part 2>

def get_signal_strength(X, i):
    return X[i-1] * i

if __name__ == "__main__":
    main()
INPUT_FILE_PATH = 'data/test-input.txt'

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        list = [[int(y) for y in x.split("\n") if y] for x in f.read().split("\n\n")]
    
    sum_list = [sum(el) for el in list]
    max_val = max(sum_list)

    print(max_val) # <Part 1>
    print(sum(max_n(sum_list, 3))) # <Part 2>

def max_n(elements, n):
    return sorted(elements, reverse=True)[:n]

if __name__ == "__main__":
    main()

def main():
    with open('input.txt', 'r') as f:
        list = [[int(y) for y in x.split("\n") if y] for x in f.read().split("\n\n")]
        sum_list = [sum(el) for el in list]

        max_val = max(sum_list)

        print(max_val) # Part 1
        print(sum(maxN(sum_list, 3))) # Part 2


def maxN(elements, n):
    return sorted(elements, reverse=True)[:n]

if __name__ == "__main__":
    main()

import re

INPUT_FILE_PATH = '../input.txt'

min_val = 1 # 1
max_val = 99 # 10

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

        # # Find min and max val 
        # global min_val 
        # global max_val 
        # val_list = re.split('\n|,|-', file)
        # min_val = min(val_list) # 1
        # max_val = max(val_list) # 99

        issubset_count = 0
        intersect_count = 0
        file = file.split("\n")
        for line in file:
            i1_str, i2_str = line.split(",")
            i1 = get_interval(i1_str)
            i2 = get_interval(i2_str)
            if i1.issubset(i2) or i2.issubset(i1): issubset_count += 1
            if len(i1.intersection(i2)) > 0: intersect_count += 1
            # print(render_interval(i1), i1_str)
            # print(render_interval(i2), i2_str)
            # print()
        
        print(f"{issubset_count = }") # Part 1
        print(f"{intersect_count = }") # Part 2

def render_interval(interval):
    interval_str = ""
    for i in range(min_val, max_val+1):
        if i in interval:
            interval_str += str(i)
        else:
            interval_str += "."    
    return interval_str

def get_interval(str):
    interval = str.split("-")
    return set (range(int(interval[0]), int(interval[1])+1))

if __name__ == "__main__":
    main()
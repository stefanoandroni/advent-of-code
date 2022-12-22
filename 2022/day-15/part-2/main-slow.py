import re

INPUT_FILE_PATH = '../data/input.txt'

C_min = 0
C_max = 4_000_000

# the distress beacon is not detected by any sensor
# tuning_frequency(x, y) = X_max * x + y 

# 1) find distress beacon pos (x, y) in search space (one only possible position in the search area)

# 2) calculate and return tuning_frequency

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    S, B = parse_file(file)  # S: sensors -> (x,y) # B: beacons -> (x,y)

    I = {}
    for y in range(C_max + 1): # [0,C_max]
        I[y] = get_intervals(S, B, y)

    distress_beacon = find_distress_beacon(I)
    # print(distress_beacon)
    tuning_frequency = get_tuning_frequency(distress_beacon)
    print(tuning_frequency) # <Part 2>

def find_distress_beacon(I):
    for key in I:
        R = set(range(C_min, C_max + 1)) # R: result -> (x0, x1, x2, .., xn)
        for (xs, xe) in I[key]:
            R = R - set(range(xs, xe + 1))
        if len(R) == 1: # > 0 never 
            (x, ) = R
            return (x, key)
    return None

def get_tuning_frequency(point):
    x, y = point
    return 4_000_000 * x + y

def get_intervals(S, B, Y):
    I = set() # (x_start, x_end)
    for i in range(len(S)): # len(S) = len(B)
        s = xs, ys = S[i]
        b = xb, yb = B[i]
        delta_x = get_manhattan_distance(s, b) - abs(ys - Y)
        if delta_x > 0:
            x_start, x_end = tuple(sorted((xs + delta_x, xs - delta_x)))
            if not(x_end < C_min) and not(x_start > C_max): # not (ends before or starts after the search space)
                if x_start < C_min:
                    x_start = C_min
                if x_end > C_max:
                    x_end = C_max            
                I.add((x_start, x_end))
    return I

def get_manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def parse_file(file): #(c,r)
    S = []
    B = []
    for line in file.split('\n'):
        matches = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        for match in matches:
            xs, ys, xb, yb = match
            S.append((int(xs), int(ys)))
            B.append((int(xb), int(yb)))
    return S, B

if __name__ == "__main__":
    main()
import re

# y = m(x+d) + q
# 
# M +
# q = y - (x + d) = y-x-d
# q = y - (x - d) = y-x+d

# M -
# q = y + (x + d) = y+x+d
# q = y + (x - d) = y+x-d


INPUT_FILE_PATH = '../data/input.txt'

C_min = 0
C_max = 4_000_000

def main():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    S, B, D = parse_file(file)  # S: sensors -> (x,y) # B: beacons -> (x,y) # D: distances (D[i] = distance between S[i] and B[i])

    # Calculate the q (y = mx + q, m in {1, -1}) of the straight lines of the edges of the rhombus
    M_pos, M_neg = get_borders(S, D)

    distress_beacon = get_distress_beacon(S, D, M_pos, M_neg)

    tuning_frequency = get_tuning_frequency(distress_beacon)
    print(tuning_frequency) # <Part 2>
 
def get_distress_beacon(S, D, M_pos, M_neg):
    for a in M_pos:
        for b in M_neg:
            p = ((b-a)//2, (a+b)//2) # intersection point
            if all(0 < c < C_max for c in p):
                if all(get_manhattan_distance(p, S[i]) > D[i] for i in range(len(S))):
                    return p
    return None

def get_borders(S, D):
    M_pos = set() # m = +1
    M_neg = set() # m = -1
    for i in range(len(S)): # len(S) == len(B) == len(D)
        x, y = S[i]
        d = D[i] 
        M_pos.add(y - x + d + 1) 
        M_pos.add(y - x - d - 1)
        M_neg.add(y + x + d + 1) 
        M_neg.add(y + x - d - 1) 
    return M_pos, M_neg

def get_tuning_frequency(point):
    x, y = point
    return 4_000_000 * x + y

def get_manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def parse_file(file): #(c,r)
    S = []
    B = []
    D = []
    for line in file.split('\n'):
        matches = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        for match in matches:
            xs, ys, xb, yb = match
            S.append((int(xs), int(ys)))
            B.append((int(xb), int(yb)))
            D.append(get_manhattan_distance((int(xs), int(ys)), (int(xb), int(yb))))
    return S, B, D

if __name__ == "__main__":
    main()
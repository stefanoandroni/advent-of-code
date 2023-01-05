import re

INPUT_FILE_PATH = '../data/test-input.txt'
Y = 2_000_000

def main():
    global B_set
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    S, B = parse_file(file)  # S: sensors # B: beacons
    B_set = set(B)

    N = set() # N: positions a beacon cannot possibly exist
    for i in range(len(S)): # len(S) = len(B)
        print(f"{i+1}/{len(S)}")
        distance = get_manhattan_distance(S[i], B[i])
        print(distance)
        N.update(get_no_beacon_points(S[i], distance))

    R = [(x,y) for (x,y) in N if y==Y]
    print(len(R))

    # for (x,y) in N:
    #     print((x,y))
    # print(sum([(a, b) for (a, b) in N if a==10]))
    
def get_no_beacon_points(point, distance):
    N = set() # set to return
    A = set() # last added

    A.add(point)
    for d in range(distance):
        print(d)
        for p in A.copy():
            x, y = p
            p1 = (x - 1, y)
            p2 = (x + 1, y)
            p3 = (x, y - 1)
            p4 = (x, y + 1)
            L = [p for p in [p1, p2, p3, p4] if p not in B_set]
            l = [p for p in [p1, p2, p3, p4] if p not in N]
            N.update(L)
            A.remove(p)
            A.update(l)

    return N

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
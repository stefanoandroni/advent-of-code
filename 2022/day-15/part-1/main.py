import re

INPUT_FILE_PATH = '../data/test-input.txt'
Y = 10 #2000000

def main():
    S, B = parse_file(INPUT_FILE_PATH)  # S: sensors -> (x,y) # B: beacons -> (x,y)
    I = get_intervals(S, B, Y) # I: intervals (of not allowed beacon positions) -> (x_start, x_end)

    R = set() # R: result -> (x0, x1, x2, .., xn)
    for xs, xe in I:
        R.update(range(xs, xe + 1))
    
    # notR = {x for x in R if (x, Y) in B}
    R = {x for x in R if (x, Y) not in B} # remove position with explixit beacon

    print(len(R)) # <Part 1>


def get_intervals(S, B, Y):
    I = set() # (x_start, x_end)
    for i in range(len(S)): # len(S) = len(B)
        s = xs, ys = S[i]
        b = xb, yb = B[i]
        delta_x = get_manhattan_distance(s, b) - abs(ys - Y)
        if delta_x > 0:
            interval = tuple(sorted((xs + delta_x, xs - delta_x)))
            I.add(interval)
    return I

def get_manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def parse_file(path): #(c,r)
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')
    S = []
    B = []
    for line in lines:
        matches = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        for match in matches:
            xs, ys, xb, yb = match
            S.append((int(xs), int(ys)))
            B.append((int(xb), int(yb)))
    return S, B

if __name__ == "__main__":
    main()
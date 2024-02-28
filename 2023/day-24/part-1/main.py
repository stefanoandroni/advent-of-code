
import re


INPUT_FILE_PATH = '../data/input.txt'

# ??: precision or time problems

MIN = 200000000000000 # 7
MAX = 400000000000000 # 27

# 146 too low

def main():
    # hailstones: list of hailstones; each hailstone is a tuple ((px, py, pz), (vx, vy, vz))
    hailstones = parse_input_file() 

    # linear_equation_hailstones: list of hailstones; each hailstone is a tuple (m, q) representing a line y=mx+q
    linear_equation_hailstones = vector_to_linear_equation(hailstones)

    count = 0
    crossed = set()
    # For each pair of linear equations
    for i in range(len(linear_equation_hailstones)):
        for j in range(i+1, len(linear_equation_hailstones)):
            # Check for past crossing # TODO: wrong
            if i not in crossed and j not in crossed:
                # Check for intersection
                ix, iy = find_intersection(linear_equation_hailstones[i], linear_equation_hailstones[j])
                if ix != None and iy != None: # non-parallel lines
                    # Chef for intersection in boundaries
                    if ix >= MIN and ix <= MAX and iy >= MIN and iy <= MAX:
                        count += 1
                        crossed.add(i)
                        crossed.add(j)
    # Part 1
    print(count)


def find_intersection(e1, e2):
    m1, q1 = e1
    m2, q2 = e2

    if m1 == m2: # //
        return None, None
    
    # ix, iy intersection
    ix = (q2-q1)/(m1-m2)
    iy = m1*ix + q1

    return ix, iy


def vector_to_linear_equation(vectors):
    linear_equations = []
    for vector in vectors:
        (px, py, pz), (vx, vy, vz) = vector
        linear_equations.append((vy/vx, py-(vy/vx)*px))
    return linear_equations


def parse_input_file():
    hailstones = []
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.readlines()

    regex = re.compile('(-?\d+),\s*(-?\d+),\s*(-?\d+)\s+@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)') # TODO: generalize RE

    for line in lines:
        matches = re.match(regex, line)
        # NOTE: bad
        hailstones.append(((int(matches[1]), int(matches[2]), int(matches[3])), (int(matches[4]), int(matches[5]), int(matches[6]))))
    
    return hailstones


if __name__ == "__main__":
    main()

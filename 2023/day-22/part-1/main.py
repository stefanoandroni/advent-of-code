
INPUT_FILE_PATH = '../data/test-input.txt'

def main():
    global max_z

    # B: (bricks) list of tuples ((xs, ys, zs), (xe, ye, ze)) representing a brick
    # from (xs, ys,zs) to (xe, ye, ze)), sortered by z
    B = parse_input_file() 

    # max_z: dict of key = (x, y), value = highest z brick value in the (x, y) coordinates
    max_z = dict()

    # (1) BRICKS FALLING SIMULATION
    settled_bricks = []
    for brick in B:
        (xs, ys, zs), (xe, ye, ze) = brick
        
        # Get the lowest z possible (drop the brick)
        new_zs = get_min_z_for_brick(brick) # z start
        new_ze = ze - zs + new_zs # z end

        # Add brick to settled_bricks list with new z value
        settled_bricks.append(((xs, ys, new_zs), (xe, ye, new_ze)))

        # Update max_z dict
        # NOTE: one of the two cycles loops only once (xs == xe+1 or ys == ye+1)
        for ix in range(xs, xe + 1):
            for iy in range(ys, ye + 1):
                if (ix, iy) in max_z:
                    max_z[(ix, iy)] = max(new_ze, max_z[(ix, iy)])
                else:
                    max_z[(ix, iy)] = new_ze
    

    # (2) GET THE NUMBER OF BRICKS THAT CAN BE DISINTEGRATED
    settled_bricks = sorted(settled_bricks, key=lambda brick: brick[0][2])

    supports_dict = {i: set() for i in range(len(settled_bricks))}
    supported_dict = {i: set() for i in range(len(settled_bricks))}

    for i_up, up_brick in enumerate(settled_bricks):
        for i_down, down_brick in enumerate(settled_bricks[:i_up]):
            (xs_u, ys_u, zs_u), (xe_u, ye_u, ze_u) = up_brick
            (xs_d, ys_d, zs_d), (xe_d, ye_d, ze_d) = down_brick

            # NOTE: they support each other iff:
            # - (they touch each other on z axis) the starting z of the upper block is equal to the ending z 
            #   of the lower block - 1
            # - they intersect on the (x, y) plane

            # Check if they touch on the z axis
            if zs_u == ze_d + 1: 
                # Check if there is an intersection on the (x,y) plane
                if max(xs_u, xs_d) <= min(xe_u, xe_d) and max(ys_u, ys_d) <= min(ye_u, ye_d):
                    supports_dict[i_down].add(i_up)
                    supported_dict[i_up].add(i_down)

    # Get the number of bricks that can be disintegrated
    total = 0
    for i in range(len(settled_bricks)):
        # Check if if all the bricks it supports are supported by more than one brick
        if all(len(supported_dict[k]) > 1 for k in supports_dict[i]):
            total += 1
    # Part 1
    print(total)


def get_min_z_for_brick(brick):
    (xs, ys, zs), (xe, ye, ze) = brick
    
    z_max = 0
    # NOTE: one of the two cycles loops only once (xs == xe+1 or ys == ye+1)
    for ix in range(xs, xe + 1):
        for iy in range(ys, ye + 1):
            if (ix, iy) in max_z:
                if max_z[(ix, iy)] > z_max:
                    z_max = max_z[(ix, iy)]
    return z_max + 1

   
def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()
    
    bricks = []
    for line in file.splitlines():
        coords1, coords2 = line.split('~')
        x1, y1, z1 = map(int, coords1.split(','))
        x2, y2, z2 = map(int, coords2.split(','))
        # bricks.append(((x1, y1, z1), (x2 - x1, y2 - y1, z2 - z1)))
        bricks.append(((x1, y1, z1), (x2, y2, z2)))
        
        # assert x1 <= x2
        # assert y1 <= y2
        # assert z1 <= z2

    # Sort asc by z1
    bricks = sorted(bricks, key=lambda brick: brick[0][2])

    return bricks


if __name__ == "__main__":
    main()

# Approach: Brute Force + Heuristic optimization (pruning tree) (BAD CODING)

from collections import deque
import re

INPUT_FILE_PATH = '../data/test-input.txt'

ORE = 0 
CLAY = 1
OBSIDIAN = 2 
GEODE = 3

TOTAL_TIME = 24 # minutes

ROBOTS = [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)]

def main():
    
    def get_max_costs(project_id):
        project = P[project_id]
        max = [0, 0, 0, 0]
        for robot_cost in project:
            x, y, z, k = robot_cost
            if x > max[0]: max[0] = x
            if y > max[1]: max[1] = y
            if z > max[2]: max[2] = z
            if k > max[3]: max[3] = k # useless
        return max

    global MC, P
    QL = [] # QL: projects' quality levels

    # Parse file
    P = parse_file(INPUT_FILE_PATH)

    # Get mmax # of geodes per project
    for i in range(len(P)):
        project_id = i + 1
        MC = get_max_costs(project_id) # MX: max minerals costs (for all robot) of project with id 'project_id'
        geode_num = get_max_num_of_geodes(P[project_id])
        QL.append(get_quality_level(geode_num, project_id))

    print(sum(QL)) # <Part1>
    
def get_quality_level(geode_num, project_id):
    return geode_num * project_id

def get_max_num_of_geodes(project):

    def sum_tuple(tuple_1, tuple_2):
        return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

    def diff_tuple(tuple_1, tuple_2):
        return tuple(map(lambda i, j: i - j, tuple_1, tuple_2))

    def get_buildable_robots(minerals):
        B = []

        for i in range(len(project)):
            x, y, z, _  = diff_tuple(minerals, project[i])
            if x >= 0 and y >= 0 and z >= 0:
                B.append(i)
        return B

    def get_optimized_state(state):
        add = True
        
        (ore_r, cla_r, obs_r, geo_r), (ore_m, cla_m, obs_m, geo_m), t = state
        
        # Opt1: keep only the resources needed in the worst case
        if ore_m > (MC[ORE] * t) - (ore_r * (t-1)): 
            ore_m = (MC[ORE] * t) - (ore_r * (t-1))
        if cla_m > (MC[CLAY] * t) - (cla_r * (t-1)):
            cla_m =(MC[CLAY] * t) - (cla_r * (t-1))
        if obs_m > (MC[OBSIDIAN] * t) - (obs_r * (t-1)):
            obs_m = (MC[OBSIDIAN] * t) - (obs_r * (t-1))
        if ore_m > (MC[ORE] * t) - (ore_r * (t-1)):
            ore_m = MC[ORE]

        # Opt2: limits the production of useless robots
        if ore_r > MC[ORE]: ore_r = MC[ORE]
        if cla_r > MC[CLAY]: cla_r = MC[CLAY]
        if obs_r > MC[OBSIDIAN]: obs_r = MC[OBSIDIAN] # if geo_r > MC[3]:

        # Opt3
        # if TM[t] > geo_m: # 1) > 0r >=?? 2) su m o r??
        #     add = False
        
        state = ((ore_r, cla_r, obs_r, geo_r), (ore_m, cla_m, obs_m, geo_m), t)

        if state in S:
            add = False

        return add, state
    
    def add_state(state):
        add, state = get_optimized_state(state)
        if add:
            queue.append(state)

    S = set()
    TM = [0] * (TOTAL_TIME + 1) # Geode Max at time
    max_geode = 0
    queue = deque()

    R = (1, 0, 0, 0) # robot [Ore, Clay, Obsidian, Geode]
    M = (0, 0, 0, 0) # minerals [Ore, Clay, Obsidian, Geode]
    t = TOTAL_TIME
    s0 = (R, M, TOTAL_TIME)

    add_state(s0)

    while queue:
        r, m, t = s = queue.popleft()

        if s in S:
            continue

        S.add(s)

        if t > 0:

            # Update minerals and time
            new_minerals = sum_tuple(m, r)
            new_t = t - 1

            # Update max
            _, _, _, geode_num = new_minerals
            max_geode = max(max_geode, geode_num)
            # TM[t] = max(TM[t], geode_num)


            # Get buildable robots
            B = get_buildable_robots(m)

            if GEODE in B: # If i can build a geode robot, i build it
                new_robots = sum_tuple(r, ROBOTS[GEODE])
                new_minerals = diff_tuple(new_minerals, project[GEODE])
                state = (new_robots, new_minerals, new_t)
                add_state(state)
            else:
                # I don't build any robots
                state = (r, new_minerals, new_t)
                add_state(state) 
                # I try to build every robot possible
                for i in B:
                    new_r = sum_tuple(r, ROBOTS[i])
                    new_m = diff_tuple(new_minerals, project[i])
                    state = (new_r, new_m, new_t)
                    add_state(state) 
 
    return max_geode

def parse_file(path):
    P = {}
    with open(path, 'r') as f:
        projects_lines = f.read().strip().split('\n')

    pattern = r'(\d+)'
    for project in projects_lines:
        r = re.findall(pattern, project)
        r = [int(x) for x in r]
        P[r[0]] = [
            # (ore, clay, obsidian, geode)
            (r[1], 0, 0, 0), # ore robot cost
            (r[2], 0, 0, 0), # clay robot cost
            (r[3], r[4], 0, 0), # obsidian robot cost
            (r[5], 0, r[6], 0) # geode robot cost
        ]

    return P

if __name__ == "__main__":
    main()

# Project id    robot               costs 
# --------------------------------------------
# id              

#               Ore robot           N ore

#               Clay robot          N ore

#               Obsidian robot      N ore 
#                                   M clay

#               Geode robot         N ore
#                                   M obsidian
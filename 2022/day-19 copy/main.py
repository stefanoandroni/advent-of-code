# Approach: Brute Force + Heuristic optimization (pruning tree) (BAD CODING)

from collections import deque
import re

INPUT_FILE_PATH = 'data/test-input.txt'

ORE = 0 
CLAY = 1
OBSIDIAN = 2 
GEODE = 3

TOTAL_TIME = 24 # minutes

ROBOTS = [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)]

def main():
    global P
    global MC

    P = parse_file(INPUT_FILE_PATH)
    
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
    
    QL = [] # QL: projects' quality levels

    for i in range(len(P)):
        project_id = i + 1
        MC = get_max_costs(project_id) # MX: max minerals costs (for all robot) of current project
        geode_num = get_max_num_of_geodes(P[project_id])
        print(geode_num)
        
        QL.append(get_quality_level(geode_num, project_id))

    #print(sum(QL))
    
def get_quality_level(geode_num, project_id):
    return geode_num * project_id

def get_max_num_of_geodes(project):

    def sum_tuple(tuple_1, tuple_2):
        return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

    def diff_tuple(tuple_1, tuple_2):
        return tuple(map(lambda i, j: i - j, tuple_1, tuple_2))

    def get_buildable_robots(minerals):
        B = []

        for index, robot_cost in enumerate(project):
            x, y, z, _ = new_tuple = diff_tuple(minerals, robot_cost)
            if x >= 0 and y >= 0 and z >= 0:
                B.append([index, robot_cost])
        return B

    def optimized(state):
        (ore_r, cla_r, obs_r, geo_r), (ore_m, cla_m, obs_m, geo_m), t = state
        if state in S:
            return False
        if ore_r > MC[0] or cla_r > MC[1] or obs_r > MC[2]: # or geo_r > MC[3]:
            return False
        return True
    
    queue = deque()

    R = (1, 0, 0, 0) # robot [Ore, Clay, Obsidian, Geode]
    M = (0, 0, 0, 0) # minerals [Ore, Clay, Obsidian, Geode]
    t = TOTAL_TIME
    s0 = (R, M, t)

    queue.append(s0)

    max_geode = 0
    S = set()

    while queue:
        r, m, t = s = queue.popleft()
        S.add(s)
        # print(s)
        if t >= 0:
            
            _, _, _, geode_r = r
            if geode_r > max_geode:
                max_geode = geode_r
            # Opt2, Opt3, Opt4

            # if len(B) == 0: # Non posso costruire robot       # FORSE: se non posso costruire robot nel t rimanente
            #     print("I CANT")
            state = (r, sum_tuple(m, r), t-1)
            if optimized(state):
                queue.append(state) 

            B = get_buildable_robots(m)
            #else: # Posso costruire robot
            if GEODE in [x for x, _ in B]: # Posso costruire robot di GEODE
                b = [(x,y) for x, y in B if x == GEODE][0]
                robot_index, robot_cost = b
                state = (sum_tuple(r, ROBOTS[robot_index]), diff_tuple(sum_tuple(m, r), robot_cost), t-1)
                queue.append(state)
            else: 
                for b in B:
                    robot_index, robot_cost = b
                    state = (sum_tuple(r, ROBOTS[robot_index]), diff_tuple(sum_tuple(m, r), robot_cost), t-1)
                    if optimized(state):
                        queue.append(state) 

    return max_geode

def parse_file(path):
    P = {}
    with open(INPUT_FILE_PATH, 'r') as f:
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

        # P[r[0]] = {
        #     ORE: {
        #         ORE: r[1]
        #         },
        #     CLAY: {
        #         ORE: r[2]
        #     },
        #     OBSIDIAN: {
        #         ORE: r[3],
        #         CLAY: r[4]
        #     },
        #     GEODE: {
        #         ORE: r[5],
        #         OBSIDIAN: r[6]
        #     }
        # }
        # Examples
        # print(P[1][ORE]) # costs of ORE ROBOT building for project 1
        # print(P[1][ORE].keys()) # index of minerals needed to built ORE ROBOT for project 1

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
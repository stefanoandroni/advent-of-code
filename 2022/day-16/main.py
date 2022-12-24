import re
from collections import deque, defaultdict
from itertools import permutations

INPUT_FILE_PATH = 'data/input.txt'

START_VALVE = "AA"

TOTAL_TIME_1 = 30 
TOTAL_TIME_2 = 26
OPEN_TIME = 1 
STEP_TIME = 1 
# time in minutes

def main():
    global N
    global G
    global V

    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read().strip()

    # Parse file
    V = parse_file(file) # V: valves id -> rate: int,  to: [id, id, ...]
    
    # Reduce problem
    N, G = reduce_graph(V) # N: nodes, G: graph matrix
    
    # Simulate    
    # Part1 - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - -
    s1 = simulate(TOTAL_TIME_1)
  
    m = max(s1.values())
    print(m) # <Part 1>

    # Part2 - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - -
    s2 = simulate(TOTAL_TIME_2)
    m = max(s2.values())

    # works cause A has rate=0
    m = 0
    for key1, value1 in s2.items():
        for  key2, value2 in s2.items():
            c1, t1, set1 = key1
            c2, t2, set2 = key2
            if len(set(set1) & set(set2)) == 0: # no intersection
                if value1 + value2 > m:
                    m = value1 + value2
    print(m) # <Part 2> # O(N^2) -> very slow
    
def simulate(T): 
    queue = deque()
    B = defaultdict(lambda: -1)
    c = START_VALVE

    def add(c, t, o, f):
        # c: current node [String], t: time left [Int], o: opened nodes [Set], f: total pressure [Int]
        if t >= 0 and (B[(c, t, o)] < f):
            B[(c, t, o)] = f
            queue.append((c, t, o, f))

    add(c, T, tuple(), 0)

    while queue:
        c, t, o, f = queue.popleft()
        if t > 0 and (c not in o):
            flow_here = (t - OPEN_TIME) * V[c]['rate']
            v_tuple = (c, )
            # open valve
            add(c, t - OPEN_TIME, tuple(sorted(o + v_tuple)), f + flow_here) #tuple(sorted(o + v_tuple)) -> faster

        for n in N:
            t_move_cost = G[N.index(c)][N.index(n)]
            if t_move_cost <= t:
                # move to valve
                add(n, t - t_move_cost, o, f)
    return B

def reduce_graph(Vdict):
    graph_matrix = get_graph_matrix(Vdict)
    floyd_warshall_matrix = get_floyd_warshall_matrix(graph_matrix) # shortest path between each node

    Vpos = [v for v in Vdict if Vdict[v]['rate'] != 0 or v == START_VALVE]
    Vlist = list(Vdict)

    V = []
    for i in range(len(floyd_warshall_matrix)):
        if Vlist[i] in Vpos:
            r = []
            for j in range(len(floyd_warshall_matrix)):
                if Vlist[j] in Vpos:
                    r.append(floyd_warshall_matrix[i][j])
            V.append(r)
    return Vpos, V

def get_floyd_warshall_matrix(graph_matrix):
    V = len(graph_matrix)
    dist = graph_matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )
    return dist

def get_graph_matrix(dict):
    matrix = []
    INF = 999

    for i, ival in enumerate(dict):
        row = []
        for j, jval in  enumerate(dict):
            if ival == jval:
                row.append(0)
            elif jval in dict[ival]['to']:
                row.append(1)
            else:
                row.append(INF)
        matrix.append(row)

    return matrix

def parse_file(file):
    V = {}
    lines = file.split('\n')
    rgx = re.compile(r"^Valve (\w{2}) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]?(.*)")

    for line in lines:
        matches = rgx.match(line)
        id = matches.group(1)
        rate = int(matches.group(2))
        to = matches.group(3).strip().split(", ")
        V[id] = {'rate': rate, 'to': to}
    return V

# def get_best_valve(v, t): # greedy algorithm
#     o = set() # o: options
    
#     # BFS
#     vs = set() # vs: visited set
#     Q = deque()

#     Q.append((v, t))
#     # vs.add(v)

#     while Q:
#         c, t = Q.popleft() # c: current node
#         if c not in vs:
#             vs.add(c)
#             o.add((c, t))
#             for a in V[c]['to']:
#                 Q.append((a, t - 1))

#     # Find best val
#     max_v = None
#     max = 0
#     for el in o:
#         v, t = el
#         # print(v,t)
#         score = V[v]['rate']*(t-1)
#         print(el, score)
#         if score > max:
#             max = score
#             max_v = v
#     return max_v

if __name__ == "__main__":
        main()
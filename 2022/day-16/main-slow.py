import re
from collections import deque, defaultdict
from itertools import permutations

INPUT_FILE_PATH = 'data/input.txt'

START_VALVE = "AA"
TOTAL_TIME = 30 # minutes
OPEN_TIME = 1 # minute
STEP_TIME = 1 # minute

# Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

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

    Na = N.copy()
    if V[START_VALVE]['rate'] == 0:
        Na.remove(START_VALVE)

    P = list() # P: possible orders that we can open the valves
    for r in range(len(Na)):
        print(r, "/", len(Na))
        P.extend(list(permutations(Na, r + 1)))
    
    for p in P.copy():
        time_cost = get_time_cost(p)
        if time_cost > TOTAL_TIME:
            P.remove(p)

    max = 0
    for i, p in enumerate(P):
        print(i, "/", len(P))
        relased_pressure = get_relased_pressure(p)
        if relased_pressure > max:
            max = relased_pressure
    print(max)

    # Problem
    # c: current node, t: time left, o: opened nodes

# def simulate(T):
#     queue = deque()
#     best = defaultdict(lambda: -1)
    
#     v = N.index(START_VALVE) # 'AA'

#     # i: current node index added: ?? v: total flow t: left time #
#     def add(i, added, v, t):
#         if t >= 0 and (best[(i, added, t)] < v):
#             best[(i, added, t)] = v
#             queue.append((i, t, added, v))
    
#     add(aa, 0, 0, T)
#     while queue:
#         i, t, added, v = queue.popleft()
#         if (added & (1 << i)) == 0 and t >= 1:
#             flow_here = (t - 1) * flow_rates[positive_rate_nodes[i]]
#             add(i, added | (1 << i), v + flow_here, t - 1)
        
#         for j in range(M):
#             t_move = graph[positive_rate_nodes[i]][positive_rate_nodes[j]]
#             if t_move <= t:
#                 add(j, added, v, t - t_move)

#     return best

def get_relased_pressure(S):
    left_time = TOTAL_TIME
    S = list(S)
    S.insert(0, START_VALVE)
    
    # pr = False
    # if S == ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']:
    #     pr = True

    total_flow_rate = 0
    total_flow = 0
    i = 0 
    while left_time > 0:
        cost = 0
        if i + 1 < len(S):
            cost = G[N.index(S[i])][N.index(S[i + 1])] # move to valve
            cost +=1
            total_flow += total_flow_rate * cost
            left_time -= cost
            total_flow_rate += V[S[i+1]]['rate']
            i += 1
        else:
            cost += 1 # open valve
            left_time -= cost
            total_flow += total_flow_rate

    return total_flow

def get_time_cost(S):
    S = list(S)
    S.insert(0, START_VALVE)

    cost = 0
    i = 0
    while i < len(S) - 1: # and cost < TOTAL_TIME
        cost += G[N.index(S[i])][N.index(S[i + 1])] # move to valve
        cost += OPEN_TIME # open valve
        i += 1
    return cost

def reduce_graph(Vdict):
    graph_matrix = get_graph_matrix(Vdict)
    floyd_warshall_matrix = get_floyd_warshall_matrix(graph_matrix)
    Vpos = [v for v in Vdict if Vdict[v]['rate'] != 0]
    Vpos.insert(0, START_VALVE)

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
    INF = 99
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

#     print(len(o))
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

if __name__ == "__main__":
        main()

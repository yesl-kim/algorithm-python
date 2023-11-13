from collections import defaultdict
import math

def solution(n, wires):
    adj = defaultdict(list)
    for a, b in wires:
        adj[a].append(b)
        adj[b].append(a)
        
    def get_size(node, prev):
        return 1 + sum(get_size(x, node) for x in adj[node] if x != prev)
        
    res = math.inf
    for x in range(1, n + 1):
        children_size = [get_size(child, x) for child in adj[x]]
        degree = sum(children_size)
        for c in children_size:
            dif = abs(c - (degree - c + 1))
            res = min(res, dif)
    return res
            
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))
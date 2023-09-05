# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    index = {name: i for i, name in enumerate(players)}
    for cur in callings:
        i = index[cur]
        prev = players[i-1]

        players[i], players[i-1] = players[i-1], players[i]
        index[cur] -=1
        index[prev] += 1
    
    return sorted(index.keys(), key=lambda name: index[name])
    
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
# res=  ["mumu", "kai", "mine", "soe", "poe"]
print(solution(players, callings))
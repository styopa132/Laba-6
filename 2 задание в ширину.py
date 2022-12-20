adj_list = [
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]
level = [-1] * len(adj_list)
def bfs(s):
    level[s] = 0
    ochered = [s]
    while ochered:
        v = ochered.pop(0)
        for i in adj_list[v]:
            if level[i] == -1:
                ochered.append(i)
                level[i] = level[v] + 1
for i in range(len(adj_list)):
    if level[i] == -1:
        bfs(i)
print(level[4])

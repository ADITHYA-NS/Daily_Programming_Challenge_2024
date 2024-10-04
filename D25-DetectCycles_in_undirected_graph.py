# Day 26
# Detect Cycle in a graph 
def dfs(i,adj_list,pre,visited):
    visited[i]=1
    for j in adj_list[i]:
        if visited[j]!=1:
            if dfs(j,adj_list,i,visited):
                return True
        elif j!=pre:
                return True
    return False


Edges= [[0, 1], [1, 2]]
V=3
E=2
op=False
adj_list={i:[] for i in range(V)}
for k in Edges:
    adj_list[k[0]].append(k[1])
    adj_list[k[1]].append(k[0])
visited=[0]*V
for i in range(V):
    if visited[i]!=1:
        op=dfs(i,adj_list,-1,visited)
        if op==True:
            break
if op:
    print("Cycle Present")
else:
    print("Cycle not Present")

    

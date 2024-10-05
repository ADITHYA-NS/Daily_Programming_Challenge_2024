# Day 27
# Find the shortest path in an unwieghted graph
def bfs(adj_list,V,start,end):
    distance=[V*V for i in range(V)]
    queue=[]
    queue.append([start,0])
    while queue:
        node,dis=queue.pop(0)
        if node==end:
            return dis
        for i in adj_list[node]:
            if distance[i]>dis+1:
                distance[i]=dis+1
                queue.append([i,dis+1])
    return -1

Edges = [[0, 1], [1, 2]]

V = 4
adj_list={i:[] for i in range(V)}
for j in Edges:
    adj_list[j[0]].append(j[1])
    adj_list[j[1]].append(j[0])
start=2
end=3
#print(adj_list)
print("Distance:",bfs(adj_list,V,start,end))

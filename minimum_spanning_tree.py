
# coding: utf-8

# In[ ]:

G =  {'A': [('B', 2),('C',6)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5),('A',6)]}
vertices = G.keys()
edges = []
for i in G:
    for j in G[i]:
        if i < j[0]:
            edges.append([j[1],i, j[0]])
        else:
            edges.append([j[1],j[0],i])

edges_clean = []
for i in edges:
    if not i in edges_clean:
        edges_clean.append(i)

edges_clean = sorted(edges_clean)


exsisted_vertices = []
adj = {}
count = 0
while count < len(vertices)-1:
    for i in edges_clean:
        if not (i[1] and i[2]) in exsisted_vertices:
            if i[1] in adj:
                adj[i[1]].append((i[2],i[0]))
                exsisted_vetices.append(i[1])
                exsisted_vetices.append(i[2])
                count+=1
            else:
                adj[i[1]] = [(i[2],i[0])]
                exsisted_vertices.append(i[1])
                exsisted_vertices.append(i[2])
                count+=1
                                      
        else:
            continue

out_G = {}
for i in vetices:
    out_G[i]=[]
    
for i in adj:
    out_G[i].append(adj[i][0])
    for j in adj[i]:
        out_G[j[0]].append((i,j[1]))


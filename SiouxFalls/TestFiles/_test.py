for i in range(10):
	if i==7:continue
	else:
		print(i)


quit()
import networkx as nx
import random
import time
start_time = time.time()

G=nx.complete_graph(40)
#G = nx.generators.directed.random_k_out_graph(10, 3, 0.5)

G.add_weighted_edges_from((u,v,random.random()) for u,v in nx.complete_graph(5).edges())
#print(G.edges(data=True))

#print(list(nx.all_shortest_paths(G,30,1,weight="weight")))
for i in range(4,10):
	Liste=list(nx.all_simple_paths(G,5,1, cutoff=i)) # Complexity increases exponential->use small graphs
	print(Liste)


print("--- %s seconds ---" % (time.time() - start_time))
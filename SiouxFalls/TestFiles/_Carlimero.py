import pandas as pd
import numpy as np
import re
################################################
######## Import GraphData ######################
net="SiouxFalls_net.tntp"
trips="SiouxFalls_trips.tntp"

################################################

################################################
######## Import routes #########################
################################################

#file=open(trips,"r")



################################################


################################################
######## To networkx ###########################
################################################


SF = pd.read_csv(net,comment="<",header=0, sep="\t")
SF=SF.drop(SF.columns[[0,8,9,10,11]], axis=1)
print SF

SF.to_csv("file_name.csv", sep=';')
quit()

#print AH.ix[2]

#print AH[["Tail","Head",]]
EdgeList= SF[["Tail","Head","Length (ft)"]]



############## Irgendwas mit kurzen Wegen ###########
import networkx as nx  									#works
G = nx.from_pandas_edgelist(EdgeList,"Tail","Head",edge_attr="Length (ft)",create_using=nx.DiGraph())		#works
#print nx.degree(G)							#works#
print(nx.dijkstra_path(G,300,1))
###
print(nx.bellman_ford_path(G,300,1))
###
print(nx.shortest_path(G,300,1,weight="Length (ft)"))
###
print(nx.astar_path(G,300,1))
print "\n SKRRT"
print(list(nx.all_shortest_paths(G,300,1,weight="Length (ft)")))
print "\n Burr Burr"
Liste=list(nx.all_simple_paths(G,300,1, cutoff=15))
print(Liste)
##############
df=EdgeList

ListeMitWert=[]
for i in Liste:
	Summe=0
	print "############"
	for j,nextj in zip(i,i[1:]):
		Summe=Summe+df.loc[(df['Tail'] == j) & (df["Head"]==nextj), 'Length (ft)'].item()
		#print j, nextj

	#print "Summe: ", Summe
	i.append(int(Summe))
	ListeMitWert.append(i)


A=np.array(ListeMitWert)
print A[A[:,-1].argsort()]

#print(sorted(ListeMitWert[]))


#print df.query('Tail==10 & Head==338')['Length (ft)'].astype('str')

#print df.loc[(df['Tail'] == 10) & (df["Head"]==338), 'Length (ft)'].item()
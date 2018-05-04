import numpy as np
import pandas as pd
import networkx as nx
import re
from itertools import islice


def ToPandaDF():
	df=pd.read_csv("SiouxFalls_flow.tntp", sep="\t")

	print(df)

	Total = df['Volume_Capacity '].sum()
	print(Total)

	
	SF=nx.from_pandas_edgelist(df)

text= "Origin 1"
re.findall("\d+" ,str(re.findall("Origin \d", text)))

def ExtractOrigin(str):
	return(re.findall("\d+" ,str(re.findall("Origin \d", text))))
def ExtractDestination(str):
	return([int(s) for s in str.split() if s.isdigit()])
def ExtractValue(str):
	result=re.findall("\d+\.\d",str)
	#print(result)
	result=list(map(float, result))
	return(result)

#################
def Matrix():
	import re
	x=[]
	y=[]
	z=[]
	
	trips = "SiouxFalls_trips.tntp"
	file=open(trips,"r").readlines()
	#print(file)
	#print(type(file))
	lines = iter(enumerate(file))
	for i,l in lines:
		if i<5:continue
		#print(i,l)
		if "Origin" in l:
			x.append(int(l[-4:]))
			yy=[]
			#print(int(l[-4:])) #extract Origin node
		else:
			yy.append(ExtractDestination(l))
			z.append(ExtractValue(l))

	print("ACHTUNG##############################################################")
	#print(AssignValue2Matrix(x,z))
	Test=AssignValue2Matrix(x,z)
	Matrix=np.zeros(shape=(24,24))
	h=0
	for i in range(24):
		for j in range(24):
			Matrix[i][j]=Test[h]
			h+=1
	print(Matrix)
	return(Matrix)
	


def AssignValue2Matrix(x,z):
	#Matrix=np.zeros(shape=(24,24))
	flat_list = [item for sublist in z for item in sublist]
	iterator=0
	#for i in range(23):
	#	for j in range(23):
	#		Matrix[i][j]=flat_list[i]
	#		i+=1

	return(flat_list)

#####################################################################
#####################################################################
def LoadNetwork():
	df = pd.read_csv("SiouxFalls_net.tntp",comment="<",header=0, sep="\t")
	print(df)
	print("halt stop")
	print(df.columns[1:])
	print(df.iloc[0:4,0:5])
	return(df)

def InitNetworkCosts(nw):
	nw["Actual_Flow"]=0
	print(nw)
	print(df.keys())
	nw["LinkTravelTime"]=nw["B"] * (1 + nw["Free Flow Time "] * (nw["Actual_Flow"] / nw["Capacity "]) ** nw["Power"])
	print(nw)
	return(nw)

def ShortestPath(nw, init_node, term_node):
	G = nx.from_pandas_edgelist(nw,'Init node ','Term node ',edge_attr="LinkTravelTime",create_using=nx.DiGraph())		#works
	SP=nx.shortest_path(G, source=init_node, target=term_node,  weight="Actual_Flow")
	print(f'shortest path is from {init_node} to {term_node} is: {SP} ')
	return(SP)

def UpdateNetwork(nw,SP_list):
	iterator=0
	#print(len(SP_list))
	for i in SP_list:
		iterator+=1
		#print(i)
		
		if iterator>(len(SP_list)-1):
			print("halt,stop")
			break
		else:
			i_target=SP_list[iterator]
			print(f'{i} to {i_target}')
			sheesh=nw.ix[(nw['Init node ']==i) & (nw['Term node ']==i_target)]
			nw.ix[(nw['Init node ']==i) & (nw['Term node ']==i_target), "Actual_Flow"] +=1
			print(sheesh)
			print("___")
	nw["LinkTravelTime"]=nw["B"] * (1 + nw["Free Flow Time "] * (nw["Actual_Flow"] / nw["Capacity "]) ** nw["Power"])
	#print(nw)
	return(nw)
#def testing(nw):
#	print(round(nw["B"] * (1 + nw["Free Flow Time "] * (nw["Actual_Flow"] / nw["Capacity "]) ** nw["Power"]),10))


#def UpdateNetworkLLT():
#	nw["LinkTravelTime"]=nw["Free Flow Time"] * (1 + nw["B"] * (nw["Actual_Flow"] / nw["Capacity"]) ** nw["Power"])
#	return(nw)

	#EdgeList= df[["Init Node","Term Node","Capacity"]]
	#print(EdgeList)




# ############## Irgendwas mit kurzen Wegen ###########
# import networkx as nx  									#works
# G = nx.from_pandas_edgelist(EdgeList,"Tail","Head",edge_attr="Length (ft)",create_using=nx.DiGraph())		#works
# #print nx.degree(G)							#works#
# print(nx.dijkstra_path(G,300,1))
# ###
# print(nx.bellman_ford_path(G,300,1))
# ###
# print(nx.shortest_path(G,300,1,weight="Length (ft)"))
# ###
# print(nx.astar_path(G,300,1))
# print "\n SKRRT"
# print(list(nx.all_shortest_paths(G,300,1,weight="Length (ft)")))
# print "\n Burr Burr"
# Liste=list(nx.all_simple_paths(G,300,1, cutoff=15))
# print(Liste)
# ##############
# df=EdgeList

# ListeMitWert=[]
# for i in Liste:
# 	Summe=0
# 	print "############"
# 	for j,nextj in zip(i,i[1:]):
# 		Summe=Summe+df.loc[(df['Tail'] == j) & (df["Head"]==nextj), 'Length (ft)'].item()
# 		#print j, nextj

# 	#print "Summe: ", Summe
# 	i.append(int(Summe))
# 	ListeMitWert.append(i)


# A=np.array(ListeMitWert)
# print A[A[:,-1].argsort()]

#print(sorted(ListeMitWert[]))


#print df.query('Tail==10 & Head==338')['Length (ft)'].astype('str')

#print df.loc[(df['Tail'] == 10) & (df["Head"]==338), 'Length (ft)'].item()


#####################################################################
#####################################################################
if __name__ == '__main__':
	#Matrix()
	matrix=Matrix()
			#Test=ToPandaDF()
			#print(Test)
	df=LoadNetwork()
			#CalcLTT(df)
	df=InitNetworkCosts(df) # all networks have Actual_Flow of 0 and edges have cost of C(0) (LinkTravelTime)
			#print(df.keys())
	init_node=2
	term_node=5
	ShortestPath(df, init_node, term_node)
	short=ShortestPath(df, init_node, term_node)
	print(short)
	'''
	####1kleinetest########
	start=1
	ende=9

	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	for i in range(10**3+000):
		short=ShortestPath(df, start, ende)
		df=UpdateNetwork(df,short)

	print(df)	
	
	quit()
	####1kleintest-ende####
	'''
	#df=UpdateNetwork(df,short)
	print("+++++++++++++++++")
	Zeile=0
	for i in matrix:
		print(i)
		Zeile+=1
		Spalte=0
		for j in i:
			Spalte+=1
			j=int(j)
			print(j)
			iterator=0
			while iterator<j:
				print(iterator)
				iterator+=1
				###### nun flow verteilung#######
				shorty=ShortestPath(df,Zeile,Spalte)
				print(shorty, iterator)
				df=UpdateNetwork(df,shorty)
			#print(df,file=open("output.carl","a"))		
		#break
	print(df)					#while



		#print(i)
		#print("________")
		#print(j)
	
	#print(x)
			#print(df[['Init node '==1,'Power']])
			#print("hallo")
			#print(df['Init node '])
			#print(df.dtypes)
	#y=df.ix[(df['Init node ']==1) & (df['Term node ']==3)]
	#print(y)
			# & df['Term node '] == "2" ])
			#nw["LinkTravelTime"]=nw["B"] * (1 + nw["Free Flow Time "] * (nw["Actual_Flow"] / nw["Capacity "]) ** nw["Power"])







# 	string=re.compile("~ 	Tail")
# file=open("Anaheim_net.tntp","r").readlines()
# for line in file:
# 	for match in string.findall(line):
# 		Exclusion = file.index(line)+1
# 		print Exclusion

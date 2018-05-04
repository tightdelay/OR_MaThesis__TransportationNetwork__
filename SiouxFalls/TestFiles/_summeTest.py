import numpy as np
import pandas as pd
import re
from itertools import islice


def ToPandaDF():
	df=pd.read_csv("SiouxFalls_flow.tntp", sep="\t")

	print(df)

	Total = df['Volume_Capacity '].sum()
	print (Total)

	import networkx as nx
	SF=nx.from_pandas_edgelsiet(df)

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
			
	#print(x)
	#print(z)
	#print(Matrix)
	#print(len(x))
	print("ACHTUNG##############################################################")
	#print(AssignValue2Matrix(x,z))
	Test=AssignValue2Matrix(x,z)
	Matrix=np.zeros(shape=(24,24))
	h=0
	#print(Matrix)
	#print(len(Test))
	for i in range(24):
		for j in range(24):
			Matrix[i][j]=Test[h]
			h+=1
			



	print(Matrix)
	


def AssignValue2Matrix(x,z):
	#Matrix=np.zeros(shape=(24,24))
	flat_list = [item for sublist in z for item in sublist]
	iterator=0
	#for i in range(23):
	#	for j in range(23):
	#		Matrix[i][j]=flat_list[i]
	#		i+=1

	return(flat_list)
	#print(Matrix[0][5])


		#s=l[0]
		#if "Origin" in s:


	# for l in enumerate(file):
	# 	s=l[1]
	# 	if 'Origin' in s: 
	# 		print(f'{l[1]}')
	# 		next(l)

		


		# while i<(len(file)-2):
		# 	i+=1		
		# 	if "Origin" in s:
		# 		print(r'{l[1]}, hallo')
		# 		x.append(ExtractOrigin(file[i]))
		# 		while "Origin" not in file[i]:
		# 			#print(file[i])
		# 			i+=1
		# 	else:print("nein")
		# 	y=ExtractDestination(file[i])
		# 	z=ExtractValue(file[i])
		# else:print("nah")
	#print(x)		

			#print(f'{i} ENDE {file[i]}')
				#i+=1
				#print(lines++)

	

#	for line in file:
#		liste=(line.split(";"))
#		for l in liste:
#			print(l.split(":"))
		#extracted = int(line.split(':'))#[0])
		#print(extracted)




if __name__ == '__main__':
	Matrix()
	




quit()



# 	string=re.compile("~ 	Tail")
# file=open("Anaheim_net.tntp","r").readlines()
# for line in file:
# 	for match in string.findall(line):
# 		Exclusion = file.index(line)+1
# 		print Exclusion

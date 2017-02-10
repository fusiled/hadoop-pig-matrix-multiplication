#!/bin/python

#Script that plot graphs used in the document

import csv
import numpy as np
import matplotlib.pyplot as plt


N_TEST = 10
MIN_NODES = 3
MAX_NODES = 8
tree={}

x_ar = []
ar_time = []
pig_header=["date","matrix","n_nodes","time"]
log_header=["app_id","node","time"]
pig_file = open("pig_times.txt", "r")
log_file = open("filter_log_times.csv", "r")


pig_csv = csv.DictReader(pig_file,fieldnames=pig_header,delimiter=",")
log_csv = csv.DictReader(log_file,fieldnames=log_header,delimiter=",")
for row in pig_csv:
	mat = row["matrix"]
	if(row["matrix"] not in tree.keys() ):
		tree[mat]={}
		for i in range(MIN_NODES,MAX_NODES+1):
			tree[mat][str(i)]=[]
	tree[ mat ][row["n_nodes"]].append( float(row["time"]) )


for i in range(MIN_NODES, MAX_NODES+1):
	ar_time.append(tree[mat][str(i)] )


#plt.boxplot(ar_time, 0, '')
#plt.show()
plt.savefig("boxes.pdf")
plt.clf()
x_avg=[]
avg=[]
for item in tree["m500"]:
	x_avg.append(int(item))
	avg.append(np.mean(tree["m500"][item]))

avg_sorted = sorted(avg, key=lambda elem: x_avg[avg.index(elem)])
base = avg_sorted[0]
for i in range(0,len(avg_sorted)):
	avg_sorted[i] = base/avg_sorted[i]
print(avg_sorted)
x_avg.sort()
plt.plot(x_avg,avg_sorted)
plt.show()








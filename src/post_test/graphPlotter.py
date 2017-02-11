#!/bin/python

#Script that plot graphs used in the document

import csv
import numpy as np
import matplotlib.pyplot as plt


ROOT_DIR="../../"

N_TEST = 10
MIN_NODES = 3
MAX_NODES = 8
tree={}

x_ar = []
pig_header=["date","matrix","n_nodes","time"]
log_header=["n_nodes";"matrix";"test";"job";"jobId","alias","operation","node","time"]
pig_file = open(ROOT_DIR+"log/pig_times.txt", "r")
log_file = open(ROOT_DIR+"log/pig_matrix-mul_extra-fine.csv", "r")

#pre-processing
pig_csv = csv.DictReader(pig_file,fieldnames=pig_header,delimiter=",")
log_csv = csv.DictReader(log_file,fieldnames=log_header,delimiter=";")

print("Building tree")
for row in pig_csv:
	mat = row["matrix"]
	if(row["matrix"] not in tree.keys() ):
		tree[mat]={}
		for i in range(MIN_NODES,MAX_NODES+1):
			tree[mat][str(i)]=[]
	tree[ mat ][row["n_nodes"]].append( float(row["time"]) )



#plot mean exec time
print("Plotting mean exec time")
for matrix in tree:
	ar_time=[]
	for i in range(MIN_NODES, MAX_NODES+1):
		ar_time.append(tree[matrix][str(i)] )
	plt.clf()
	plt.title("Mean Execution time "+matrix)
	plt.boxplot(ar_time, 0, '')
	plt.savefig(ROOT_DIR+"doc/img/box_"+matrix+".png")

#plot speedup
print("Plotting speedup")

#init x_axis
x_avg=[]
for item in tree["m500"]:
		x_avg.append(int(item))

avg={}
avg_sorted={}
for matrix in tree:
	avg[matrix]=[]
	for item in tree[matrix]:
		avg[matrix].append(np.mean(tree[matrix][item]))

for matrix in tree:
	avg_sorted[matrix] = sorted(avg[matrix], key=lambda elem: x_avg[avg[matrix].index(elem)])

for matrix in tree:
	base = avg_sorted[matrix][0]
	for i in range(0,len(avg_sorted)):
		avg_sorted[matrix][i] = base/avg_sorted[matrix][i]
x_avg.sort()

for matrix in tree:
	plt.clf()
	plt.title("Speedup "+matrix)
	plt.plot(x_avg,avg_sorted[matrix])
	plt.savefig(ROOT_DIR+"doc/img/speedup_"+matrix+".png")








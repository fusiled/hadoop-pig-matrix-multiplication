#!/bin/python

#Script that plot graphs used in the document

import csv
import numpy as np
import matplotlib.pyplot as plt
import copy


ROOT_DIR="../../"

N_TEST = 10
MIN_NODES = 3
MAX_NODES = 8
tree={}
nodes=[]

x_ar = []
pig_header=["date","matrix","n_nodes","time"]
log_header=["n_nodes","matrix","test","job","jobId","alias","operation","node","time"]
pig_file = open(ROOT_DIR+"log/pig_times.txt", "r")
log_file = open(ROOT_DIR+"log/pig_matrix-mul_extra-fine.csv", "r")

#pre-processing
pig_csv = csv.DictReader(pig_file,fieldnames=pig_header,delimiter=",")
log_csv = csv.DictReader(log_file,fieldnames=log_header,delimiter=";")

print("Building pig_csv tree")
for row in pig_csv:
	mat = row["matrix"]
	if(row["matrix"] not in tree.keys() ):
		tree[mat]={}
		for i in range(MIN_NODES,MAX_NODES+1):
			tree[mat][str(i)]=[]
	tree[ mat ][row["n_nodes"]].append( float(row["time"]) )

print("Building log_csv tree")
log_tree={}
for row in log_csv:
	mat=row["matrix"]
	if(row["matrix"] not in log_tree.keys() ):
		log_tree[mat]={}
		for i in range(MIN_NODES,MAX_NODES+1):
			log_tree[mat][str(i)]={}
	node_id=row["node"]
	if(node_id not in nodes):
		nodes.append(node_id)
	if(node_id not in log_tree[mat][row["n_nodes"]].keys()):
		log_tree[mat][row["n_nodes"]][node_id]={}
		log_tree[mat][row["n_nodes"]][node_id][1]=0
		log_tree[mat][row["n_nodes"]][node_id][2]=0
	else:
		log_tree[mat][row["n_nodes"]][node_id][int(row["job"])] = log_tree[mat][row["n_nodes"]][node_id][int(row["job"])] + float(row["time"])

for mat in log_tree:
	for n_nodes in log_tree[mat]:
		for node in log_tree[mat][n_nodes]:
			for job in log_tree[mat][n_nodes][node]:
				log_tree[mat][n_nodes][node][job]=log_tree[mat][n_nodes][node][job]/10

for node in nodes:
	for mat in log_tree:
		plt.clf()
		plt.title("Job time "+node+"_"+mat)
		plt.xlabel("n_workers")
		plt.ylabel("time[s]")
		plot_ar=[[None]*(MAX_NODES+1),[None]*(MAX_NODES+1)]
		for n_nodes in log_tree[mat]:
			try:
				for job in log_tree[mat][n_nodes][node]:
					plot_ar[int(job)-1][ int(n_nodes)]=log_tree[mat][n_nodes][node][job]
			except Exception: continue
		for ar in plot_ar:
			plt.plot(ar,label="job"+ str( plot_ar.index(ar)+1)+" "+mat )
		plt.legend()
		plt.savefig(ROOT_DIR+"/doc/img/job_"+node+"_"+mat+".png")

print("Plotting cumulative exec time per job")
for mat in log_tree:
	plt.clf()
	plt.title("Overlapping job time, "+mat)
	plt.xlabel("n_workers")
	plt.ylabel("time[s]")
	for node in nodes:
		plot_ar=[[None]*(MAX_NODES+1),[None]*(MAX_NODES+1)]
		for n_nodes in log_tree[mat]:
			try:
				for job in log_tree[mat][n_nodes][node]:
					plot_ar[int(job)-1][ int(n_nodes)]=log_tree[mat][n_nodes][node][job]
			except Exception: continue
		for ar in plot_ar:
			plt.plot(ar,label="job"+ str( plot_ar.index(ar)+1)+" "+mat )
		plt.savefig(ROOT_DIR+"/doc/img/global_job"+"_"+mat+".png")

#plot mean exec time with boxes
print("Plotting mean exec time")
for matrix in tree:
	ar_time=[]
	for i in range(MIN_NODES, MAX_NODES+1):
		ar_time.append(tree[matrix][str(i)] )
	plt.clf()
	plt.title("Total Execution time "+matrix)
	plt.xlabel("n_workers")
	plt.ylabel("time[s]")
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
	base = copy.deepcopy(avg_sorted[matrix][0])
	for i in range(0,len(avg_sorted[matrix])):
		avg_sorted[matrix][i] = base/avg_sorted[matrix][i]

x_avg.sort()

for matrix in tree:
	plt.clf()
	plt.title("Speed up "+matrix)
	plt.xlabel("n_workers")
	plt.plot(x_avg,avg_sorted[matrix],label="speed up "+matrix)
	plt.legend()
	plt.savefig(ROOT_DIR+"doc/img/speedup_"+matrix+".png")








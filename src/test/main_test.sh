#!/bin/bash
#init variables
matrices_dir="matrices_dir"
HDFS_MATRIX_NAME="mat1"
PIG_EXEC="matmul.pig"
HDFS_OUT_DIR="matmul_out"
output_dir="test_output"
all_time_storage="$output_dir/pig_times.txt"
time_buf_file="tmp/time_buf"
#get the number of workers
n_datanodes=`hdfs dfsadmin -report | grep Live | tr -d -c 0-9`
#do the test for every matrix in $matrices_dir
for matrix in `ls $matrices_dir`
do
	#do the test 10 times
	for iter in `seq 1 10`
	do
		#PREPARE THE ENVIRONMENT
		timestamp=`date -Iseconds`
		output_file=$output_dir/$matrix-$timestamp
		#copy test matrix ind hdfs
		hadoop fs -copyFromLocal -f $matrices_dir/$matrix $HDFS_MATRIX_NAME
		#clean old results that could be present in hdfs
		hadoop fs -rm -r -f $HDFS_OUT_DIR
		#RUN THE TEST
		#use unix time command, not the one of bash to estimate pig exec_time
		#redirect pig output in $output_file
		/usr/bin/time -f %e -o $time_buf_file pig $PIG_EXEC |& tee $output_file
		pig_time=$(cat $time_buf_file)
		#save exec_time in pig_times.txt
		echo "$timestamp,$matrix,$n_datanodes,$pig_time" >> $all_time_storage
	done
done 
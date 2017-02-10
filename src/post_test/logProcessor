#!/bin/bash

#Script that mines yarn logger.
#It computes the execution time of a job on every node. It saves the result
# at $log_times.
#

DATE_REGEX="2017-[0-1][0-9]-[0-3][0-9]\s[0-2][0-9]\:[0-5][0-9]\:[0-5][0-9]"
yarn_log_dir="yarn_logs"
pig_log_dir="pig_logs"
tmp_file="tmp.txt"
log_times="log_times.csv"

for pig_log in `ls $pig_log_dir`
do
	app_id_ar=`awk 'match($0,/[0-9]{13}_[0-9]{4}/){ print substr($0,RSTART,RLENGTH)}' ./"$pig_log_dir/$pig_log" | sort | uniq`
	for app_id in $app_id_ar
	do
		echo "Mining logs for $app_id"
		for yarn_worker_log in `ls $yarn_log_dir`
		do
			grep $app_id $yarn_log_dir/$yarn_worker_log > $tmp_file
			first_occ=`head $tmp_file -n 1`
			first_time=`echo "$first_occ" | grep -o $DATE_REGEX`
			first_time_sec=`date --date="$first_time" +%s`
			last_time=`tail $tmp_file -n 1 | grep -o $DATE_REGEX`
			last_time_sec=`date --date="$last_time" +%s`
			echo $first_time_sec
			echo $last_time_sec
			exec_time=`expr $last_time_sec - $first_time_sec`
			echo $exec_time
			echo "$app_id,$yarn_worker_log,$exec_time" >> $log_times
		done
	done
done

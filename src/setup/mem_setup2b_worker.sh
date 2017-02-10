#!/bin/bash
#CHECK Algorithm 4 WARNING
#format volume partitions 
mkfs.ext4 /dev/sdb1
mffs.ext4 /dev/sdb2
#create paths
mkdir /var/lib/hadoop-hdfs
mkdir /var/lib/hadoop-yarn
#mount the partitions
mount /dev/sdb1 /var/lib/hadoop-hdfs
mount /dev/sdb2 /var/lib/hadoop-yarn
#exit root environment
exit
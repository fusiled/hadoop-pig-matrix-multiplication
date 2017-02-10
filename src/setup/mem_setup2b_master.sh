#!/bin/bash
#CHECK Algorithm 4 WARNING
#format volume and mount it
#this partition will be used for hdfs
mkfs.ext4 /dev/sdb1
#create path
mkdir /var/lib/hadoop-hdfs
#mount the partition ath the new path
mount /dev/sdb1 /var/lib/hadoop-hdfs
#do the same for /dev/sda3 and /var/lib/hadoop-yarn
mkfs.ext4 /dev/sda3
mkdir /var/lib/hadoop-yarn
mount /dev/sda3 /var/lib/hadoop-yarn
#exit root environment
exit
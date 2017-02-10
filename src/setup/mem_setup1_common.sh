#!/bin/bash
#from PoliCloud dashboard create a volume and associate
# it to the instance
#enter root environment
sudo su -
#call cfdisk on the virtual disk of the instance
#create a partition that will become the swap (/dev/sda2)
#and one partition with the remaining space (/dev/sda3)
cfdisk /dev/sda
#call cfdisk on the volume
#for Master just create one big partition (/dev/sdb1)
#for workers create 2 paritions: 
# - 1 for yarn 28GB big (/dev/sdb1)
# - 1 for hdfs with the remaining space (/dev/sdb2)
cfdisk /dev/sdb
#reboot to detect partitions
reboot
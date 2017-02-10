#!bin/bash
#!!WARNING!!
#!! After the reboot the name of disks may be swapped:
#!! /dev/sda may become /dev/sdb and viceversa
#!! Always check this fact. If the names are swapped
#!! change the below commands where needed
#!! Now we assume that /dev/sda and /dev/sdb are the 
#!! same as the Algorithm 3, Part1
#enter root environment
sudo su -
#format swap and mount it
mkswap /dev/sda2
swapon /dev/sda2
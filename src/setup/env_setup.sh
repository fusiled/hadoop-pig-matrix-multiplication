#!/bin/bash
#enter root environment
sudo su -
#add misc epel-release
yum install epel-release unzip wget -y
#download and install cloudera repo reference 
wget -nc https://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo
mv -f cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo yum update -y
#get Oracle Java and install it 
wget -nc --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.rpm" 
yum localinstall jdk-8u121-linux-x64.rpm -y
#enable root login with centos user key 
/bin/cp -f /home/centos/.ssh/authorized_keys ~/.ssh/authorized_keys
#restart ssh deamon
service sshd restart
#disable selinux 
echo "SELINUX=disabled" > /etc/selinux/config 
echo "SELINUXTYPE=targeted" >> /etc/selinux/config 
#reboot the system
reboot
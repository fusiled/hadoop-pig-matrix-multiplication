sudo su -
/etc/init.d/iptables save
/etc/init.d/iptables stop
chkconfig iptables off
exit
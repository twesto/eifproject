# eifproject

In this project, a prometheus server and alert manager has been created.

node exporter and mysqld_exporter has been created and linked to the prometheus to send the system and SQL information.

grafana has been set up to read and display those information in 2 different dashboards

if the system (CPU, Memory and Disk) exceeds 70% percent, the alert manager will send an email to omarmukhayer99@gmail.com, notifying on the load

it will also send an email if certain number of queries a second is executed 

#!/bin/sh
sudo wget -O ~/mysql80-community-release-el7-5.noarch.rpm https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
sudo rpm -ivh ~/mysql80-community-release-el7-5.noarch.rpm
sudo yum install mysql-server -y
sudo systemctl start mysqld
sudo systemctl status mysqld
sudo systemctl enable mysqld
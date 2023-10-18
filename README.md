# Installation Guide for Mikrotik Traffic Counter
This guide will walk you through the installation process of the "mikrotik_traffic_counter_en" project on a Linux system.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- A Linux system (in this guide, we'll use CentOS with `yum` package manager).
- `git` installed on your system.
- MySQL database server.
- Python and other Python dependencies.

## Installation Steps

### 1. Install Git

```bash
sudo yum install git -y
```

### 2. Clone the Repository

```bash
sudo mkdir /etc/mikrotik_traffic_counter_en
sudo git clone https://github.com/h-haghpanah/mikrotik_traffic_counter_en /etc/mikrotik_traffic_counter_en
cd /etc/mikrotik_traffic_counter_en/installation
```

### 3. Set Execute Permissions

```bash
sudo chmod +x /etc/mikrotik_traffic_counter_en/installation/*
```

### 4. Install System Requirements

```bash
sudo ./1-install_system_requirement.sh
```

### 5. Install MySQL

```bash
sudo ./2-install_mysql.sh
```

After running the MySQL installation script, you'll receive a temporary password. Use `grep` to find it:

```bash
grep 'temporary password' /var/log/mysqld.log
```

### 6. Secure Your MySQL Installation

```bash
sudo mysql_secure_installation
```

### 7. Create a MySQL Database

Log in to MySQL as the root user:

```bash
mysql -u root -p
```

Then, create the "mikrotik" database:

```sql
CREATE DATABASE mikrotik;
exit
```

### 8. Import SQL Schema

Import the SQL schema into the "mikrotik" database:

```bash
mysql -u root -p mikrotik < /etc/mikrotik_traffic_counter_en/mikrotik.sql
```

### 9. Install Python Requirements

```bash
sudo ./3-install_python_requirement.sh
```

## Configuration

After completing the installation, you may need to configure the "mikrotik_traffic_counter_en" project as per your specific requirements. Refer to the project's documentation for further details on configuring and using the software.

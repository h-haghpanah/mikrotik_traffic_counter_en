import hashlib
from persiantools.jdatetime import JalaliDate
from flask import session
import mysql.connector
import re
from datetime import date
import gc
import report
import configparser
import os

dirname = os.path.dirname(__file__)
config = configparser.RawConfigParser()
config_path = os.path.join(dirname,"../config.ini")
config.read(config_path)


sqlhost = config.get("MySQL_Config","sqlhost")
sqluser = config.get("MySQL_Config","sqluser")
sqlpasswd= config.get("MySQL_Config","sqlpasswd")
sqldatabase = config.get("MySQL_Config","sqldatabase")
sqlaut = config.get("MySQL_Config","sqlaut")


def hashing(password):
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hashed_password




def update_user(id,fname,lname,uname,gname,password,email,role):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    if password == "••••••••": 
        mycursor.execute("UPDATE users SET first_name = '" + fname + "', last_name = '" + lname + "', email = '" + email + "', user_name = '" + uname + "', group_id = '" + gname + "', role_id = '" + role + "' WHERE user_id = " + id)
    else:
        password = hashing(password)
        mycursor.execute("UPDATE users SET first_name = '" + fname + "', last_name = '" + lname + "', email = '" + email + "', user_name = '" + uname + "', user_password = '" + password + "', group_id = '" + gname + "', role_id = '" + role + "' WHERE user_id = " + id)
    return "1"

def update_device(device_id,dname,model,ip,tname,uname,ip_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("UPDATE devices SET device_name = '" + dname + "', model = '" + model + "', type_id = '" + tname + "', user_id = '" + uname + "' WHERE device_id = " + device_id)
    # if 
    mycursor.execute("UPDATE ip SET ip_value = '" + ip + "' WHERE ip_id = " + str(ip_id[0]))
    return "1"

def update_local_range(local_range_address,local_range_regex,id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("UPDATE local_range SET  local_range_address = '" + local_range_address + "', local_range_regex = '" + local_range_regex + "' WHERE local_range_id = " + id)
    return "1"

def update_mikrotik_info(id,ip,port):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("UPDATE mikrotiks SET  mikrotik_address = '" + ip + "', mikrotik_port = '" + port + "' WHERE mikrotik_id = " + id)
    return "1"


def update_destination(id,dname,description,color):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("UPDATE destinations SET  destination_name = '" + dname + "', descriptions = '" + description + "', color_id = '" + color + "' WHERE destination_id = " + id)
    return "1"

def update_group(id,gname,description):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("UPDATE users_groups SET  group_name = '" + gname + "', description = '" + description + "' WHERE group_id = " + id)
    return "1"


def delete_user(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM users WHERE user_id = " + id)
    return "1"

def delete_device(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM devices WHERE device_id = " + id)

def delete_local_range(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM local_range WHERE local_range_id = " + id)

def delete_address(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM destination_address WHERE destination_address_id = " + id)

def delete_destination(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM destinations WHERE destination_id = " + id)

def delete_group(id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM users_groups WHERE group_id = " + id)

def add_user(fname,lname,uname,gname,password,email,role):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO users (first_name,last_name,user_name,group_id,user_password,email,role_id,mikrotik_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (fname,lname,uname,gname,password,email,role,1)
    mycursor.execute(sql,val)
    return "1"

def add_device(dname,model,type,user,ip):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    device_key = dname+"-"+model+"-"+user 
    sql = "INSERT INTO devices (device_name,model,type_id,user_id,device_key) VALUES (%s, %s, %s, %s, %s)"
    val = (dname,model,type,user,device_key)
    mycursor.execute(sql,val)
    mycursor.execute("SELECT LAST_INSERT_ID() FROM devices")
    device_id = mycursor.fetchone()
    device_id = device_id["LAST_INSERT_ID()"]
    add_ip(ip,device_id)

def add_group(gname,description):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO users_groups (group_name,description) VALUES (%s, %s)"
    val = (gname,description)
    mycursor.execute(sql,val)



def add_ip(ip,device_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO ip (ip_value,device_id) VALUES (%s, %s)"
    val = (ip,device_id)
    mycursor.execute(sql,val)


def add_local_range(local_range_address,local_range_regex):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT local_range (local_range_address,local_range_regex,local_range_name,mikrotik_id) VALUES (%s, %s, %s, %s)"
    val = (local_range_address,local_range_regex,"Local",1)
    mycursor.execute(sql,val)

def add_destination(dname,description,color):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT destinations (destination_name,descriptions,color_id) VALUES (%s, %s, %s)"
    val = (dname,description,color)
    mycursor.execute(sql,val)


def add_address(address,address_regex,destination):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    destination_key = address + "-" + destination
    sql = "INSERT destination_address (destination_address,destination_address_regex,destination_id,destination_key) VALUES (%s, %s, %s, %s)"
    val = (address,address_regex,destination,destination_key)
    mycursor.execute(sql,val)
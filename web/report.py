import hashlib
#from django.db import DataError
# from os import PRIO_USER
from persiantools.jdatetime import JalaliDate
from flask import session
import mysql.connector
import re
from datetime import date
import gc
from tools import jalali_to_gregorian,gregorian_to_jalali
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



def users_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from users join users_groups on users.group_id = users_groups.group_id join roles on users.role_id = roles.role_id order by first_name")
    result = mycursor.fetchall()
    return result

def users_list_without_other():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from users join users_groups on users.group_id = users_groups.group_id join roles on users.role_id = roles.role_id order by first_name")
    result = mycursor.fetchall()
    result_without_other = []
    for res in result:
        if res["user_name"] == "other":
            continue
        else:
            result_without_other.append(res)
            
    return result_without_other

def groups_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from users_groups order by group_name")
    result = mycursor.fetchall()
    return result

def groups_list_without_other():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from users_groups")
    result = mycursor.fetchall()
    result_without_other = []
    for res in result:
        if res["group_name"] == "Other":
            continue
        else:
            result_without_other.append(res)
            
    return result_without_other

def roles_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from roles order by role_name")
    result = mycursor.fetchall()
    return result


def user_info(user_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from users where user_id = '" + user_id + "'")
    result = mycursor.fetchone()
    return result


def destinations_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select destination_id,destination_name,descriptions,color_id from destinations")
    result = mycursor.fetchall()
    return result

def addresses_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from destination_address join destinations ON destinations.destination_id = destination_address.destination_id ORDER BY destinations.destination_name")
    result = mycursor.fetchall()
    return result

def devices_list(user_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select device_id,device_name,device_id,model,devices.type_id,type_name,devices.user_id,first_name,last_name,user_name from devices JOIN users ON devices.user_id = users.user_id JOIN device_type ON devices.type_id = device_type.type_id where devices.user_id = '" + user_id + "'")
    result = mycursor.fetchall()
    return result


def device_types():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from device_type order by type_name")
    result = mycursor.fetchall()
    return result


def mikrotik_info():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * from mikrotiks")
    result = mycursor.fetchall()
    return result



def devices_list_without_other(user_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select devices.device_id,device_name,model,devices.type_id,type_name,devices.user_id,first_name,last_name,user_name,ip_value,ip_id,device_key from devices JOIN users ON devices.user_id = users.user_id JOIN device_type ON devices.type_id = device_type.type_id LEFT JOIN ip ON ip.device_id = devices.device_id where devices.user_id = '" + user_id + "'")
    result = mycursor.fetchall()
    result_without_other = []
    for res in result:
        if res["device_name"] == "other":
            continue
        else:
            result_without_other.append(res)
            
    return result_without_other

def device_with_device_id(device_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM devices where device_id = '" + device_id + "'")
    result = mycursor.fetchone()
    return result

def local_range():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM local_range")
    result = mycursor.fetchall()
    return result

def ip_list():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT ip_value,user_name,first_name,last_name,device_name FROM ip JOIN devices ON ip.device_id = devices.device_id JOIN users ON devices.user_id = users.user_id")
    result = mycursor.fetchall()
    return result

def device_traffic():
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select download,upload,date,destination_name from traffic join ip on traffic.ip_id = ip.ip_id join destinations on traffic.destination_id = destinations.destination_id")
    result = mycursor.fetchall()

def user_traffic(date1,date2,user_id):
    result = []
    traffics = fetch_traffic(date1,date2,user_id)
    devices = devices_list(user_id)
    user = user_info(user_id)
    destinations = destinations_list()
    for device in devices:
        for destination in destinations:
            result.append({'first_name': user["first_name"], 'first_name': user["last_name"], 'user_name': user["user_name"],'destination_name' : destination["destination_name"] ,'device_name': device["device_name"] ,'device_id': device["device_id"] , 'download': 0.0 , 'upload': 0.0})
            for traffic in traffics:
                if traffic["device_id"] == device["device_id"] and traffic["destination_id"] == destination["destination_id"]:
                    result[-1]["download"] = round(float(result[-1]["download"]) + float(traffic["download"]),2)
                    result[-1]["upload"] = round(float(result[-1]["upload"]) + float(traffic["upload"]),2)
            if destinations.index(destination) == len(destinations)-1:
                result.append({'first_name': user["first_name"], 'first_name': user["last_name"], 'user_name': user["user_name"],'destination_name' : "Other" ,'device_name': device["device_name"] ,'device_id': device["device_id"] , 'download': 0.0 , 'upload': 0.0})
                for traffic in traffics:
                    if traffic["device_id"] == device["device_id"] and traffic["destination_id"] == None:
                        result[-1]["download"] = round(float(result[-1]["download"]) + float(traffic["download"]),2)
                        result[-1]["upload"] = round(float(result[-1]["upload"]) + float(traffic["upload"]),2)

    return result
                        

def traffic_by_user_device_destination(date1,date2,user_id,destination_name,device_id,device_name):
    if device_id == "all":
        traffics = user_traffic(date1,date2,user_id)
        result = {'destination_name' :  destination_name ,'download' : 0.0 ,  'upload' : 0.0}
        for traffic in traffics:
            if traffic["destination_name"] == destination_name:
                result["download"] = round((float(result["download"]) + float(traffic["download"]))/1024,2)
                result["upload"] = round((float(result["upload"]) + float(traffic["upload"]))/1024,2)
        return result
    else:
        traffics = user_traffic(date1,date2,user_id)
        result = {'device_id': device_id ,'device_name': device_name ,'destination_name' :  destination_name ,'download' : 0.0 ,  'upload' : 0.0}
        for traffic in traffics:
            if traffic["device_id"] == device_id:
                if traffic["destination_name"] == destination_name:
                    result["download"] = round((float(result["download"]) + float(traffic["download"]))/1024,2)
                    result["upload"] = round((float(result["upload"]) + float(traffic["upload"]))/1024,2)
        return result

def users_traffic_overview(date1,date2):
    users = users_list()
    destinations = destinations_list()
    other = {'destination_name' : "Other"}
    destinations.append(other)
    results = []
    for user in users:
        temp = {}
        total_download = 0
        total_upload = 0
        total = 0
        temp["user_id"] = user["user_id"]
        temp["user_name"] = user["user_name"]
        temp["first_name"] = user["first_name"]
        temp["last_name"] = user["last_name"]
        for destination in destinations:
            traffic = traffic_by_user_device_destination(date1,date2,str(user["user_id"]),destination["destination_name"],"all","all")
            temp[destination["destination_name"]] = str(round((traffic["download"])/1024,2)) + " / " + str(round((traffic["upload"])/1024,2))
            total_download = round(total_download + traffic["download"],2)
            total_upload = round(total_upload + traffic["upload"],2)
            total = round(total + traffic["download"] + traffic["upload"],2)
        temp["total"] = str(round(total_download/1024,2)) + " / " + str(round(total_upload/1024,2))
        temp["all_traffic"] = round(total/1024,2)
        results.append(temp)
    return results

def read_user_full_report(date1,date2,user_id):
    user=user_info(user_id)
    devices = devices_list(user_id)
    destination_traffic = []
    device_traffics = [] 
    destinations = destinations_list()
    other = {'destination_name' : "Other"}
    destinations.append(other)
    for device in devices:
        for destination in destinations:
            traffic = traffic_by_user_device_destination(date1,date2,user_id,destination["destination_name"],device["device_id"],device["device_name"])
            traffic["user_id"] = user["user_id"]
            traffic["user_name"] = user["user_name"]
            traffic["first_name"] = user["first_name"]
            traffic["last_name"] = user["last_name"]
            destination_traffic.append(traffic)
            traffic = {}
        device_traffics.append(destination_traffic)
        destination_traffic = []
    return  device_traffics
    
def read_all_users_full_report(date1,date2,user_id):
    if user_id == "all":
        users = users_list()
        user_traffics = []
        for user in users:
            traffic = read_user_full_report(date1,date2,str(user["user_id"]))
            user_traffics.append(traffic)
        return user_traffics
    else:
        user_traffics = []
        traffic = read_user_full_report(date1,date2,str(user_id))
        user_traffics.append(traffic)
        return user_traffics


def fetch_traffic(date1,date2,user_id):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select download,upload,date,destination_name,traffic.destination_id,ip.device_id,device_name from traffic join ip on traffic.ip_id = ip.ip_id  join devices on devices.device_id = ip.device_id join users on devices.user_id = users.user_id LEFT OUTER JOIN destinations on traffic.destination_id = destinations.destination_id where date >= '" + date1 + "' and date <= '" + date2 + "' and users.user_id = '" + user_id + "'")
    results = mycursor.fetchall()
    return results



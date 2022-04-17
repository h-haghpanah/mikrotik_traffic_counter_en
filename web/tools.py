import hashlib
from persiantools.jdatetime import JalaliDate
from flask import session
import mysql.connector
# import re
# from datetime import date
import gc
import configparser
import os
import ipcalc
import report

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

def login_check(username,password):
    mydb = mysql.connector.connect(
        host=sqlhost,
        user=sqluser,
        passwd=sqlpasswd,
        database=sqldatabase,
        auth_plugin=sqlaut,
        autocommit=True
    )
    mycursor = mydb.cursor(dictionary=True)
    hashed_password = hashing(password)
    mycursor.execute('SELECT * FROM users JOIN roles ON users.role_id = roles.role_id WHERE user_name = %s AND user_password = %s', (username, hashed_password,))
    account = mycursor.fetchone()
    if account:
        session["logged_in"] = True
        session['user_id'] = account['user_id']
        session['group_id'] = account['group_id']
        session['username'] = account['user_name']
        session['name'] = account['first_name']
        session['lastname'] = account['last_name']
        session['email'] = account['email']
        session['role'] = account['role_name_en']


    else:
        session.clear()
        gc.collect()
        session["logged_in"] = False

def jalali_to_gregorian(date):
    date = date.split("/")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    while True:
        try:
            date = JalaliDate(year,month,day).to_gregorian()
            break
        except:
            day = day -1
    return date

def gregorian_to_jalali(date):
    date = date.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    date = JalaliDate.to_jalali(year,month,day)
    return date


def ip_list(ip):
  local_range = []
  for x in ipcalc.Network(ip):
    local_range.append(str(x))
    
  return local_range

def check_ip_in_local_range(ip_input):
  local_ranges = report.local_range()
  for range in local_ranges:
        ips = ip_list(range["local_range_address"])
        for ip in ips:
              if ip == ip_input:
                    return True
  return False
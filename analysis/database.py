import mysql.connector
import re
from datetime import date
# import config
import convert
import os



###-------------------------- Connect To Database --------------------------###
if os.getenv('INDOCKER', 'False'):
  sqlhost = os.getenv('SQLHOST', 'database')
  sqluser = os.getenv('SQLUSER', 'root')
  sqlpasswd = os.getenv('SQLPASSWD', 'secret')
  sqldatabase = os.getenv('SQLDATABASE', 'mikrotik')
  sqlaut = os.getenv('SQLAUT', 'mysql_native_password')
else:
  import configparser
  dirname = os.path.dirname(__file__)
  config = configparser.RawConfigParser()
  config_path = os.path.join(dirname,"../config.ini")
  config.read(config_path)
  sqlhost = config.get("MySQL_Config","sqlhost")
  sqluser = config.get("MySQL_Config","sqluser")
  sqlpasswd= config.get("MySQL_Config","sqlpasswd")
  sqldatabase = config.get("MySQL_Config","sqldatabase")
  sqlaut = config.get("MySQL_Config","sqlaut")




mydb = mysql.connector.connect(
  host=sqlhost,
  user=sqluser,
  passwd=sqlpasswd,
  database=sqldatabase,
  auth_plugin=sqlaut,
  
)

mycursor = mydb.cursor()
###---------------------------------END-------------------------------------### 


###---------------------------- Convert Values -----------------------------###

def convert_string_to_list(string): 
    li = list(string.split(", ")) 
    return li

def convert_string_to_list2(string): 
    li = list(string.split("\n")) 
    return li

def concatenate_2_string(string1, string2):
    string3 = string1 + "-" + string2
    return string3

def concatenate_3_string(string1, string2, string3):
    string4 = string1 + "-" + string2 + "-" + string3
    return string4


def clean(value):    #Cleaning Stuff
 value = re.sub(r"\('", "", value)
 value = re.sub(r"\'\,\)", "", value)
 value = re.sub(r"\(", "", value)
 value = re.sub(r"\,\)", "", value)
 value = re.sub(r"\'", "", value)
 value = re.sub(r"\)", "", value)
 value = re.sub(r"\[", "", value)
 value = re.sub(r"\]", "", value)
 return value

def clean_for_local_ranges(value):    #Cleaning Stuff
 value = re.sub(r"^\[", "", value)
 value = re.sub(r"\(\'", "", value)
 value = re.sub(r"\\", "", value)
 value = re.sub(r"\.", "\.", value)
 value = re.sub(r"\'\,\)", "", value)
 value = re.sub(r"\]$", "", value)
 value = re.sub(r"\(", "(?:", value)
 #  value = re.sub(r"\]", "", value)
 return value

def return_user_id(user_name):
  mycursor.execute("SELECT user_id from users WHERE  user_name='" + user_name + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean(value)
  return value

def return_mikrotik_id(mikrotik_name):
  mycursor.execute("SELECT mikrotik_id from mikrotiks WHERE  mikrotik_name='" + mikrotik_name + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean(value)
  return value

def return_group_id(group_name):
  mycursor.execute("SELECT group_id from users_groups WHERE  group_name='" + group_name + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean(value)
  return value

def return_type_id(type_name):
  mycursor.execute("SELECT type_id from device_type WHERE  type_name='" + type_name + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean(value)
  return value

def return_destination_id(destination_name):
  mycursor.execute("SELECT destination_id from destinations WHERE  destination_name ='" + destination_name + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean(value)
  return value

def return_local_ranges_regex(mikrotik_id):
  mycursor.execute("SELECT local_range_regex from local_range WHERE  mikrotik_id='" + mikrotik_id + "'")
  value = mycursor.fetchall()
  value = str(value)
  value = clean_for_local_ranges(value)
  value = convert_string_to_list(value)
  return value

###---------------------------------END-------------------------------------###


###------------------------- Fetching From DataBase ------------------------###
def fetch_visited_website_count(web_key):
  mycursor.execute("select count from websites where web_key='" + web_key + "'")
  count = mycursor.fetchall()
  count = str(count)
  count = clean(count)
  if count == '':
    count = '0'
  return count


def fetch_today_traffic_upload(date, ip_id, destination_id):
  if destination_id == "None":
    destination_id = "IS NULL )"
  else:
    destination_id = "= '" + destination_id + "')"

  mycursor.execute("select upload from traffic where ( date='" + date + "' AND ip_id= " "'" + ip_id + "' AND destination_id " + destination_id )
  upload_today = mycursor.fetchall()
  upload_today = str(upload_today)
  upload_today = clean(upload_today)
  if upload_today == '':
    upload_today = '0'
  return upload_today

def fetch_today_traffic_download(date, ip_id, destination_id):

  if destination_id == "None":
   destination_id = "IS NULL )"
  else:
   destination_id = "= '" + destination_id + "')"

  mycursor.execute("select download from traffic where ( date='" + date + "' AND ip_id= " "'" + ip_id + "' AND destination_id " + destination_id )
  download_today = mycursor.fetchall()
  download_today = str(download_today)
  download_today = clean(download_today)
  if download_today == '':
    download_today = '0'
  # print(download_today)
  return download_today


def fetch_from_all_tablas(value):
     mycursor.execute("select " + value + " from devices join users on devices.user_id = users.user_id join ip on devices.device_id = ip.device_id")
     myresult = mycursor.fetchall()
     myresult = str(myresult)
     myresult = clean(myresult)
     return myresult

def fetch_from_mikrotiks(value):
   mycursor.execute("SELECT " + value + " from mikrotiks")
   value = mycursor.fetchall()
   value = str(value)
   value = clean(value)
   return value

def fetch_value_from_mikrotiks(value, value2):
   mycursor.execute("SELECT " + value + " from mikrotiks WHERE mikrotik_id = '" + value2 + "'")
   value = mycursor.fetchall()
   value = str(value)
   value = clean(value)
   return value

def fetch_device_id(value):
   mycursor.execute("SELECT device_id from devices WHERE device_name = '" + value + "'")
   value = mycursor.fetchall()
   value = str(value)
   value = clean(value)
   return value

def fetch_destination_regex():
   mycursor.execute("select destination_address_regex from destination_address join destinations on destinations.destination_id = destination_address.destination_id ORDER BY destination_number")
   myresult = mycursor.fetchall()
   myresult = str(myresult)
   myresult = clean_for_local_ranges(myresult)
   return myresult

def fetch_destination_id():
   mycursor.execute("select destination_address.destination_id from destination_address join destinations on destinations.destination_id = destination_address.destination_id ORDER BY destination_number")
   myresult = mycursor.fetchall()
   myresult = str(myresult)
   myresult = clean(myresult)
   return myresult
###---------------------------------END-------------------------------------###


###-Create User-Set IP-Add Device-Define Local Range-Add Mikrotik Functions-###


def create_user(name, lastname, email, username, password, mikrotik_name, group_name):
  mikrotik_id = return_mikrotik_id(mikrotik_name)
  group_id = return_group_id(group_name)
  sql = "INSERT INTO users (first_name, last_name, email, user_name, user_password, mikrotik_id, group_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  val = (name, lastname, email, username, password, mikrotik_id, group_id)
  mycursor.execute(sql, val)
  mydb.commit()


def set_ip(ip_value, device_name):
  device_id = fetch_device_id(device_name)
  sql = "INSERT INTO ip (ip_value, device_id) VALUES (%s, %s)"
  val = (ip_value, device_id)
  mycursor.execute(sql, val)
  mydb.commit()

def add_mikrotik(mikrotik_name, mikrotik_address, mikrotik_port, descriptions):
  sql = "INSERT INTO mikrotiks (mikrotik_name, mikrotik_address, mikrotik_port, descriptions) VALUES (%s, %s, %s, %s)"
  val = (mikrotik_name, mikrotik_address, mikrotik_port, descriptions)
  mycursor.execute(sql, val)
  mydb.commit()
  
def define_local_range(local_range_name, local_range_address, mikrotik_name):
  mikrotik_id = return_mikrotik_id(mikrotik_name)
  local_range_regex = convert.cidr_to_regex(local_range_address)
  local_range_id = concatenate_2_string(local_range_name, mikrotik_id)
  sql = "INSERT INTO local_range (local_range_name, local_range_address, local_range_regex, mikrotik_id, local_range_id) VALUES (%s, %s, %s, %s, %s)"
  val = (local_range_name, local_range_address, local_range_regex, mikrotik_id, local_range_id)
  mycursor.execute(sql, val)
  mydb.commit()


def add_device(device_name, device_model, type_name, user_name, ip_value):
   user_id = return_user_id(user_name)
   type_id = return_type_id(type_name)
   device_key =concatenate_3_string(device_name, device_model, user_id)
   sql = "INSERT INTO devices (device_name, model, type_id, user_id, device_key) VALUES (%s, %s, %s, %s, %s)"
   val = (device_name, device_model, type_id, user_id, device_key)
   mycursor.execute(sql, val)
   mydb.commit()
   set_ip(ip_value, device_name)

def add_destination(destination_name, destination_address, descriptions, color_id):
   sql = "INSERT INTO destinations (destination_name, descriptions, color_id) VALUES (%s, %s, %s)"
   val = (destination_name, descriptions, color_id)
   mycursor.execute(sql, val)
   mydb.commit()
   #destination_id = mycursor.lastrowid
   set_destination_address(destination_address, destination_name)

def set_destination_address(destination_address, destination_name):
   destination_id = return_destination_id(destination_name)
   destination_key = concatenate_2_string(destination_address, str(destination_id))
   destination_address_regex = convert.cidr_to_regex(destination_address)
   sql = "INSERT INTO destination_address (destination_address, destination_address_regex, destination_id, destination_key) VALUES (%s, %s, %s, %s)"
   val = (destination_address, destination_address_regex, destination_id, destination_key)
   mycursor.execute(sql, val)
   mydb.commit()

def add_group(group_name, descriptions):
   sql = "INSERT INTO users_groups (group_name, description) VALUES (%s, %s)"
   val = (group_name, descriptions)
   mycursor.execute(sql, val)
   mydb.commit()


###---------------------------------END-------------------------------------###


###------------------- Upload IP Traffic In Database -----------------------###
def insert_visited_web(domain,count,ip_id):
  today = date.today()
  today = str(today)
  web_key = concatenate_3_string(domain,today,str(ip_id))
  domain_count = int(count) + int(fetch_visited_website_count(web_key))
  sql = "INSERT INTO websites (web_key, domain, count, ip_id, date) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE count = '" + str(domain_count) + "'"
  val = (web_key, domain, count, ip_id, today)
  mycursor.execute(sql, val)
  mydb.commit()


def insert_traffic(download, upload, ip_id,destination_id,traffic_key):
  today = date.today()
  today = str(today)
  # traffic_key = concatenate_3_string(today, ip_id, str(destination_id))
  traffic_download = float(download) + float(fetch_today_traffic_download(today, str(ip_id), str(destination_id)))
  traffic_upload = float(upload) + float(fetch_today_traffic_upload(today, str(ip_id), str(destination_id)))
  sql = "INSERT INTO traffic (download, upload, date, ip_id, destination_id, traffic_key) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE download = '" + str(traffic_download) + "' , upload = '" + str(traffic_upload) + "'"
  val = (download, upload, today, ip_id, destination_id, traffic_key)
  mycursor.execute(sql, val)
  mydb.commit()
  


###---------------------------------END-------------------------------------###
###---------------------------------END-------------------------------------###
###---------------------------------END-------------------------------------###
###---------------------------------END-------------------------------------###
###---------------------------------END-------------------------------------###

# test = return_local_ranges_regex("1")
# test = convert_string_to_list(test)
# print(test[1])

# create_user("Other", "Other", "", "other", "other@123", "Home", "other")
# add_device("other", "other", "Other", "other", "NONE")

# #define_local_range("test16", "10.253.240.0/8", "Home")


# add_destination("Instagram", "157.240.0.0/16", "Instagram Address List", "#ffac0e")

# set_destination_address("95.161.64.0/20", "Telegram")
  



#set_ip("172.16.2.100", "18")


# insert_visited_web("www.google.com", "2", "5")
# fetch_visited_website_count("www.google.com-20")
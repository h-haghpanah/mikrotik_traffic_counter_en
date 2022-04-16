import mysql.connector
# import re
from datetime import date
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
  autocommit=True

)

mycursor = mydb.cursor(dictionary=True)
###---------------------------------END-------------------------------------###

def read_all_tables(value):
     mycursor.execute("select " + value + " from devices join users on devices.user_id = users.user_id join ip on devices.device_id = ip.device_id")
     result = mycursor.fetchall()
     return result


def read_destinations(value):
    mycursor.execute("select " + value + " from destination_address join destinations on destinations.destination_id = destination_address.destination_id ORDER BY destination_address_id")
    result = mycursor.fetchall()
    return result
def read_destination_name(value):
    mycursor.execute("select " + value + " from destinations")
    result = mycursor.fetchall()
    return result

def local_range(value):
    mycursor.execute("SELECT " + value + " from local_range")
    result = mycursor.fetchall()
    return result

def fetch_today_traffic_upload(date, ip_id, destination_id):
  if destination_id == "None":
    destination_id = "IS NULL )"
  else:
    destination_id = "= '" + destination_id + "')"

  mycursor.execute("select upload from traffic where ( date='" + date + "' AND ip_id= " "'" + ip_id + "' AND destination_id " + destination_id )
  upload_today = mycursor.fetchone()
  if upload_today == None:
    upload_today = '0'
    return float(upload_today)
  return float(upload_today['upload'])

def local_ranges():
  mycursor.execute("SELECT * from local_range")
  value = mycursor.fetchall()
  return value

def fetch_today_traffic_download(date, ip_id, destination_id):
  if destination_id == "None":
   destination_id = "IS NULL )"
  else:
   destination_id = "= '" + destination_id + "')"

  mycursor.execute("select download from traffic where ( date='" + date + "' AND ip_id= " "'" + ip_id + "' AND destination_id " + destination_id )
  download_today = mycursor.fetchone()


  if download_today == None:
    download_today = '0'
    return float(download_today)

  return float(download_today['download'])

def insert_traffic(download, upload, ip_id,destination_id):
  pass
  today = date.today()
  today = str(today)
  traffic_key = today + "-" + ip_id + "-" + str(destination_id)
  download_today =  fetch_today_traffic_download(today, ip_id, str(destination_id))
  upload_today =  fetch_today_traffic_upload(today, ip_id, str(destination_id))

  traffic_download = float(download) + download_today
  traffic_upload = float(upload) + upload_today
  sql = "INSERT INTO traffic (download, upload, date, ip_id, destination_id, traffic_key) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE download = '" + str(traffic_download) + "' , upload = '" + str(traffic_upload) + "'"
  val = (download, upload, today, ip_id, destination_id, traffic_key)
  mycursor.execute(sql, val)
  mydb.commit()


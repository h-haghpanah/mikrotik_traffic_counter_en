import mysql.connector
import re
from datetime import date
import config
import database
###-------------------------- Connect To Database --------------------------###
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="%Mysql123%",
  database="mikrotik",
)

mycursor = mydb.cursor()

###---------------------------------END-------------------------------------###
def all_users():
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload

def all_users_day(date):
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date = '" + date + "'")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date = '" + date + "'")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload
    




def specified_user_day(date, user):
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date = '" + date + "' AND user_name = '" + user + "'")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date = '" + date + "' AND user_name = '" + user + "'")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload
def all_users_month(date):
    date = "'"+ date + "-01'" + " AND LAST_DAY('" + date + "-01')" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date BETWEEN " + date )
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE date BETWEEN " + date )
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload

def specified_user_month(date, user):
    date = "'"+ date + "-01'" + " AND LAST_DAY('" + date + "-01')" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload
    

def all_users_year(date):
    date = "'"+ date + "-01-01'" + " AND LAST_DAY('" + date + "-12-31')" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " )")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " )")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload

def specified_user_year(date, user):
    date = "'"+ date + "-01-01'" + " AND LAST_DAY('" + date + "-12-31')" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload

def all_users_custom(date1, date2):
    date = "'"+ date1 + "'" + " AND '" + date2 + "'" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " )")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " )")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload

def specified_user_custom(date1, date2, user):
    date = "'"+ date1 + "'" + " AND '" + date2 + "'" 
    mycursor.execute("SELECT download FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    download = mycursor.fetchall()
    download = str(download)
    download = database.clean(download)
    download = database.convert_string_to_list(download)
    x = len(download)
    temp = 0
    for i in range(0, x):
        total_download = float(download[i]) + temp
        temp = total_download
        i += 1
    
    mycursor.execute("SELECT upload FROM devices JOIN users ON devices.user_id = users.user_id JOIN ip ON devices.device_id = ip.device_id JOIN traffic ON traffic.ip_id = ip.ip_id WHERE ( date BETWEEN " + date + " AND users.user_name = '" + user + "')")
    upload = mycursor.fetchall()
    upload = str(upload)
    upload = database.clean(upload)
    upload = database.convert_string_to_list(upload)
    y = len(upload)
    temp = 0
    for i in range(0, y):
        total_upload = float(upload[i]) + temp
        temp = total_upload
        i += 1
    return total_download, total_upload
date1 = "2020-04-24"
date2 = "2020-04-24"


traffic = [[0, 0]]
traffic = specified_user_custom(date1, date2, 'h.haghpanah')

print("--------- - ----------")
print("Download : " + str(round(traffic[[0][0]], 3)))
print("UPload   : " + str(round(traffic[[1][0]], 3)))
print("Total   : " + str(round(traffic[[0][0]], 3) + round(traffic[[1][0]], 3)))

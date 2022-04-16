# from analysis.new.database import local_range
import fetch
import address
import re
import database
import database2
import time
import datetime
# import sys
# import websites
#----------------------------------------------------------------------------#
#                                Functions                                   #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------# 
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#


def replaceusers(html, users):   # Repalacing Defined Users In HTML File And Other Local IP's with "local"
     for user in users:
         user_key = str(user["user_name"]) + "-" + str(user["device_id"]) + "-" + str(user["ip_id"]) + " "
         ip_value = str(user["ip_value"]) + " "
         html = re.sub(ip_value,user_key, html)

     local_regex = database2.local_ranges()
     for regex in local_regex:
        print(regex)
        html = re.sub(regex["local_range_regex"], "other-40-20", html)

     return html


def ignorelocals(html):  #Ignore Local Traffic 
    html = re.sub((r".*[a-z].*" + " " + r".*[a-z].*"), "LOCAL LOCAL 0 0 * *", html)
    return html

def trafficCounter(html, user):   #Count Traffic For Users
    # maxrows = 2560
    # temp2Upload = 0
    # temp2Download = 0
    date = str(datetime.datetime.today().strftime("%Y-%m-%d"))
    user_key = str(user["user_name"]) + "-" + str(user["device_id"]) + "-" + str(user["ip_id"])
    traffic = {}
    usage = []

    for item in html:
        if item != [""]:
            if item[0] == user_key:
                traffic["upload"] = round(float(item[2])/1048576,2)
                traffic["download"] = 0.00
                for destination in destinations:
                    if re.search(destination["destination_address_regex"],item[1]):
                        traffic["destination_id"] = destination["destination_id"]
                        traffic["date"] = date
                        traffic["ip_id"] = user["ip_id"]
                        traffic_key = str(date) + "-" + str(user["ip_id"]) + "-" + str(destination["destination_id"])
                        traffic["traffic_key"] = traffic_key
                        usage.append(traffic)
                        traffic = {}
                        break
                    elif destinations.index(destination) == len(destinations) - 1 :
                        traffic["destination_id"] = None
                        traffic["date"] = date
                        traffic["ip_id"] = user["ip_id"]
                        traffic_key = str(date) + "-" + str(user["ip_id"]) + "-" + "None"
                        traffic["traffic_key"] = traffic_key
                        usage.append(traffic)
                        traffic = {}
            elif item[1] == user_key:
                traffic["download"] = round(float(item[2])/1048576,2)
                traffic["upload"] = 0.00
                for destination in destinations:
                    if re.search(destination["destination_address_regex"],item[0]):
                        traffic["destination_id"] = destination["destination_id"]
                        traffic["date"] = date
                        traffic["ip_id"] = user["ip_id"]
                        traffic_key = str(date) + "-" + str(user["ip_id"]) + "-" + str(destination["destination_id"])
                        traffic["traffic_key"] = traffic_key
                        usage.append(traffic)
                        traffic = {}
                        break
                    elif destinations.index(destination) == len(destinations) - 1 :
                        traffic["destination_id"] = None
                        traffic["date"] = date
                        traffic["ip_id"] = user["ip_id"]
                        traffic_key = str(date) + "-" + str(user["ip_id"]) + "-" + "None"
                        traffic["traffic_key"] = traffic_key
                        usage.append(traffic)
                        traffic = {}
    if usage != []:
        users_traffic.append(usage)





#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------# 


while True: # Infinite Loop
    users = database2.read_all_tables("user_name,devices.device_id,ip_id,ip_value") #Username must include at least one letter
    destinations = database2.read_destinations("destination_address_regex,destination_address.destination_id,destinations.destination_id")
    users_key = []
    user_len = len(users)
    ###------------------Fetch HTML And Replace Users And Locals------------------###
    mikrotik = database.fetch_from_mikrotiks("mikrotik_id")
    mikrotik_numbers = len(mikrotik)
    html = []
    html =fetch.url(address.mikrotik("1")) #Fetch HTML Accounting for correspondig mikrotik
    # html = "149.154.10.20 172.16.1.100 1570000 1 * *\n172.16.4.118 149.154.10.20 850000 1 * *\n172.16.1.100 61.83.55.143 12990978900 1 * *\n172.16.4.118 61.83.55.142 19096755 1 * *\n172.16.4.188 1.1.1.1 1445355 1 * *\n172.16.2.121 172.16.4.127 3000 1 * *\n172.16.2.121 172.16.1.100 3000 1 * *\n"
    # html = "3.208.68.52 172.16.1.100 1570000 1 * *\n"
    html = replaceusers(html, users) #Replacing IP's with corresponding user
    html = ignorelocals(html) #Ignoring Local Traffics
    html = html.split("\n")
    for item in html:
        html[html.index(item)] = item.split(" ")




    ###-------------------- Count Traffic AND Upload to database -------------------###

    destination_length = len(destinations)
    users_traffic = []
    for user in users: 
        trafficCounter(html, user)


    # Insert To database 

    for user_traffic in users_traffic:
        for traffic in user_traffic:
            database.insert_traffic(traffic["download"], traffic["upload"], traffic["ip_id"],traffic["destination_id"],traffic["traffic_key"])


 ###------------------------------------------------------------------------------###
    time.sleep(20)


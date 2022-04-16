import fetch
import address
import re
import database
import time
import sys
import websites
#----------------------------------------------------------------------------#
#                                Functions                                   #
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------# 
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
def visited(web,user):
        temp = re.findall(r"^" + user + r".*", web, flags=re.MULTILINE)
        temp = "\n".join(temp) #Remove Extra Stuff
        temp = re.findall(r" " + r".*", temp, flags=re.MULTILINE)
        temp = "\n".join(temp)

        sites = []
        visit = []
        visit_final = []
        word = ""
        for item in temp:
            if item == "\n" and word != "":
                sites.append(word)
                word = ""
            if item != "\n" and item != " ":
                word = word + item
        count = 0
        for i in range(0,len(sites)):
            for j in range(0,len(sites)):
                if sites[i] == sites [j]:
                    count = count + 1
                    
                if j == len(sites) - 1:
                    visit.append([sites[i],count])
                    count = 0
        for k in range(0,len(visit)):
            condition = True
            for item in visit_final:
                if item == visit[k]:
                    condition = False
            if condition:
                visit_final.append(visit[k])

        return visit_final


def replaceusers(html, m):   # Repalacing Defined Users In HTML File And Other Local IP's with "local"
     i = 0
     for i in range(0, x):
         html = re.sub(ip[i] + " ", users[i] + " ", html)
         i+=1
         if i == x:
             local_regex = database.return_local_ranges_regex(m)
             length = len(local_regex)
             z = 0
             for z in range(0, length):
                html = re.sub(local_regex[z], "other-40-20", html)
                z +=1
     return html


def ignorelocals(html):  #Ignore Local Traffic 
    html = re.sub((r".*[a-z].*" + " " + r".*[a-z].*"), "LOCAL LOCAL 0 0 * *", html)
    return html

def trafficCounter(html, user):   #Count Traffic For Users
    maxrows = 2560
    temp2Upload = 0
    temp2Download = 0
    user = re.escape(user)
    userUpload = re.findall(r"^" + user + r".*", html, flags=re.MULTILINE) #Extract Upload
    userDownload = re.findall(r".*" + " " + user + r".*", html) #Extract Download
    userUpload = "\n".join(userUpload) #Remove Extra Stuff
    userDownload = "\n".join(userDownload) #Remove Extra Stuff
    destination_lenth = len(destination_address_regex) 
    destination_usage = [c[:] for c in [[0] * 2] * (destination_lenth )]
    destination_traffic = [c[:] for c in [[0] * 3] * (destination_lenth )]
    
    for w in range(0, destination_lenth): #Replace Destinations
        destination_usage[w][0] = re.findall(r"^" + destination_address_regex[w] + r".*", userDownload, flags=re.MULTILINE)
        destination_usage[w][1] = re.findall(r".*" + " " + destination_address_regex[w] + r".*", userUpload)
        destination_usage[w][0] = "\n".join(destination_usage[w][0]) #Remove Extra Stuff
        destination_usage[w][1] = "\n".join(destination_usage[w][1]) #Remove Extra Stuff
        # print(destination_usage[w][0])
        # print(destination_usage[w][1])
        w +=1

    for e in range(0, destination_lenth ): #Count Traffic per Distination
        for k in range(0, maxrows): 
            try:  #Count Upload per Distination
                temp1Upload = destination_usage[e][1].split("\n")[k].split(' ')[2] + "\n"
                temp2Upload = int(temp1Upload) + int(temp2Upload) #Count Upload
                userUpload = re.sub(r".*" + destination_address_regex[e] + r".*", "CALCULATED CALCULATE 0 0 * *", userUpload)
                
                k +=1
            except: 
                k = maxrows
    
        for o in range(0, maxrows):
            try: #Count Download per Distination
               
               temp1Download = destination_usage[e][0].split("\n")[o].split(' ')[2] + "\n"
               temp2Download = int(temp1Download) + int(temp2Download) #Count Download
               userDownload = re.sub(r".*" + destination_address_regex[e] + r".*", "CALCULATED CALCULATE 0 0 * *", userDownload)
               
               o +=1
            except:
                destination_traffic[e] = [temp2Download, temp2Upload , destination_id_list[e]]
                break

        if e == destination_lenth -1 :
           temp1Upload = 0
           temp1Download = 0
           temp2Upload = 0
           temp2Download = 0
           for q in range(0, maxrows):    #Count Other IP's traffic                        
               try:
                  temp1Upload = userUpload.split("\n")[q].split(' ')[2] + "\n"
                  temp2Upload = int(temp1Upload) + int(temp2Upload) #Count Upload
                  q +=1
               except:
                   q = maxrows

                     
           for t in range(0, maxrows):
               try:
                   temp1Download = userDownload.split("\n")[t].split(' ')[2] + "\n"
                   temp2Download = int(temp1Download) + int(temp2Download) #Count Download
                   t +=1
               except:
                #    e +=1
                   destination_traffic.append([temp2Download, temp2Upload , None])
                   return destination_traffic

        e +=1
        temp1Upload = 0
        temp1Download = 0
        temp2Upload = 0
        temp2Download = 0



#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------# 

while True: # Infinite Loop

 ###------------- Fetching User_name,IP,Device Name,User_ID List  --------------###

 users = database.fetch_from_all_tablas("user_name") # Fetch user name
 users = database.convert_string_to_list(users)
 users_temp = database.fetch_from_all_tablas("user_name") # Fetch user name For showing result
 users_temp = database.convert_string_to_list(users_temp)
 x = len(users)
#  print(users)
 destination_address_regex = database.fetch_destination_regex() # Fetch Destination Address
 destination_address_regex = database.convert_string_to_list(destination_address_regex)
 destination_id = database.fetch_destination_id()
 destination_id_list = database.convert_string_to_list(destination_id)
#  print(destination_id_list)
#  print(destination_address_regex)

 ip = database.fetch_from_all_tablas("ip_value") # Fetch IP List
 ip = database.convert_string_to_list(ip)

#  print(ip)
 device_name = database.fetch_from_all_tablas("device_name") # Fetch device name List
 device_name = database.convert_string_to_list(device_name)


 device_id = database.fetch_from_all_tablas("devices.device_id") # Fetch device id  List
 device_id = database.convert_string_to_list(device_id)
#  print(device_name)

 ip_id = database.fetch_from_all_tablas("ip_id") # Fetch ip_id
 ip_id = database.convert_string_to_list(ip_id)
#  print(ip_id)

 m = 0
 for m in range(0, x):
     users[m] = database.concatenate_3_string(users[m], device_id[m], ip_id[m]) # Convert users list to unique list of users and device


 traffic = [c[:] for c in [[0] * 3] * x] # Create three demensinals array with lenth of users
 visited_web = [g[:] for g in [[0] * 3] * x]
#  print(users)
 ###------------------Fetch HTML And Replace Users And Locals------------------###


 mikrotik = database.fetch_from_mikrotiks("mikrotik_id")
 mikrotik_numbers = len(mikrotik)
 html = []
 weblog = []
 for m in range(0, mikrotik_numbers):
    #  html.append(fetch.url(address.mikrotik(str(m + 1)))) #Fetch HTML Accounting for correspondig mikrotik
     weblog.append(websites.log())
     weblog[m] = replaceusers(weblog[m], str(m + 1))
    #  print(weblog[m])
     html.append("149.154.10.20 172.16.1.100 1570000 1 * *\n172.16.4.118 149.154.10.20 850000 1 * *\n172.16.1.100 61.83.55.143 12990978900 1 * *\n172.16.4.118 61.83.55.142 19096755 1 * *\n1.1.1.1 172.16.4.118 1445355 1 * *\n172.16.2.121 172.16.4.127 3000 1 * *\n")
     html[m] = replaceusers(html[m], str(m + 1)) #Replacing IP's with corresponding user 
     html[m] = ignorelocals(html[m]) #Ignoring Local Traffics



 ###-------------------- Count Traffic AND Upload to database -------------------###
 j = 0
 
 destination_length = len(destination_id_list)
 for j in range(0, x): 
      download = [c[:] for c in [[0] * 1] * destination_length]
      upload = [c[:] for c in [[0] * 1] * destination_length]
      destination_id_temp = [c[:] for c in [[0] * 1] * destination_length]
      traffic[j] = 0
      traffic[j] = trafficCounter(html[m], users[j])
      visited_web[j] = visited(weblog[m],users[j])
    #   print(visited_web[j])
    #   print("---------------->> " + users_temp[j] + "-" + device_name[j] +" <<----------------")
    #   print(traffic[j])

      for y in range(0, destination_length + 1):
          download = 0
          upload = 0
          destination_id_temp = 0
          download = str(round(float(traffic[j][y][0]) /1048576, 3))
          upload = str(round(float(traffic[j][y][1]) /1048576, 3))
          destination_id_temp =  traffic[j][y][2]
        #   print(download)
        #   print(upload)
        #   print(destination_id_temp)
        #   print("--------")
          y +=1
          database.insert_traffic(download, upload, ip_id[j], destination_id_temp) 
      for item in visited_web[j]:
          if item != "":
              domain = str(item[0])
              count = item[1]
              database.insert_visited_web(domain,count,ip_id[j])
    
      
      j += 1

 ###------------------------------------------------------------------------------###
 time.sleep(20)


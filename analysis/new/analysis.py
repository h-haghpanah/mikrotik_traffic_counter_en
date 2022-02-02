import database
import fetch
import re
from time import sleep

###-------------  Functions  --------------### 

def replaceusers(html,local_range_regex):   # Repalacing Defined Users In HTML File And Other Local IP's with "local"
     i = 0
     for i in range(0, user_len):
         html = re.sub(ip[i]["ip_value"] + " ", user[i] + " ", html)
         i+=1
     length = len(local_range_regex)
     z = 0
     for z in range(0, length):
        html = re.sub(local_range_regex[z]['local_range_regex'], "--><Local><--", html)
        z +=1
     return html

def ignorelocals(html):  #Ignore Local Traffic 
    html = re.sub((r".*[a-z].*" + " " + r".*[a-z].*"), "LOCAL LOCAL 0 0 * *", html)
    return html

def trafficCounter(html, user):   #Count Traffic For Users
    maxrows = 2560
    temp2Upload = 0
    temp2Download = 0
    print(user)
    user = re.escape(user)
    print(user)
    userUpload = re.findall(r"^" + user + r".*", html, flags=re.MULTILINE) #Extract Upload
    userDownload = re.findall(r".*" + " " + user + r".*", html) #Extract Download
    userUpload = "\n".join(userUpload) #Remove Extra Stuff
    userDownload = "\n".join(userDownload) #Remove Extra Stuff
    destination_lenth = len(destination_address)
    regex_length = len(destination_regex)
    destination_usage = [c[:] for c in [[0] * 2] * (regex_length)]
    destination_traffic = [c[:] for c in [[0] * 3] * (destination_lenth)]

    # print(userDownload)
    
    for w in range(0, regex_length): #Replace Destinations
        destination_usage[w][0] = re.findall(r"^" + destination_regex[w]['destination_address_regex'] + r".*", userDownload, flags=re.MULTILINE)
        destination_usage[w][1] = re.findall(r".*" + " " + destination_regex[w]['destination_address_regex'] + r".*", userUpload)
        destination_usage[w][0] = "\n".join(destination_usage[w][0]) #Remove Extra Stuff
        destination_usage[w][1] = "\n".join(destination_usage[w][1]) #Remove Extra Stuff
        # print(destination_usage[w][0])
        # print(destination_usage[w][1])
        w +=1
    # print(destination_usage)
    # print("*****************")
    for e in range(0, destination_lenth ): #Count Traffic per Distination
        for k in range(0, maxrows): 
            try:  #Count Upload per Distination
                temp1Upload = destination_usage[e][1].split("\n")[k].split(' ')[2] + "\n"
                temp2Upload = int(temp1Upload) + int(temp2Upload) #Count Upload
                userUpload = re.sub(r".*" + destination_regex[e]['destination_address_regex'] + r".*", "CALCULATED CALCULATE 0 0 * *", userUpload)
                
                k +=1
            except: 
                k = maxrows
    
        for o in range(0, maxrows):
            try: #Count Download per Distination
               
               temp1Download = destination_usage[e][0].split("\n")[o].split(' ')[2] + "\n"
               temp2Download = int(temp1Download) + int(temp2Download) #Count Download
               userDownload = re.sub(r".*" + destination_regex[e]['destination_address_regex'] + r".*", "CALCULATED CALCULATE 0 0 * *", userDownload)
               
               o +=1
            except:
                destination_traffic[e] = [temp2Download, temp2Upload , destination_id[e]]
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
                   print(destination_traffic)
                   return destination_traffic

        e +=1
        temp1Upload = 0
        temp1Download = 0
        temp2Upload = 0
        temp2Download = 0
###-------------  Initiate  --------------###

users = database.read_all_tables("user_name") #Username must include at least one letter
destination_regex = database.read_destinations("destination_address_regex")
destination_id = database.read_destinations("destination_address.destination_id")
destination_address = database.read_destination_name("destination_id")
ip = database.read_all_tables("ip_value")
device_name = database.read_all_tables("device_name")
device_id = database.read_all_tables("devices.device_id")
ip_id = database.read_all_tables("ip_id")
user_len = len(users)
user = []
for x in range(0,user_len):
    user.append(str(users[x]["user_name"]) + "-" + str(device_id[x]["device_id"]) + "-" + str(ip_id[x]["ip_id"]))


traffic = [c[:] for c in [[0] * 3] * user_len] # Create three demensinals array with lenth of users
visited_web = [g[:] for g in [[0] * 3] * user_len]

###------------------  Fetch HTML  ------------------###
mikrotik_ip = '172.16.11.1'
mikrotik_port = "8080"
html = fetch.url("http://" + mikrotik_ip + ":" + mikrotik_port + "/accounting/ip.cgi")
html = "149.154.10.20 172.16.1.100 1570000 1 * *\n149.154.10.20 172.16.1.115 850000 1 * *\n172.16.1.100 61.83.55.143 12990978900 1 * *\n34.193.10.15 172.16.1.115 19096755 1 * *\n1.1.1.1 172.16.11.118 1445355 1 * *\n172.16.12.121 172.16.4.127 3000 1 * *\n"
# weblog = []

###------------------  Analysing HTML  ------------------###

local_address_regex = database.local_range("local_range_regex") #Read Local Regex to analys html
html = replaceusers(html,local_address_regex) #Replace Local Range and user to html
html = ignorelocals(html) #ignore Local Traffic 


###-------------------- Count Traffic AND Upload to database -------------------###

destination_length = len(destination_id)

for j in range(0, user_len): 
    download = [c[:] for c in [[0] * 1] * destination_length]
    upload = [c[:] for c in [[0] * 1] * destination_length]
    destination_id_temp = [c[:] for c in [[0] * 1] * destination_length]
    traffic[j] = 0
    traffic[j] = trafficCounter(html, user[j])
    # print(traffic[j])


    # for y in range(0, destination_length+1):
    #     download = 0
    #     upload = 0
    #     destination_id_temp = 0
    #     download = str(round(float(traffic[j][y][0]) /1048576, 3))
    #     upload = str(round(float(traffic[j][y][1]) /1048576, 3))
    #     destination_id_temp =  traffic[j][y][2]
    #     y +=1
    #     # print(ip_id[j]["ip_id"])
    #     database.insert_traffic(download, upload, str(ip_id[j]["ip_id"]), destination_id_temp['destination_id']) 

    # j += 1

###------------------------------------------------------------------------------###
print(html)

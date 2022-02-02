import database





print("\n\n\n<<-------------- Welcome To Mikrotik Internet Usage Reporter ---------------->>")
print("\n   [*]For Add Mikrotik Press ----------------->  1")
print("\n   [*]Add Group Press ------------------------>  2")
print("\n   [*]For Add User Press --------------------->  3")
print("\n   [*]For Add Device Press ------------------->  4")
print("\n   [*]For Set Additional IP To Device Press -->  5")
x = input()
try:

    if x == "3":

       print("\n   First Name :")
       first_name = input()
       print("\n   last Name :")
       last_name = input()
       print("\n   Email :[Can be Empty]")
       email = input()
       print("\n   Username Name :[Must be unique with no space]")
       user_name = input()
       print("\n   Password :")
       password = input()
       print("\n   Do you Want To Add To Which Mikrotik[Exact Mikrotik Name] :")
       mikrotik_name = input()
       print("\n   Group Name :")
       group_name = input()
       database.create_user(first_name, last_name, email, user_name, password, mikrotik_name, group_name)
except:
    print("\n   Not Valid Input Please Check There Parameters : 1- Check CapsLock 2- Check Mikrotik Name and Group Exist 3- User Name Must Be Unique")


try:

    if x == "2":

       print("\n   Group Name [With No Space]:")
       group_name = input()
       print("\n   Descriptions :")
       descriptions = input()
       database.add_group(group_name, descriptions)
except:
    print("\n   Not Valid Range Of Characters")

try:

    if x == "1":

       print("\n   Mikrotik Name [With No Space And Must Be Unique]:")
       mikrotik_name = input()
       print("\n   Mikrotik IP Address[EX: 192.16.1.10 OR 172.16.11.21 ...] :")
       mikrotik_address = input()
       print("\n   Mikrotik Port :")
       mikrotik_port = input()
       print("\n   Descriptions :")
       descriptions = input()
       database.add_mikrotik(mikrotik_name, mikrotik_address, mikrotik_port, descriptions)
       
except:
    print("\n   Not Valid Range Of Characters")

try:

    if x == "4":

       print("\n   Device Name [With No Space]:")
       device_name = input()
       print("\n   Device Model :")
       device_model = input()
       print("\n   Type Name?[Accessories,Laptop,Mobile,Network,Other,PC,Server][It Is Case Sensitive]")
       type_name = input()
       print("\n   For Which User ?[Enter User Name] :")
       user_name = input()
       print("\n   IP Address ? [EX: 192.16.1.10 OR 172.16.11.21 ...] :")
       ip_address = input()
       database.add_device(device_name, device_model, type_name, user_name, ip_address)
except:
     print("\n   Not Valid Input Please Check There Parameters : 1- Check CapsLock 2- Check Username Exist")




if x == "4":

   print("\n   Device Name [With No Space]:")
   device_name = input()
   print("\n   Device Model :")
   device_model = input()
   print("\n   Type Name?[Accessories,Laptop,Mobile,Network,Other,PC,Server][It Is Case Sensitive]")
   type_name = input()
   print("\n   For Which User ?[Enter User Name] :")
   user_name = input()
   print("\n   IP Address ? [EX: 192.16.1.10 OR 172.16.11.21 ...] :")
   ip_address = input()
   database.add_device(device_name, device_model, type_name, user_name, ip_address)




try:

    if x == "5":

       print("\n   IP Address ? [EX: 192.16.1.10 OR 172.16.11.21 ...]:")
       ip_value = input()
       print("\n   Device Name [Case Sensitive] :")
       device_name = input()
       database.set_ip(ip_value, device_name)
except:
     print("\n   Not Valid Input Please Check There Parameters : 1- Check CapsLock 2- Check Username Exist")




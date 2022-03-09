from operator import add
import re
# from typing import OrderedDict
from flask import Flask,render_template,url_for,redirect,send_from_directory,session,request,jsonify,make_response
import gc
import database
from functools import wraps
from datetime import datetime
from tools import login_check,jalali_to_gregorian,gregorian_to_jalali
import report
import tools
import convert
import calendar


app = Flask(__name__)
app.config["SECRET_KEY"] = "mykey"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        session.permanent = True
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            # flash("You need to login first")
            return redirect(url_for('login'))

    return wrap

@app.route("/logout")
@login_required
def logout():
    session.clear()
    # flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('login'))

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_check(username,password)
        if session["logged_in"]:
            pass
        else:
            msg = "Incorrenct Username or Password"
            return render_template("login.html",msg=msg)

        if session["role"] == "Admin":
            return redirect(url_for("dashboard"))
        elif session["role"] == "User":
            return redirect(url_for("self_report"))
        else:
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/")
@login_required
def root():
    if session["role"] == "Admin":
        return redirect(url_for("dashboard"))
    elif session["role"] == "User":
        return redirect(url_for("self_report"))
    else:
        return redirect(url_for("dashboard"))

@app.route("/dashboard")
@login_required
def dashboard():
    if session["role"] == "Admin" or session["role"] == "Reporter":
        return render_template("dashboard.html")
    else:
        return render_template("403.html")

@app.route("/reporting")
@login_required
def reporting():
    if session["role"] == "Admin" or session["role"] == "Reporter":
        return render_template("report.html")
    else:
        return render_template("403.html")

@app.route("/self_report")
@login_required
def self_report():
    if session["role"] == "Admin" or session["role"] == "Reporter" or session["role"] == "User":
        return render_template("self_report.html")
    else:
        return render_template("403.html")

@app.route("/users")
@login_required
def users():
    if session["role"] == "Admin":
        return render_template("users.html")
    else:
        return render_template("403.html")

@app.route("/devices")
@login_required
def devices():
    if session["role"] == "Admin":
        return render_template("devices.html")
    else:
        return render_template("403.html")

@app.route("/destinations")
@login_required
def destinations():
    if session["role"] == "Admin":
        return render_template("destinations.html")
    else:
        return render_template("403.html")


@app.route("/setting")
@login_required
def setting():
    if session["role"] == "Admin":
        return render_template("setting.html")
    else:
        return render_template("403.html")

@app.route("/about")
@login_required
def about():
    return render_template("about.html")

#################### READ ######################


@app.route("/read_users_traffic", methods=["POST"])
def read_users_traffic():
    if request.method == "POST":
        event = request.form["event"]
        if event == "event":
            date1 = request.form["date1"]
            date2 = request.form["date2"]
        else:
            date2 = str(datetime.today().strftime('%Y-%m-%d'))
            temp =  date2.split("-")
            date1 = str(temp[0]) + "-" + str(temp[1]) + "-" + "01"
        if session["role"] != "User":
            result = report.read_all_users_full_report(date1,date2,"all")
        else:
            result = report.read_all_users_full_report(date1,date2,session["user_id"])
        user_table = []
        destination_usage = []
        top_ten_temp = []
        top_ten = []
        destinations = report.destinations_list()
        for dst in destinations:
            destination_usage.append({"destination" : "","color_id" : dst["color_id"],"download" : 0.00,"upload" : 0.00,"total" : 0.00})
        destination_usage.append({"destination" : "","color_id" : "#003b54","download" : 0.00,"upload" : 0.00,"total" : 0.00})
        for user in result:
            usage_temp = {"name" : "","download" : 0.00,"upload" : 0.00,"total":0.00}
            for device in user:
                for dst in device:
                    destination_usage[device.index(dst)]["destination"] = dst["destination_name"]
                    destination_usage[device.index(dst)]["total"] =  round(float(destination_usage[device.index(dst)]["total"]) + float(dst["download"]) + float(dst["upload"]),2)
                    usage_temp["name"] = dst["first_name"] +" "+ dst["last_name"]
                    usage_temp["download"] = round(usage_temp["download"] + float(dst["download"]),2)
                    usage_temp["upload"] = round(usage_temp["upload"] + float(dst["upload"]),2)
                    if user.index(device) == len(user) - 1 and device.index(dst) == len(device) -1 :
                        usage_temp["total"] = round(usage_temp["download"] + usage_temp["upload"],2)
                        user_table.append(usage_temp)
        top_ten_temp = sorted(user_table, key=lambda k: k['total'],reverse=True) 
        for item in top_ten_temp:
            top_ten.append(item)
            if top_ten_temp.index(item) == 9:
                break
            
        return jsonify([user_table,destination_usage,top_ten])
    return "0"

@app.route("/read_users", methods=["GET"])
def read_users():
    if request.method == "GET" and (session["role"] == "Admin" or session["role"] == "Reporter"):
        result = report.users_list()
        return jsonify(result)
    return "0"
    

@app.route("/read_users_without_other", methods=["GET"])
def read_users_without_other():
    if request.method == "GET" and (session["role"] == "Admin" or session["role"] == "Reporter"):
        result = report.users_list_without_other()
        return jsonify(result)
    return "0"

@app.route("/read_devices_without_other", methods=["POST"])
def read_devices_without_other():
    if request.method == "POST" and session["role"] == "Admin":
        user_id = request.form["user"]
        result = report.devices_list_without_other(user_id)
        return jsonify(result)
    return "0"

@app.route("/read_local_lan", methods=["GET"])
def read_local_lan():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.local_range()
        final = []
        for item in result:
            temp = item["local_range_address"].split("/")
            temp.append(item["local_range_id"])
            final.append(temp)

        return jsonify(final)
    return "0"

@app.route("/read_groups", methods=["GET"])
def read_groups():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.groups_list()
        return jsonify(result)
    return "0"

@app.route("/read_groups_without_other", methods=["GET"])
def read_groups_without_other():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.groups_list_without_other()
        return jsonify(result)
    return "0"

@app.route("/read_destinations", methods=["GET"])
def read_destinations():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.destinations_list()
        return jsonify(result)
    return "0"

@app.route("/read_addresses", methods=["GET"])
def read_addresses():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.addresses_list()
        return jsonify(result)
    return "0"


@app.route("/read_device_types", methods=["GET"])
def read_device_types():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.device_types()
        return jsonify(result)
    return "0"

@app.route("/read_roles", methods=["GET"])
def read_roles():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.roles_list()
        return jsonify(result)
    return "0"

@app.route("/read_users_full_report", methods=["POST"])
def read_users_full_report():
    if request.method == "POST":
        date1 = request.form["date1"]
        date2 = request.form["date2"]
        if date1 == "this_month":
            today = str(datetime.today().strftime('%Y-%m-%d'))
            temp = today.split("-")
            monthrange = calendar.monthrange(int(temp[0]),int(temp[1]))
            date1 = temp[0] + "-" + temp[1] + "-" + str(monthrange[0])
            date2 = temp[0] + "-" + temp[1] + "-" + str(monthrange[1]) 
        if session["role"] != "User":
            user_id = request.form["id"]
        else:
            user_id = session["user_id"]
        result = report.read_all_users_full_report(date1,date2,user_id)

        device_table = []
        destination_usage = []
        top_ten_temp = []
        top_ten = []
        destinations = report.destinations_list()
        for dst in destinations:
            destination_usage.append({"destination" : "","color_id" : dst["color_id"],"download" : 0.00,"upload" : 0.00,"total" : 0.00})
        destination_usage.append({"destination" : "","color_id" : "#003b54","download" : 0.00,"upload" : 0.00,"total" : 0.00})
        for user in result:
            for device in user:
                usage_temp = {"name" : "","download" : 0.00,"upload" : 0.00,"total":0.00}
                for dst in device:
                    destination_usage[device.index(dst)]["destination"] = dst["destination_name"]
                    destination_usage[device.index(dst)]["total"] =  round(float(destination_usage[device.index(dst)]["total"]) + float(dst["download"]) + float(dst["upload"]),2)
                    usage_temp["name"] = dst["device_name"]
                    usage_temp["download"] = round(usage_temp["download"] + float(dst["download"]),2)
                    usage_temp["upload"] = round(usage_temp["upload"] + float(dst["upload"]),2)
                    if device.index(dst) == len(device) -1 :
                        usage_temp["total"] = round(usage_temp["download"] + usage_temp["upload"],2)
                        device_table.append(usage_temp)
    


        return jsonify([result,destination_usage,device_table])
    return "0"


@app.route("/read_mikrotik_info", methods=["GET"])
def read_mikrotik_info():
    if request.method == "GET" and session["role"] == "Admin":
        result = report.mikrotik_info()
        return jsonify(result[0])
    return "0"

#################### UPDATE ######################


@app.route("/update_user", methods=["POST"])
def update_user():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        uname = request.form["uname"]
        gname = request.form["gname"]
        password = request.form["password"]
        email = request.form["email"]
        role = request.form["role"]
        if fname == "" or uname == "" or gname == "" or email == "":
            return "not_valid"
        users = report.users_list()
        for user in users:
            if user["user_name"] == uname and str(user["user_id"]) != str(id):
                return "user_exist"
            if user["email"] == email and str(user["user_id"]) != str(id):
                return "email_exist"
        database.update_user(id,fname,lname,uname,gname,password,email,role)
        return "1"
    return "0"


@app.route("/update_device", methods=["POST"])
def update_device():
    if request.method == "POST" and session["role"] == "Admin":
        device_id = request.form["id"]
        ip_id = [request.form["ip_id"]]
        dname = request.form["dname"]
        model = request.form["model"]
        ip = request.form["ip"]
        tname = request.form["tname"]
        uname = request.form["uname"]
        device_key = dname + "-" + model + "-" + uname
        database.update_device(device_id,dname,model,ip,tname,uname,ip_id,device_key)
        return "1"
    return "0"

@app.route("/update_local_range", methods=["POST"])
def update_local_range():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        ip = request.form["ip"]
        mask = request.form["mask"]
        local_range_address = ip+"/"+mask
        local_range_regex = convert.cidr_to_regex(local_range_address)
        local_range_regex = re.escape(local_range_regex)
        database.update_local_range(local_range_address,local_range_regex,id)

        return "1"
    return "0"

@app.route("/update_mikrotik_info", methods=["POST"])
def update_mikrotik_info():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        ip = request.form["ip"]
        port = request.form["port"]
        database.update_mikrotik_info(id,ip,port)

        return "1"
    return "0"

@app.route("/update_destination", methods=["POST"])
def update_destination():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        dname = request.form["dname"]
        description = request.form["description"]
        color = request.form["color"]
        destinations = report.destinations_list()
        for dst in destinations:
            if dst["destination_name"]  == dname and dst["destination_id"] != id:
                return "dstination_name_exist"
        database.update_destination(id,dname,description,color)

        return "1"
    return "0"
    

@app.route("/update_group", methods=["POST"])
def update_group():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        gname = request.form["gname"]
        description = request.form["description"]
        groups = report.groups_list()
        for group in groups:
            if group["group_name"]  == gname and group["group_id"] != id:
                return "group_name_exist"
            elif gname  == "دیگر":
                return "other_not_valid"

        database.update_group(id,gname,description)

        return "1"
    return "0"


#################### DELETE ######################


@app.route("/delete_user", methods=["POST"])
def delete_user():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        user = report.user_info(id)
        if user["user_name"] == "other":
            return "0"
        else:
            database.delete_user(id)
            return "1"
    return "0"

@app.route("/delete_device", methods=["POST"])
def delete_device():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        device = report.device_with_device_id(id)
        database.delete_device(id)
        return str(device["user_id"])
    return "0"

@app.route("/delete_local_range", methods=["POST"])
def delete_local_range():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        database.delete_local_range(id)
        return "1"
    return "0"

@app.route("/delete_address", methods=["POST"])
def delete_address():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        database.delete_address(id)
        return "1"
    return "0"


@app.route("/delete_destination", methods=["POST"])
def delete_destination():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        database.delete_destination(id)
        return "1"
    return "0"

@app.route("/delete_group", methods=["POST"])
def delete_group():
    if request.method == "POST" and session["role"] == "Admin":
        id = request.form["id"]
        database.delete_group(id)
        return "1"
    return "0"
#################### ADD ######################


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST" and session["role"] == "Admin":
        fname = request.form["fname"]
        lname = request.form["lname"]
        uname = request.form["uname"]
        gname = request.form["gname"]
        password = request.form["password"]
        email = request.form["email"]
        role = request.form["role"]
        if fname == "" or uname == "" or gname == "" or email == "" or role == "":
            return "not_valid"
        users = report.users_list()
        for user in users:
            if user["user_name"] == uname:
                return "user_exist"
            if user["email"] == email:
                return "email_exist"
        else:
            database.add_user(fname,lname,uname,gname,password,email,role)
            return "1"
    return "0"


@app.route("/add_group", methods=["POST"])
def add_group():
    if request.method == "POST" and session["role"] == "Admin":
        gname = request.form["gname"]
        description = request.form["description"]

  
        if gname == "":
            return "not_valid"
        groups = report.groups_list()
        for group in groups:
            if group["group_name"] == gname:
                return "group_exist"
        database.add_group(gname,description)
        return "1"
    return "0"



@app.route("/add_device", methods=["POST"])
def add_device():
    if request.method == "POST" and session["role"] == "Admin":
        dname = request.form["dname"]
        model = request.form["model"]
        type = request.form["type"]
        user = request.form["user"]
        ip = request.form["ip"]
        if dname == "" or model == "" or type == "" or user == "":
            return "not_valid"
        devices = report.devices_list_without_other(user)
        device_key = dname+"-"+model+"-"+user 
        for device in devices:
            if device["device_key"] == device_key:
                return "device_exist"

        check_ip = tools.check_ip_in_local_range(ip)
        if check_ip:
            ips = report.ip_list()
            for ipv4 in ips:
                if ipv4["ip_value"] == ip:
                    return f"IP belog to user {ipv4['user_name']} and device {ipv4['device_name']} ,you cannot register this ip."
            database.add_device(dname,model,type,user,ip)
        else:
            return "wrong_ip"

        
        return "1"
    return "0"

@app.route("/add_local_range", methods=["POST"])
def add_local_range():
    if request.method == "POST" and session["role"] == "Admin":
        ip = request.form["ip"]
        mask = request.form["mask"]
        local_range_address = ip+"/"+mask
        local_range_regex = convert.cidr_to_regex(local_range_address)
        # local_range_regex = re.escape(local_range_regex)
        database.add_local_range(local_range_address,local_range_regex)

        return "1"
    return "0"

@app.route("/add_destination", methods=["POST"])
def add_destination():
    if request.method == "POST" and session["role"] == "Admin":
        dname = request.form["dname"]
        description = request.form["description"]
        color = request.form["color"]
        destinations = report.destinations_list()
        for dst in destinations:
            if dst["destination_name"] == dname:
                return "destination_exist"
        database.add_destination(dname,description,color)

        return "1"
    return "0"


@app.route("/add_address", methods=["POST"])
def add_address():
    if request.method == "POST" and session["role"] == "Admin":
        address = request.form["ip"]
        mask = request.form["mask"]
        address = address + "/" + mask
        addresses = report.addresses_list()
        for addr in addresses:
            if addr["destination_address"] == address:
                return "address_exist"
        destination = request.form["destination"]
        address_regex = convert.cidr_to_regex(address)
        address_regex = re.escape(address_regex)
        
        
        database.add_address(address,address_regex,destination)

        return "1"
    return "0"

# Run Application

@app.route('/assets/<path:path>' , methods=['GET', 'POST'])
def send_assets(path):
    return send_from_directory('assets', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='80',debug=True)
import database
def mikrotik(mikrotik_id):
    ip = database.fetch_value_from_mikrotiks("mikrotik_address", mikrotik_id)
    port = database.fetch_value_from_mikrotiks("mikrotik_port", mikrotik_id)
    return "http://" + ip + ":" + port + "/accounting/ip.cgi"


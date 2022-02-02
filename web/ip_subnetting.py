

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

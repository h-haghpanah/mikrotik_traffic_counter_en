import ipcalc

def ip_list(ip):
  local_range = []
  for x in ipcalc.Network(ip):
    local_range.append(str(x))
    
  return local_range


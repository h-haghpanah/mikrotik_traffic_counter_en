import requests
def url(address):
    r = requests.get(address)
    return(r.text)
import pysyslog
import re
import database
def log():
    filename = "weblog.txt"
    log = ""
    # with open(filename) as f:
    #     content = f.readlines()

    # for line in content:

    #      website_query = re.findall("dns query" + r".*" , line, flags=re.MULTILINE)
    #      website_query = database.clean(str(website_query))
    #      website_query = re.sub("dns query from ", "", website_query)
    #      website_query = re.sub(": #" + r".*" + r"[0-9]\s", " ", website_query)
    #      website_query = re.sub(". A", "", website_query)
    #      if len(website_query.strip()) != 0:
    #             log = log + website_query + "\n"
    # fi = open("weblog.txt", "w")
    # fi.write("")
    # fi.close()
    return log


# print(log())






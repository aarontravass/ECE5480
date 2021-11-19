# put needed imports here
import datetime
import calendar

# read in the dns log file

file1 = open("dns_log_file.txt")
logs = file1.readlines()
file1.close()


# canonical line:
# 07-Nov-2011 00:14:19.671 queries: info: client 7.204.241.161#49698: query: smtp.usna.bluenet IN A +

def fetchDT(date_str: str):
    foo = date_str.split(" ", 2)
    dmy = foo[0].split("-", 2)
    d = dmy[0]
    mo = dmy[1]
    y = dmy[2]
    hms = foo[1].split(":", 2)
    h = hms[0]
    mi = hms[1]
    mysec = hms[2].split(".", 1)
    s = mysec[0]
    ms = mysec[1]
    return datetime.datetime(int(y), list(calendar.month_abbr).index(mo), int(d), int(h), int(mi), int(s),
                             int(ms) * 1000)


# create an empty list to hold the good records
type_A = []


def ipClean(ip_bad):
    ip_good = ip_bad.split("#")[0]
    return ip_good


# we'll check each line of the log file and filter on the records to keep
# create a for loop
# split the record based on whitespace
# determine how you are going to filter each record
# append the record to your good records list if the record passes your filter
for log in logs:
    var = log.rstrip().split(" ")
    if ("A" in var):
        type_A.append(log.rstrip())
min_rec = {"t": "", "r": ""}
max_rec = {"t": "", "r": ""}
ip_list = {}
query_list = {}
common_ip = {"count": 0, "ip": ""}
common_address = {"count": 0, "query": ""}
for log in type_A:
    var = log.split(" ")
    if (min_rec["t"] == ""):
        min_rec["t"] = fetchDT(var[0] + " " + var[1])
        min_rec["r"] = log
    if (max_rec["t"] == ""):
        max_rec["t"] = fetchDT(var[0] + " " + var[1])
        max_rec["r"] = log
    if (min_rec["t"] > fetchDT(var[0] + " " + var[1])):
        min_rec["t"] = fetchDT(var[0] + " " + var[1])
        min_rec["r"] = log
    if (max_rec["t"] < fetchDT(var[0] + " " + var[1])):
        max_rec["t"] = fetchDT(var[0] + " " + var[1])
        max_rec["r"] = log
    ip = ipClean(var[5])
    if (ip != ""):
        try:
            ip_list[ip] = ip_list[ip] + 1
        except:
            ip_list[ip] = 1
        if (ip_list[ip] > common_ip["count"]):
            common_ip = {"count": ip_list[ip], "ip": ip}
    query = var[len(var) - 4]
    try:
        query_list[query] = query_list[query] + 1
    except:
        query_list[query] = 1
    if (query_list[query] > common_address["count"]):
        common_address = {"count": query_list[query], "ip": query}


# You don't need to solve this in one big for loop -- complex code is seldom better


# 1.) Earliest record time and date
# see the calendar_time_example.py 
print("Earliest record time: " + str(min_rec["t"]) + " and record: " + min_rec["r"])
# 2.) Last record date/time
# see the calendar_time_example.py
print("Last record time: " + str(max_rec["t"]) + " and record: " + max_rec["r"])

# 3.) Total number of records
# number of elements in your good records list
print("Total number of records: ", len(type_A))
# 4.) Number of unique client  IP addresses (ignore port #)
# create a dictionary to hold your ip addresses
# find the good_record element containing the ip address and port number
# separate the ip address from the port number
# add the ip address to the dictionary as the key and increment its count as the value
print("Number of unique client IPs: ", len(ip_list.keys()))

# 5.) Number of unique query domains (ignore query IP addresses)
# do similar for the query domain
print("Number of unique Query domains: ", len(query_list.keys()))
# 6.) Most common client address  and number of occurrences
# a dictionary's keys() is a list of all the keys in the dictionary
# dict[key] refers to the value associated with key key
# you could create a for loop to look at each value for each key and find the largest value -- the
# key associated with the largest value is the most common client ip address
print("Most common client address: ", common_ip["ip"], " and count: ", common_ip["count"])

# 7.) Most common query domain and number of occurrences
# do something similar
print("Most common client query: ", common_address["ip"], " and count: ", common_address["count"])

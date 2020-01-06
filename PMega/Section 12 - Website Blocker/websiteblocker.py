import os
import time
from datetime import datetime as dt

#first we set up a path to the hosts file
#note: the r means a real string with no special characters
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #note: the r means a real string with no special characters
hosts_temp=r"F:\Google Drive\JupyterNotebooks\PMega\Section 12 - Website Blocker\hosts"

# this is where we redirect to --> it won't load in the browser
redirect = "127.0.0.1"

# set up a black list
black_list= ["www.facebook.com","www.youtube.com"]

# We only want to add these lines at certain times of day and remove itself when it's all clear
#i = 0
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours")
        with open(hosts_path,"r+") as file: # note: this means you can read AND append
            content = file.read()
            for website in black_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
                
    else:
# If outside working hours, write a new host file
        with open(hosts_path,"r+") as file:
            content = file.readlines() # this will produce a list with each line
            file.seek(0) # place the pointer before the first character of the file
            for line in content:
                if not any(website in line for website in black_list):
                    file.write(line)
            file.truncate() # truncate kills everything after the pointer
        print("Fun Hours")
        
        
    time.sleep(5) #5 seconds
#    i+= 1
    
# %cd "F:\Google Drive\JupyterNotebooks\PMega\Section 12 - Website Blocker"
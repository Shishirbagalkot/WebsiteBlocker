import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1" 
website_list = ["www.facebook.com", "facebook.com" , "https://shellshock.io/", "shellshock.io"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 14):
        print("Tika muchkond odo ley")
        with open(hosts_file, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website + "\n")
    else:
        with open(hosts_file, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Maja maadu")
    time.sleep(300)                                
import socket
import os
os.system("clear")
text = """
.___                .__  __          
|   |_____     _____|__|/  |_  ____  
|   \____ \   /  ___/  \   __\/ __ \ 
|   |  |_> >  \___ \|  ||  | \  ___/ 
|___|   __/  /____  >__||__|  \___  >
    |__|          \/              \/   

          By Xedtewqze
"""
os.system(f'echo "{text}" | lolcat')
def get_ip_address(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.error as e:
        return str(e)

def get_host_info(host):
    try:
        host_info = socket.gethostbyaddr(host)
        return host_info
    except socket.error as e:
        return str(e)

def get_provider_info(ip):
    try:
        provider_info = socket.gethostbyaddr(ip)
        return provider_info
    except socket.error as e:
        return str(e)

while True:
    choice = input("\033[1;35mEnter the host name or q to quit:\033[1;31m ")

    if choice.lower() == "q":
        break
    
    ip_address = get_ip_address(choice)
    host_info = get_host_info(choice)
    provider_info = get_provider_info(ip_address)

    print("\033[1;35mHost name:\033[1;32m", host_info[0])
    print("\033[1;35mIP address:\033[1;32m", ip_address)
    print("\033[1;35mProvider:\033[1;32m", provider_info[0])


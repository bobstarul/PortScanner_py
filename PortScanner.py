#!/usr/bin/env python3

import sys
import socket
import pyfiglet
from tqdm import tqdm

ascii_banner = pyfiglet.figlet_format("Bobster \n ")
print(ascii_banner)
print()
print("This is a Port Scanner script. \n ")
print()
ip=input("Which IP should i scan?")

lower_limit_ports=int(input("Specify the lower limit for the ports to be scanned : "))
upper_limit_ports=int(input("Specify the upper limit for the ports to be scanned : "))
if(lower_limit_ports<0):
  print("The lower limit should be a positive number")
  sys.exit()  #exit program

if(upper_limit_ports<lower_limit_ports):
  print("The upper limit should be an integer bigger than the lower limit")
  sys.exit()

open_ports =[] 

def check_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(2) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close()  #socket-ul trebuie inchis dupa ce te ai conectat la el, altfel nu mai poti crea o noua conexiune
  except Exception as e: 
    pass 
  return result


for port in tqdm(range(lower_limit_ports,upper_limit_ports+1)): 
    #print("Scanning port ", port)
    response = check_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")

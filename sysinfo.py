# ======================================================|
# Program Name: sysinfo
# Author: Rob Daglio
# Last Updated: 10_11_2019
# Descript: Simple system information gathering script
#========================================================|

#!/usr/bin/env python
import os
from platform import uname
from time import sleep

def system_info():


    criteria = ['[*] Platform: ',
		'[*] System Name: ',
        '[*] Kernel Version: ',
        '[*] Kernel Details: ',
		'[*] Architecture: ',
        '[*] Processor: ',]

    print("\n|===================| System Information |====================|\n")
	
    for index, item in enumerate(uname()):
        if item == "":
            print(f"{criteria[index]}n\\a")
        else:
            print(f"{criteria[index]}{item}")

    print("\n|=============================================================|\n")

def check_os():

    if os.name == 'posix' or os.name == 'linux':
        os.system('clear')
        sleep(1)
        system_info()
    elif os.name == ('nt'):
        os.system('cls')
        sleep(1)
        system_info()
    else:
        pass

if __name__ == '__main__':

    check_os()
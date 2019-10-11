#!/usr/bin/env python
import os, time, sys, platform

def system_info():

	criteria = ['Platform: ',
		'System Name: ',
        'Release: ',
		'Kernel Version: ',
		'Kernel Details: ',
		'Architecture: ',]

	print("\n|==============System Information===============>\n")
	for index, item in enumerate(platform.uname()):
		print(criteria[index] + item)
	print("\n|================================================>\n")

def run():

    if os.name == 'posix' or os.name == 'linux':
        os.system('clear')
        time.sleep(1)
        system_info()
    elif os.name == ('nt'):
        os.system('cls')
        time.sleep(1)
        system_info()
    else:
        pass

if __name__ == '__main__':

    run()
#!/usr/bin/python3

import sys
import time
import os
import threading

class BruteForceCracker:
    def __init__(self, Dir, F_name, error):
        self.Dir = Dir
        self.F_name = F_name
        self.error = error
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)
    
def password_cracker(Dir,F_name):
    
    os.chdir(Dir)
    stm_2 = 'cat '+F_name
    os.system(stm_2)
    
    #proceed_ask = input("Do you wish to bruteforce the file?")
    
def main():
    Dir = input("Enter the Directory")
    F_name = input("Enter Filename: ")  
    error = input("Enter Wrong Password Error Message: ")
    cracker = BruteForceCracker(Dir, F_name, error)
    password_cracker(Dir,F_name)
    #passw()
    
def passw():
    os.chdir('/home/alex/Documents/Hacking')
    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        #while True:
            #passwords = f.readlines(chunk_size)
            #if not passwords:
            #    break

if __name__ == '__main__':
    banner = "Loading...\n"
    print(banner)
    main()

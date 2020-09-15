import os
import sys
import logging
from datetime import datetime
import argparse
import subprocess
from config import *
#-----------------------------
# XentInterpret 2.0.0
# copyright 2020, 17lwinn

parser = argparse.ArgumentParser(prog='python3 main.py', description='XenText... remastered')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0', help='view the CLI version')
parser.add_argument('-r', '--run', metavar='<script/path>', help='Run your XenText scripts');

if EXPERIMENTAL_MODE == "true":
    parser.add_argument('-i', '--install', metavar='<package>', help='Install Xent plugins to extend your experience');
    parser.add_argument('-s', '--search', metavar='<package>', help='search for Xent plugins to extend your experience');

args = parser.parse_args()

if args.run:
  if DISABLE_SCRIPT_EXECUTION == "false":
    scriptname = args.run
    os.system("python3  " + PARSER_LOCATION + scriptname)
    exit()
  if DISABLE_SCRIPT_EXECUTION == "true":
    print("Remote script execution has been disabled, please change DISABLE_SCRIPT_EXECUTION to false")
    print("")
    
if args.install:
  packageinstall = args.install
  os.system("svn checkout https://github.com/ProTech-IT-Solutions/xentext-addon-registry/trunk/" + packageinstall)
  exit()

if args.search:
  packagesearch = args.search
  os.system("curl -s -L https://raw.githubusercontent.com/ProTech-IT-Solutions/xentext-addon-registry/master/" + packagesearch + "/info.py | python")
  exit()
print("XenText interpreter " + INTERPRETER_VERSION)

print("type xenText code here and type run() to execute")
print("or exit() to exit the interpreter")
def main():
  while True:
    cliprompt()
        
def cliprompt():
            

      code = input(">>> ")
      
      if code == "run()":
        run()
        return
      
      
      if code == "forcerun()":
        forcerun()
        return
      
      if code == "exit()":
        exit()
        
      f = open(".temp.xt", "a")
      f.write(code + "\n")
      f.close()
      
      if code == "moomoo()":
        moomoo()


def run():
  file = ".temp.xt"
  try:
    os.system("python3 xent.py " + file)
    os.remove(".temp.xt")
  except:
    print("An error occured while evaluating the code!")

def forcerun():
  file = ".temp.xt"
  try:
    os.system("python3 xent.py " + file)
  except:
    print("An error occured while evaluating the code!")


def exit():
  try:
    os.unlink(".temp.xt")
  except:
    0
  finally:
    print("exiting...")
    sys.exit()

def moomoo():
  os.unlink(".temp.xt")
  print('\|/          (__)    ')
  print('     `\------(oo)    ')
  print('       ||    (__)    ')
  print('       ||w--||    \|/')



if __name__ == '__main__': 
  main()

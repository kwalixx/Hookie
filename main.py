# Code contain args parse func 
# and calling hookie.py func
from colorama import Fore, init
import banner
import hookie
init(autoreset=True)

def main():
  banner.banner() # Header
  hooker = hookie.Hookie()
  print("Test")
  return 0
 
if __name__ == '__main__':
  main()

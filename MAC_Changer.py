import subprocess
from colored import bg,fg,attr
red = fg("red")
reset = attr("reset")
green = fg("green")
author = "**Coded by N4kb4**\n\n"
space = author.center(100) 
def intro():
  print (green + """
##     ##    ###     ######      ######  ##     ##    ###    ##    ##  ######   ######## ########  
###   ###   ## ##   ##    ##    ##    ## ##     ##   ## ##   ###   ## ##    ##  ##       ##     ## 
#### ####  ##   ##  ##          ##       ##     ##  ##   ##  ####  ## ##        ##       ##     ## 
## ### ## ##     ## ##          ##       ######### ##     ## ## ## ## ##   #### ######   ########  
##     ## ######### ##          ##       ##     ## ######### ##  #### ##    ##  ##       ##   ##   
##     ## ##     ## ##    ##    ##    ## ##     ## ##     ## ##   ### ##    ##  ##       ##    ##  
##     ## ##     ##  ######      ######  ##     ## ##     ## ##    ##  ######   ######## ##     ## 
\n""" + red + space)

  
def mac(interface , new_mac):

  
  subprocess.call(["ifconfig", interface , "down"])
  subprocess.call(["ifconfig", interface , "hw", "ether", new_mac])
  print("Your MAC Adress has been changed to", new_mac)

intro()
interface = raw_input(green + "[+] Enter an interface >>" + reset)
new_mac = raw_input (green + "[+] Enter a MAC Address >>" + reset)

mac(interface , new_mac)

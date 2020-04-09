print("              MAC CHANGER\n""             by N4KB@ \n\n"
      "Instagaram:https://www.instagram.com/hackersarena0/\n")

import subprocess



interface = raw_input("Enter an interface >")
new_mac = raw_input ("Enter a MAC Address >")
subprocess.call(["ifconfig", interface , "down"])
subprocess.call(["ifconfig", interface , "hw", "ether", new_mac])
print("Your MAC Adress has been changed to", new_mac)
# will make this a bash script

import os 

# import python reqs
os.system("pip3 install -r requirments.txt")

# download geckodriver
os.system("chmod +x NotiPyer/get_gecko.sh")
os.system("./NotiPyer/get_gecko.sh")

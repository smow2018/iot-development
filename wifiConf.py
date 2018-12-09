#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an run script of SMOW software.                                                   *#
#* The script first checks if the raspberry has already a network connection                          *#
#* If it exists, is will start the software                                                           *#
#* If not, it asks from user to enter the network credentials and add it in wpa_supplicant.conf file  *#
#*                                                                                                    *#
#* 09/12/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#
import os
import sys
import urllib2

# This class is used to add network credentials in raspberry con file.
# First it checks wether network exists
# If exists, it exits
# If it does not exist:
#   - asks from user if he wants to enter credentials
#   - edits wpa_suoolicant.conf file
#   - restarts the pi
class Wifi:
  # initializes class
  def __init__(self):
    self.name = ""
    self.password = ""
    self.hasValidName = False
    self.hasValidPassword = False

  # check internet connection
  # return True if google page is responging
  # False eitherwise
  def isInternetActive(self):
    try:
      urllib2.urlopen('http://google.com', timeout=1)
      return True
    except urllib2.URLError as err:
      return False

  # store the wifi name
  def getName(self):
    self.name = self.getValue("Enter wifi name: ", False)

  # store the wifi password
  def getPassword(self):
    self.password = self.getValue("Enter wifi password: ", False)
  
  # reads the value entered by users, and excepted
  # returns the accepted value (string)
  def getValue(self, strMessage, bHasValue):
    while not bHasValue:
      strValue = raw_input(strMessage)
      print 'You entered', strValue
      bAcceptValue = raw_input("are you sure(Y/N)?")
      if bAcceptValue == 'y' or bAcceptValue == 'Y':
        bHasValue = True
    return strValue

  # adds the network credentials to the pi's conf file
  # first checks if the file exists
  # returns True if file updated successfully
  # False if there was an error or file did not exist
  def addNetwork(self):
    bFileExists = os.path.isfile("/etc/wpa_supplicant/wpa_supplicant.conf")
    if not bFileExists:
      return False
    else:
      try:
        f = open("/etc/wpa_supplicant/wpa_supplicant.conf", "a")
        f.write("\n")
        f.write("network={\n")
        ssid =  "        ssid=\"" + self.name + "\"\n"
        f.write(ssid)
        psk =   "        psk=\"" + self.password + "\"\n"
        f.write(psk)
        f.write("        key_mgmt=WPA-PSK\n")
        f.write("}\n")
        return True
      except:
        return False

# main function
if __name__ == '__main__':
  # fist we need to check if network already connected
  # if yes we just need to exit
  # if no, we have to ask user if he wishes to add network
  # in case he selects no, we have to inform him that some smow features wont be available without connection
  wifi = Wifi()
  # check if pi has already network
  bIsInternetActive = wifi.isInternetActive()
  if not bIsInternetActive:
    print ("SMOW has no internet connection")
    bExit = False
    while not bExit:
      strAddNetwork = raw_input("Do you want to configure a network?(Y/N)")
      if strAddNetwork  == 'y' or strAddNetwork == 'Y':
        # get name
        wifi.getName()
        print "Wifi is",  wifi.name
        # get password
        wifi.getPassword()
        print "wifi Password is", wifi.password
        # write to wpa_supplicant.conf
        bNetworkAdded = wifi.addNetwork()
        if bNetworkAdded:
          print("Network added, smow has to restart")
          os.system("sudo reboot")
        else:
          print("Something went wrong. Be sure you added the network credentials correctly")
          bExit = False
      else:
        print("Without internet connection some SMOW's features will not be available")
        goWithNoNetwork = raw_input("Do you want to continue with no network?(Y/N)")
        if goWithNoNetwork == 'Y' or goWithNoNetwork == 'y':
          bExit = True
          break
        else:
          bExit = False
  else:
    print("Network connection is already active, continue with SMOW configuration")

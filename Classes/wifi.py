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
# checks whether network exists
# adds new network credentials
# edits wpa_suoolicant.conf file

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

# End of class __Wifi__

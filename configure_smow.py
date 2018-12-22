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
import sys
import time

sys.path.insert(0,'/home/pi/iot-development/Classes')
from wifi import Wifi
from rotate import *
from location import Location
from smowFeatures import Features

# fist we need to check if network already connected
# if yes we just need to exit
# if no, we have to ask user if he wishes to add network
# in case he selects no, we have to inform him that some smow features wont be available without connection
def updateNetwork():
  bUpdated = False
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
          bUpdated = True
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
  return bUpdated

# rotate SMOW
# First it asks from user whether he wants to change orientation
# If no, it exits
# If yes
# -retrieves info from config file
# -replaces orientation value
def updateRotate():
  bUpdated = False
  pi = Rotate()
  #get current orientation
  currentOrientation = pi.getStrCurrentOrientation()
  print 'SMOW has ' + currentOrientation + ' orientation'
  strChange = raw_input("Do you want to change(Y/N)")
  if strChange == 'y' or strChange == 'Y':
    bValidResponse = False
    while not bValidResponse:
      print ''
      print 'Please select new orientation :'
      print 'PORTRAIT              :0'
      print 'LANDSCAPE RIGHT       :1'
      print 'PORTRAIT UPSIDE DOWN  :2'
      print 'LANDSCAPE LEFT        :3'
      selection = raw_input()
      if selection != '0' and selection != '1' and selection != '2' and selection != '3':
        print 'Please select number between 0-3'
      else:
        bValidResponse = True

    bUpdated = pi.setOrientation(selection)
    if bUpdated:
      # get current orientation
      currentOrientation = pi.getStrCurrentOrientation ()
      print 'Orientation changed to ' + currentOrientation + '.SMOW needs to restart'
    else:
      print 'Something went wrong, orientation did not update'
  return bUpdated

def enableWeatherFeature():
  #first retrieve current location
  location = Location()
  features = Features ()
  bLocationFound = location.getCurrentLocation()
  bLocationIDFound = location.getLocationCode()
  if bLocationFound and bLocationIDFound:
    # add location to config.js file
    bResult = features.addCityForCurrentWeather(location)
    if bResult:
      print 'SMOW detected ' + location.city + '-' + location.country + ' as current location'
      print 'With location Id: ' + location.id
    else:
      print 'Something went wrong, current weather was not enabled'

#main function
# Check first for internet connection
bNetworkUpdated = updateNetwork ()
print " "
bOrientationUpdated = updateRotate ()
if bNetworkUpdated or bOrientationUpdated:
  print 'SMOW NEEDS TO RESTART SMOW'
  print 'RESTARTING SMOW....'
  time.sleep(4)
  os.system('sudo reboot')

print " "
#enable current weather feature
enableWeatherFeature()



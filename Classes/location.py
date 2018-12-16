#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an run script of SMOW software.                                                   *#
#* The script sets the current location of SMOW users                                                 *#
#* Then replaces the value in config.json file                                                        *#
#*                                                                                                    *#
#*                                                                                                    *#
#* 11/12/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#
import os
import sys
import requests
import json

# This class is used to retrieve current location information
class Location:
  #initializes class
  def __init__(self):
    self.country = ""
    self.country_code = ""
    self.region = ""
    self.region_code = ""
    self.city = ""
    self.cityListPath = "/home/pi/iot-development/configuration_files/city.list.json"
    self.id = ""
  
  # Retrieves the current location
  def getCurrentLocation (self):
    try:
      url = "http://api.ipstack.com/check?access_key=7b176711dd6030389f32cd398d0220ab"
      req = requests.get(url)
      res = json.loads(req.text)
      self.country = res['country_name']
      self.country_code = res['country_code']
      self.region = res['region_name']
      self.region_code = res['region_code']
      self.city = res['city']
      return True
    except:
      print 'Something went wrong with retrieving current location'
      print 'Check internet connection'
      return False

  # Retrieves location code from city.list.json
  def getLocationCode (self):
    bFileFound = os.path.isfile(self.cityListPath)
    if bFileFound:
      try:
        inFile = open(self.cityListPath, 'r')
        strSearchCountry = '    \"country\": \"' + self.country_code +'\",\n'
        strSearchCity =    '    \"name\": \"'  + self.city + '\",\n' 
        lineList = inFile.readlines()
        uiIndex = 0
        for line in lineList:
          if line == strSearchCity.encode('utf-8') and lineList[uiIndex+1] == strSearchCountry.encode('utf-8'):
            self.id = str(lineList[uiIndex-1][10:-2])
            return True
          uiIndex = uiIndex + 1
        return False
      except:
        print "Something went wrong while reading " + self.cityListPath
        return False
    else:
      print "File" + self.cityListPath + "not found"
      return False

# end of class __Location__

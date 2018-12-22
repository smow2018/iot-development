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
from location import Location

# This class i used to configure SMOW modules
class Features: 
  #Initialize class
  def __init__(self):
    self.filePath = "/home/pi/iot-development/configuration_files/config.js.sample"

  # Adds current city to config.js file for weather modules
  # currentweather and weatherforecast
  def addCityForWeatherModule(self, location, strSearch):
    #read config file
    bFileFound = os.path.isfile(self.filePath)
    if bFileFound:
      try:
        inFile = open(self.filePath, 'r')
        strReplaceHeader = '\t\t\theader: \"' + location.city + ' - ' + location.country + '\",\n'
        strReplaceLocation = '\t\t\t\tlocation: \"' + location.city + '\",\n'
        strReplaceLocationID = '\t\t\t\tlocationID: \"' + location.id + '\",\n'
        lineList = inFile.readlines()
        uiIndex = 0
        for line in lineList:
          if line == strSearch:
            lineList[uiIndex+2] = strReplaceHeader
            lineList[uiIndex+4] = strReplaceLocation
            lineList[uiIndex+5] = strReplaceLocationID
            break
          uiIndex = uiIndex + 1
        inFile.close()
        outFile = open(self.filePath, 'w')
        outFile.writelines(lineList)
        outFile.close()
        return True
      except:
        print "Something went wrong with " + self.filePath
        return False
    else:
      print self.filePath + "not found"
      return False


  # Adds current city to config.js file for currentweather module
  def addCityForCurrentWeather(self, location):
    #read config file
    strSearch = '\t\t\tmodule: \"currentweather\",\n'
    bCurrentWeatherEnabled = self.addCityForWeatherModule(location, strSearch)
    return bCurrentWeatherEnabled

  # Adds current city to config.js file for weather forecast module
  def addCityForWeatherForecast(self, location):
    #read config file
    strSearch = '\t\t\tmodule: \"weatherforecast\",\n'
    bForecastEnabled = self.addCityForWeatherModule(location, strSearch)
    return bForecastEnabled

# end of class __Features__

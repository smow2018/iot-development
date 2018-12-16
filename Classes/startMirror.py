#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an run script of SMOW software.                                                   *#
#* The script first checks if the MagicMirror open source already has a config.js file                *#
#* If it exists, is will start the software                                                           *#
#* If not, config.js should be created                                                                *#
#*                                                                                                    *#
#* 30/11/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#

import os
import subprocess
import shutil

# This class is used to start magic mirror open source software in Raspberry pi current directory
# checks whether config.js exists
# starts the software by running nmp start
# configures config.js file

class Mirror:
    
  # initialises object
  def __init__(self):
    # The repository that Magic Mirror open source is located 
    self.magicMirrorDir = "/home/pi/iot-development/MagicMirror"
    
  # check if file exists
  def isFileExist (self, strFilePath):
    print ("Checking if " + strFilePath + " exists....")
    if os.path.isfile(strFilePath):
      return True
    else:
      return False
  
  # starts magic mirror software by executing npm start
  # First it checks if config.js file exists
  # If it exists, starts magic mirror
  # If not it renames config.js.sample to config.js
  def start (self):
    strConfigFileSample = "/home/pi/iot-development/configuration_files/config.js.sample"
    strConfigFile = "/home/pi/iot-development/MagicMirror/config/config.js"
    if self.isFileExist(strConfigFileSample):
      #rename it to config.js
      self.renameFile(strConfigFileSample, strConfigFile)
      
    if self.isFileExist(strConfigFile):
      os.chdir(self.magicMirrorDir)
      subprocess.check_call('npm start', shell=True)
      
  # renames a filename    
  def renameFile(self, sourceFile, targetFile):
    shutil.move(sourceFile, targetFile)
    
        
# main function	
if __name__ == '__main__':
  # init an object
  mirror = Mirror()
  mirror.start()
	
  

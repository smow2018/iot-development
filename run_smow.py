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
# First it checks wether config.js exists
# If exists, it simply starts the software by running nmp start
# If it does not exist:
#   - configures config.js file
#   - runs npm starts
class StartMirror:
    
  # initialises object
  def __init__(self):
    # The repository that Magic Mirror open source is located 
    self.magicMirrorDir = "/home/pi/iot-development-master/MagicMirror"
    
  # check if file exists
  def isFileExist (self, strFilePath):
    print ("Checking if " + strFilePath + " exists....")
    if os.path.isfile(strFilePath):
      return True
    else:
      return False
  
  # starts magic mirror software by executing npm start
  # First it checks if condig.js file exists
  # If it exists, starts magic mirror
  # If not it renames config.js.sample to config.js
  # If not even a config sample file exists, print an error
  def start (self):
    strConfigFileSample = "MagicMirror/config/config.js.sample"
    strConfigFile = "MagicMirror/config/config.js"
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
  objMagicMirror = StartMirror()
  objMagicMirror.start()
	
  
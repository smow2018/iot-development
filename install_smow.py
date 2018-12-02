#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an installation script of SMOW software.                                          *#
#* The script first checks if the MagicMirror open source already exists in the current directory     *#
#* If not, Magic Mirror 2 should be cloned from github repository                                     *#
#*                                                                                                    *#
#* 30/11/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#

import os
import subprocess
import shutil

# This class is used to install magic mirror open source software in Raspberry pi current directory
# First it checks wether Magic Mirror folder exists
# If exists, it simply prints a message and exits
# If it does not exist:
#   - it downloads the required software from the repository
#   - it installs the software
#   - configures config.js file
class InitMirror:
    
  # initialises object
  def __init__(self):
    # The repository that Magic Mirror open source is located 
    self.magicMirrorDir = "/home/pi/iot-development/MagicMirror"
  # checks if mirror is downloaded
  # returns true if installed, false eitherwise
  
  def isMirrorDownloaded (self):
    # Check if Magic Mirror is already downloaded
    print ("Detecting SMOW......")
    print ("Check for previous installations")
    if os.path.isdir("MagicMirror"):
      return True
    else:
      return False
	  
  # installs magic mirror
  # if mirror is not downloaded it downloads first and then installs it
  # returns true if mirror is finally installed
  def install (self):
    os.system("git clone https://github.com/MichMich/MagicMirror")
    if self.isMirrorDownloaded:
      print("MAGIC MIRROR DOWNLOADED SUCCESSFULLY")
      os.chdir(self.magicMirrorDir)
      subprocess.check_call('npm install', shell=True)
      return True
    else:
      print("SOMETHING WENT WRONG")
      return False
        
# main function	
if __name__ == '__main__':
  # init an object
  objMagicMirror = InitMirror()
  bInstalled = True
  # check if mirror is downloaded
  if not objMagicMirror.isMirrorDownloaded():
    # need to install mirror
    bInstalled = objMagicMirror.install()
	
  #mirror already installed
  if bInstalled:
    print ("SMOW Installation Completed")
	
  
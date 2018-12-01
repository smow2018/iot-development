#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an installation script of SMOW software.                                          *#
#* The script first checks if the MagicMirror open source already exists in the current directory     *#
#* If it exists, is will start the software by executing mnp install                                  *#
#* If not, Magic Mirror 2 should be cloned from github repository                                     *#
#*                                                                                                    *#
#* 30/11/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#

import os
import subprocess


class InitMirror:
 
  def __init__(self):
    # The repository that Magic Mirror open source is located
    self.url = "https://github.com/MichMich/MagicMirror"
	
  def isMirrorInstalled (self):
    # Check if Magic Mirror is already installed
    print ("Initializing SMOW......")
    print ("Check for previous installations")
    if os.path.isdir("MagicMirror"):
      # TODO: Add more checks on the format of the directory
      return True
    else:
      return False
	  
  def install (self):
    os.system("git clone https://github.com/MichMich/MagicMirror")
    if self.isMirrorInstalled:
      print("CLONED SUCCESSFULLY")
      os.chdir('/home/pi/Desktop/iot-development-master/MagicMirror')
      subprocess.check_call('npm install', shell=True)
      return True
    else:
      print("SOMETHING WENT WRONG")
      return False
    

  def printInfo(self):
    print ("*****************************************************************************")
    print ("* SMOW V1.0                                                                 *")
    print ("* SMOW stands for Smart Mirror On the Wall.                                 *")
    print ("* It is a set of features for a Smart Mirror product, by Lambda Electronics *")
    print ("* The following is an installation script of SMOW software.                 *")
    print ("* If it exists, is will start the software by executing mnp install         *")
    print ("* If not, Magic Mirror 2 should be cloned from github repository            *")
    print ("*****************************************************************************")
    print ("");
  
  def start (self):
    #TODO: Add implementation
    os.chdir('/home/pi/Desktop/iot-development-master/MagicMirror')
    subprocess.check_call('npm start', shell=True)
	
if __name__ == '__main__':

  objMagicMirror = InitMirror()
  objMagicMirror.printInfo ()
  bResult = True
  
  if not objMagicMirror.isMirrorInstalled():
    # need to install mirror
    bResult = objMagicMirror.install()
	
  #mirror already installed, start it
  if bResult:
    objMagicMirror.start()
	
  
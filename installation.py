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
# The repository that Magic Mirror open source is located
url_repository = "https://github.com/MichMich/MagicMirror"

def printInfo():
  print ("*********************************************************************************************")
  print ("* SMOW V1.0                                                                                 *")
  print ("* SMOW stands for Smart Mirror On the Wall.                                                 *")
  print ("* It is a set of features for a Smart Mirror product, powered by Lambda Electronics         *")
  print ("* The following is an installation script of SMOW software.                                 *")
  print ("* If it exists, is will start the software by executing mnp install                         *")
  print ("* If not, Magic Mirror 2 should be cloned from github repository                            *")
  print ("*********************************************************************************************")
  print ("");
  print ("Initializing SMOW......")
  print ("Check for previous installations")
  
def startMagicMirror ():
  #TODO: Add implementation
  print("")

  
printInfo()
if os.path.isdir("MagicMirror"):
  print ("Magic Mirror already installed")
else:
  print ("Checking out Magic mirror from repository")
  path  = "MagicMirror_Project" 
  clone = "git clone https://github.com/MichMich/MagicMirror" 
  os.system(clone) # Cloning
  print ("\n CLONED SUCCESSFULLY.! \n")
# call function to start magic mirror
startMagicMirror ()
  
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
import sys
import subprocess
import shutil
sys.path.insert(0, '/home/pi/iot-development/Classes')
from  startMirror import Mirror

# This class is used to start magic mirror open source software in Raspberry pi current directory
# First it checks wether config.js exists
# If exists, it simply starts the software by running nmp start
mirror = Mirror()
mirror.start()
	
  

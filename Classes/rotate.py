#******************************************************************************************************#
#* SMOW V1.0                                                                                          *#
#* SMOW stands for Smart Mirror On the Wall.                                                          *#
#* It is a set of features for a Smart Mirror product, powered by Lambda Electronics                  *#
#* The following is an run script of SMOW software.                                                   *#
#* The script first asks if user wants to set raspberry in landscape or portrait mode                 *#
#* Then replaces the value in config.txt file                                                         *#
#*                                                                                                    *#
#*                                                                                                    *#
#* 11/12/2018 - Vasileios Toukas                                                                      *#
#* - Creation                                                                                         *#
#******************************************************************************************************#
import os
import sys

# class to store the orientation values
class Orientation:
  portrait = 0 # default
  lanscape_right = 1
  portrait_upside_down = 2
  landscape_left = 3
# end of class __Orientation__

# This class is used to setup orientation in raspberry conf file.
# retrieves info from config file
# replaces orientation value
class Rotate:
  #initializes class
  def __init__(self):
    #self.newOrientation = Orientation.portrait
    self.orientationLine = "display_rotate="
  
  # Retrieves the orientation value
  # return a Rotate object value
  def getCurrentOrientation (self):
    # read config file
	bFileFound = os.path.isfile("/boot/config.txt")
	if not bFileFound:
	  return Orientation.portrait
	else:
	  try:
	    f = open('/boot/config.txt', 'r')
	    lineList = f.readlines()
	    f.close()
	    bOrientationFound = False
	    for line in lineList:
	      if self.orientationLine in line:
	        bOrientationFound = True
	        break
	    if not bOrientationFound:
	      return Orientation.portrait
	    else:
	      strOrientation = line[-2:]
	      if strOrientation == '0\n':
	        return Orientation.portrait
	      elif strOrientation == '1\n':
		    return Orientation.lanscape_right
	      elif strOrientation == '2\n':
	        return Orientation.portrait_upside_down
	      else:
	        return Orientation.landscape_left
	  except:
	    return Orientation.portrait
  
  # Retreives the orientation value
  # returns a string
  def getStrCurrentOrientation (self):
    orientation = self.getCurrentOrientation()
    if orientation == 0:
      return 'PORTRAIT'
    elif orientation == 1:
      return 'LANDSCAPE RIGHT'
    elif orientation == 2:
      return 'PORTRAIT UPSIDE DOWN'
    else:
      return 'LANDSCAPE LEFT'

		
  # set the new value of orientation
  # return True if update is sucessful, else eitherwise
  def setOrientation(self, orientation):
    # read config file
	bFileFound = os.path.isfile("/boot/config.txt")
	if bFileFound:
	  try:
	    inFile = open('/boot/config.txt', 'r')
	    strReplace = 'display_rotate=' + orientation + '\n'
	    strSearch = 'display_rotate=' + str(self.getCurrentOrientation()) + '\n'
	    lineList = inFile.readlines()
	    uiIndex = 1
	    for line in lineList:
		  if line == strSearch:
		    uiIndex = uiIndex + 1
		    lineList[uiIndex] = strReplace
		    break
	    inFile.close()
	    outFile = open('/boot/config.txt', 'w')
	    outFile.writelines(lineList)
	    outFile.close()
            return True
	  except:
	    print 'Something went wrong with /boot/config.txt file'
            return False
	else:
	  print 'File /boot/config.txt not found'
          return False
  
# end of class __Rotate__

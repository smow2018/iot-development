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

class Orientation:
  portrait = 0 # default
  lanscape_right = 1
  portrait_upside_down = 2
  landscape_left = 3

# This class is used to screen orientation in raspberry conf file.
# First it ask from user wether he wants to change
# If no, it exits
# If yes :
#   - retrieves info from config file
#   - replaces orientation value
#   - restarts the pi
class Rotate:
  #initializes class
  def __init__(self):
    self.currentOrientation = Orientation.portrait
    self.newOrientation = Orientation.portrait
    self.orientationLine = "display_rotate="

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
		
  def setOrientation(self, orientation):
    # read config file
	bFileFound = os.path.isfile("/boot/config.txt")
	if bFileFound:
	  try:
	    inFile = open('/boot/config.txt', 'r')
	    strReplace = 'display_rotate=' + orientation + '\n'
	    strSearch = 'display_rotate=' + str(self.currentOrientation) + '\n'
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
	  except:
	    print 'Something went wrong with /boot/config.txt file'
	else:
	  print 'File /boot/config.txt not found'
  
# main function	
if __name__=='__main__':
  # fist we need to check what is the current orientation
  # ask user if he wants to change
  # if no, exit
  # if yes, change andf update config file
  pi = Rotate()
  # get current orientation
  pi.currentOrientation = pi.getCurrentOrientation ()
  if pi.currentOrientation == 0:
    strCurrentOrientation = 'PORTRAIT'
  elif pi.currentOrientation == 1:
    strCurrentOrientation = 'LANDSCAPE RIGHT'
  elif pi.currentOrientation == 2:
    strCurrentOrientation = 'PORTRAIT UPSIDE DOWN'
  else:
    strCurrentOrientation = 'LANDSCAPE LEFT'
  print 'Smow has ' + strCurrentOrientation + ' orientation'
  strChange = raw_input("Do you want to change it(Y/N)")
  if strChange == 'y' or strChange == 'Y':
    print ''
    print 'Please select orientation to change :'
    print 'PORTRAIT             : 0'
    print 'LANDSCAPE RIGHT      : 1'
    print 'PORTRAIT UPSIDE DOWN : 2'
    print 'LANDSCAPE LEFT       : 3'
    selection = raw_input()
    if selection == '1':
      pi.setOrientation(selection)
    elif selection == '2':
      pi.setOrientation(selection)
    elif selection == '3':
      pi.setOrientation(selection)
    else:
      pi.setOrientation(selection)
	
	# get current orientation
    pi.currentOrientation = pi.getCurrentOrientation ()
    if pi.currentOrientation == 0:
      strCurrentOrientation = 'PORTRAIT'
    elif pi.currentOrientation == 1:
      strCurrentOrientation = 'LANDSCAPE RIGHT'
    elif pi.currentOrientation == 2:
      strCurrentOrientation = 'PORTRAIT UPSIDE DOWN'
    else:
      strCurrentOrientation = 'LANDSCAPE LEFT'
    print "Orientation changed to " + strCurrentOrientation
  else:
    print("No changing of orientation continue with SMOW configuration")

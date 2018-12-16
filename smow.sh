#!/bin/bash

echo "*****************************************************************************"
echo "* SMOW V1.0                                                                 *"
echo "* SMOW stands for Smart Mirror On the Wall.                                 *"
echo "* It is a set of features for a Smart Mirror product, by Lambda Electronics *"
echo "* The following is an run script of SMOW software.                          *"
echo "*****************************************************************************"

cd /home/pi/iot-development
sudo python configure_smow.py
python run_smow.py

#!/bin/bash
# This scripts runs the configuration commands
# for each rasoberry pi that is going to be used in SMOW


echo "Change permission rights to software"
cd /home/pi/iot-development
sudo chmod 777 *
cd /home/pi/iot-development/Classes
sudo chmod 777 *
cd /home/pi/iot-development/configuration_files
sudo chmod 777 *
cd /home/pi

echo "Update pi"
sudo apt-get update

echo "Upgrade pi"
echo y | sudo apt-get upgrade

echo "Update rpi"
sudo rpi-update

echo "Install npm"
sudo apt-get install npm

echo "Disable rainbow splash"
sudo sh -c "echo 'disable_splash=1' >> /boot/config.txt"

echo "Hide boot messages"
sudo cp /home/pi/iot-development/configuration_files/cmdline_silent_boot.txt /boot/cmdline.txt

echo "Replace raspberry logo with smow logo"
sudo cp /home/pi/iot-development/configuration_files/smow_logo_negative.png /usr/share/plymouth/themes/pix/splash.png

echo "Unzip city list"
gunzip /home/pi/iot-development/configuration_files/city.list.json.gz
chmod 777 /home/pi/iot=development/configuration_files/city.list.json

echo "Installing SMOW"
python /home/pi/iot-development/install_smow.py

echo "make smow executable"
sudo chmod 777 /home/pi/iot-development/smow.sh

echo "Autostart smow"
sudo sh -c "echo '@lxterminal -e sh /home/pi/iot-development/smow.sh' >> /home/pi/.config/lxsession/LXDE-pi/autostart"

echo "Hide menu bar"
sudo cp /home/pi/iot-development/configuration_files/panel.nobar /home/pi/.config/lxpanel/LXDE-pi/panels/panel

echo "Disable mouse cursor and sleep display"
sudo cp /home/pi/iot-development/configuration_files/lightdm.conf.nocursor /etc/lightdm/lightdm.conf

echo "Change background picture"
sudo cp /home/pi/iot-development/configuration_files/desktop-items-0.conf.smow /home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf

echo "reboot pi"
sudo reboot

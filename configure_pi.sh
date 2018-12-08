#!/bin/bash
# This scripts runs the configuration commands
# for each rasoberry pi that is going to be used in SMOW

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
sudo cp /home/pi/iot-development/cmdline_silent_boot.txt /boot/cmdline.txt

echo "Replace raspberry logo with smow logo"
sudo cp /home/pi/iot-development/smow_logo_negative.png /usr/share/plymouth/themes/pix/splash.png

echo "reboot pi"
sudo reboot

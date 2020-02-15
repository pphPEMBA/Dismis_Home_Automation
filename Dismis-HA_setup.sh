#!/bin/bash
echo "#############################################################"
echo "Updating apt, preparing to install pip3, dependencies,"
echo "python3 libraries and other things to make Dismis_Home_Automation"
echo "runs perfectly for now and the future"
echo "#############################################################"
export DISMIS_HOME_AUTOMATION_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "DISMIS_HOME_AUTOMATION_DIR = $DISMIS_HOME_AUTOMATION_DIR"
echo " "
echo "*** Installing Dependencies ***"
apt-get update #system upate
apt-get install python3-pip #pip3
apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 #pyaudio
apt-get install libttspico-utils #pico2wave
pip3 install --upgrade google-api-python-client google-auth-httplib2 #google-auth-oauthlib #google-api-python-clients
apt-get install sox libsox-fmt-mp3 #sox
cd
pip3 install -r $DISMIS_HOME_AUTOMATION_DIR/requirements.txt #Python3 Libraries
echo " "
echo "Creating Dismis_Home_Automation and coping files from source to Dismis_Home_Automation"
mkdir -p ~/.Dismis_Home_Automation
cp -a $DISMIS_HOME_AUTOMATION_DIR/. ~/.Dismis_Home_Automation/
echo " "
echo " Installing Dismis-HA Accomplished! "
echo "_____________________________________________________________"
echo
echo "Now Running Dismis-Home_Automation"
cd ~/.Dismis_Home_Automation/
python3 DISMIS-HA.py

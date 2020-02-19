#!/bin/bash
echo "############################################################# "
echo "Updating apt, preparing to install pip3, dependencies,"
echo "python3 libraries and other things to make Dismis_Home_Automation"
echo "runs perfectly for now and the future"
echo "############################################################# "
export DISMIS_HOME_AUTOMATION_SETUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "DISMIS_HOME_AUTOMATION_SETPUT_DIR = $DISMIS_HOME_AUTOMATION_SETUP_DIR"
echo " "
echo "*** Installing Dependencies ***"

echo " "
pico2wave -w speech.wav "Hello PEMBA, please reconfigure mpg on two three volume at 30% in PulseAudio Control. Now opening PulseAudio Control application" && aplay speech.wav 
mpg123 $DISMIS_HOME_AUTOMATION_SETUP_DIR/volReconfigure_MPG123.mp3 &
pavucontrol
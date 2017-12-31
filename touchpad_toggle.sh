if [ $(xinput list-props "FocalTechPS/2 FocalTech FocalTech Touchpad" | grep "Device Enabled" | cut -d ':' -f2) -eq "1" ];
then
xinput set-prop "FocalTechPS/2 FocalTech FocalTech Touchpad" "Device Enabled" 0
else
xinput set-prop "FocalTechPS/2 FocalTech FocalTech Touchpad" "Device Enabled" 1
fi

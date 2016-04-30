#!/bin/bash 
# Driver for "Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter"
# This Adapter is present in Lenovo Y50. Stock divers may be buggy
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

# Make/Go to sandbox directory
cd ~
if [ ! -d "sandbox" ]; then
	mkdir sandbox
fi
cd ~/sandbox

# pull driver files
if [ ! -d "rtlwifi_new" ]; then
	git clone https://github.com/lwfinger/rtlwifi_new/
	check_quit "$?"
fi
cd rtlwifi_new
make clean
git pull origin master
check_quit "$?"

# Install Driver
make
check_quit "$?"
sudo make install
check_quit "$?"
sudo modprobe -r rtl8723be
sudo modprobe rtl8723be
check_quit "$?"

# Clean sandbox
cd ~/sandbox
rm -rf rtlwifi_new
check_quit "$?"

# Ref : http://askubuntu.com/questions/590414/wifi-problems-with-rtl8723be-in-ubuntu-14-04

# Make/Go to sandbox directory
if [ ! -d "~/sandbox" ]; then
	cd ~
	mkdir sandbox
fi
cd ~/sandbox

# pull driver files
if [ ! -d "rtlwifi_new" ]; then
	git clone https://github.com/lwfinger/rtlwifi_new/
fi
cd rtlwifi_new
make clean
git pull origin master

# Install Driver
make
sudo make install
sudo modprobe -r rtl8723be
sudo modprobe rtl8723be

# Clean sandbox
cd ~/sandbox
rm -rf rtlwifi_new

# Ref : http://askubuntu.com/questions/590414/wifi-problems-with-rtl8723be-in-ubuntu-14-04

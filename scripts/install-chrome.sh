#!/bin/bash 
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

cd /tmp
# This link may be broken
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
check_quit "$?"
sudo dpkg -i google-chrome-stable_current_amd64.deb
check_quit "$?"
sudo apt-get -f install
check_quit "$?"

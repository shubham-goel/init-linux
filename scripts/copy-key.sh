#!/bin/bash 
# Copies rsa public key to clipboard

function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

# Install xsel
sudo apt-get install xsel
check_quit "$?"

# Copy public key to clipboard
cat ~/.ssh/id_rsa.pub | xsel -ib
check_quit "$?"

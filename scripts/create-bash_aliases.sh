#!/bin/bash 
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

# Go to home directory
cd ~

# Add bash-aliases
if [ ! -f ~/.bash_aliases ]; then
	touch .bash_aliases
	sudo chmod 755 .bash_aliases
	check_quit "$?"
fi

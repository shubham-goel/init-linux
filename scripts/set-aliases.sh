#!/bin/bash 
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

sudo cat settings/bash_aliases > .bash_aliases
check_quit "$?"

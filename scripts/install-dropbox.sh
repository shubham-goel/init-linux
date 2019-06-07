#!/bin/bash
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
check_quit "$?"

#!/bin/bash 
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

cd settings/

if [ -f bash_aliases ]; then
	rm bash_aliases
	check_quit "$?"
fi
touch bash_aliases
check_quit "$?"

if [ -f ~/.bash_aliases ]; then
	cat ~/.bash_aliases >> bash_aliases
	check_quit "$?"
fi

cat ~/.bashrc | grep "alias" | grep -v "#.*alias">> bash_aliases
check_quit "$?"
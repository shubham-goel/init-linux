#!/bin/bash 
# Takes input as $ ./install-package.sh <package> <repo>
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

if [ -n "$2" ]              # Tested variable is quoted.
then
	sudo add-apt-repository $2
	check_quit "$?"
	sudo apt-get update
	check_quit "$?"
fi 

if [ -n "$1" ]              # Tested variable is quoted.
then
	sudo apt-get install $1
	check_quit "$?"
fi 
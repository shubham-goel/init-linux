#!/bin/bash 
function check_quit {
	if [ $1 -ne 0 ]; then
	    exit 1
	fi
}

# Change terminal prompt to $<uname> [<path>]
# Example : 
# shubham [~/Github] git status

echo '
if [ "$color_prompt" = yes ]; then
    PS1='"'"'${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u \[\033[00m\][\[\033[01;34m\]\w\[\033[00m\]] '"'"'
else
    PS1='"'"'${debian_chroot:+($debian_chroot)}\u [\w] '"'"'
fi' >> ~/.bashrc

check_quit "$?"
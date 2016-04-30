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

sudo echo "# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias upgrade='sudo apt-get upgrade'
alias update='sudo apt-get update'
alias gop='gnome-open'
alias gpom='git push origin master'
alias gpum='git push upstream master'
alias gplu='git pull upstream master'
alias gplo='git pull origin master'
alias py='python'
alias wifi='sudo modprobe -r rtl8723be && sudo modprobe rtl8723be'
alias s++='/usr/lib/simplecpp/s++'
alias wt20='watch python2 ~/.utilities/.wt20.py'
" > .bash_aliases
check_quit "$?"

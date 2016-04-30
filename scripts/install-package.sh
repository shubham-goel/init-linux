if [ -n "$2" ]              # Tested variable is quoted.
then
	sudo add-apt-repository $2
	sudo-apt-get update
fi 

if [ -n "$1" ]              # Tested variable is quoted.
then
	sudo-apt-get install $1
fi 
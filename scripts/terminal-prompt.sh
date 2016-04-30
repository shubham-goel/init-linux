# Go to home directory
cd ~

# Change terminal prompt
echo "
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u \[\033[00m\][\[\033[01;34m\]\w\[\033[00m\]] '
else
    PS1='${debian_chroot:+($debian_chroot)}\u [\w] '
fi" >> ~/.bashrc

if [ $? -ne 0 ]; then
    echo "Unable to change prompt"
else
	echo "Changed prompt successfully."
	echo " Use command $ source ~/.bashrc to incorporate changes"
fi
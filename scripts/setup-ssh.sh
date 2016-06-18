# Defining variables
email="sgoel160@gmail.com"

# Goto Home Dir
cd ~

# Create ssh folder
if [ ! -d ".ssh" ]; then
	mkdir .ssh
fi

# Manage Permissions
sudo chmod u+xr,go-rwx .ssh
sudo chmod 700 .ssh

# Remove existing keys
rm -rf .ssh/id_rsa
rm -rf .ssh/id_rsa.pub

# Create new key pair
ssh-keygen -t rsa -b 4096 -C $email

# Check if keys are stored in correct folder
if [ ! -f ".ssh/id_rsa" ]; then
	echo "Private key not found! Aborting." 1>&2
	exit 1
fi

if [ ! -f ".ssh/id_rsa.pub" ]; then
	echo "Public key not found! Aborting." 1>&2
	exit 1
fi

# Set key permissions
sudo chmod 600 .ssh/id_rsa
sudo chmod 644 .ssh/id_rsa.pub

# Add keys to ssh-adent
eval "$(ssh-agent -s)"

if [ -f ".ssh/id_rsa" ]; then
	ssh-add .ssh/id_rsa
fi


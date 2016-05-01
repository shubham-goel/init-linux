import sys
import subprocess

# Global Vars
script_name = {
"prompt":"terminal-prompt.sh",
"alias":"set-aliases.sh",
"wifi":"setup-wifi.sh",
"git":"conf-git.sh",
"ssh":"setup-ssh.sh",
"copy-key":"copy-key.sh",
"firefox":"open-firefox.sh",
"package":"install-package.sh",
"chrome":"install-chrome.sh"
}

def get_packages():
	packages = {}
	with open('settings/packages.csv') as f:
		content = f.readlines()
	for line in content:
		spl = line.strip().split(',')
		if len(spl) >= 3 and spl[2] != '':
			new_pkg = [spl[1],spl[2]]
		else:
			new_pkg = [spl[1],None]
		packages[spl[0]] = new_pkg

	return packages


# Ref : http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via input() and return their answer.

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is True for "yes" or False for "no".
	"""
	valid = {"yes": True, "y": True, "ye": True,
			 "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		# sys.stdout.write(question + prompt)
		choice = input(question + prompt).lower()
		# print(choice)
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
							 "(or 'y' or 'n').\n")
def get_script_name(name):
	return './scripts/'+script_name[name]

packages = get_packages()

# terminal prompt
ques = "Change terminal prompt to \"<user> [<dir>] \" in .bashrc?"
if query_yes_no(ques, default = "no"):
	# print("Calling process..." + get_script_name("prompt"),shell=True)
	if subprocess.call([get_script_name("prompt")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")


# bash aliases?
ques = "Create/Reset aliases in .bash_aliases?"
if query_yes_no(ques, default = "yes"):
	if subprocess.call([get_script_name("alias")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")

# Setup wifi modules?
ques = "Install wifi drivers?"
if query_yes_no(ques, default = "yes"):
	if subprocess.call([get_script_name("wifi")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")

# install packages...
ques = "Install new packages?"
if query_yes_no(ques, default = "yes"):
	for package in packages:
		ques = "Install " + package + "?"
		if query_yes_no(ques, default = "yes"):
			if subprocess.check_call([get_script_name("package") +" "+ str(packages[package][0]) + " "+ str(packages[package][1])],shell=True) == 1 :
				print("Exit Status error!")
			else:
				print("SUCCESS!")
	ques = "Install Google Chrome?"
	if query_yes_no(ques, default = "yes"):
		if subprocess.call([get_script_name("chrome")],shell=True) == 1 :
			print("Exit Status error!")
		else:
			print("SUCCESS!")

# Configure Git
ques = "Configure Git?"
if query_yes_no(ques,default="yes"):
	if subprocess.call([get_script_name("git")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")

# Setup SSH keys
ques = "Setup new SSH Keys?"
if query_yes_no(ques,default="no"):
	print("Please save key in ~/.ssh/id_rsa")
	if subprocess.call([get_script_name("ssh")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")

# Copy key to Github
ques = "Add RSA key to Github?"
if query_yes_no(ques,default="no"):
	print("You Public Key will be copied to you clipboard")
	print("Please Add it as a new SSH Key in your github account")
	if subprocess.call([get_script_name("copy-key")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")
	if subprocess.check_call([get_script_name("firefox") + " https://github.com/settings/keys"],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")

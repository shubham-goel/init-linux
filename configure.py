import sys
import subprocess

# Global Vars
script_name = {
"prompt":"set-aliases.sh",
"alias":"set-aliases.sh",
"wifi":"setup-wifi.sh",
"git":"conf-git.sh",
"ssh":"setup-ssh.sh",
"copy-key":"copy-key.sh",
"firefox":"open-firefox.sh",
"package":"install-package.sh"
}
packages = {
"tilda":["tilda",None], 
"wine":["wine",None], 
"steam":["steam",None],
"git":["git",None],
"sublime3":["sublime-text-installer","ppa:webupd8team/sublime-text-3"]
}


# Ref : http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

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
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
def get_script_name(name):
	return './scripts/'+script_name[name]


# terminal prompt
ques = "Change terminal prompt to \"<user> [<dir>] \" in .bashrc?"
if query_yes_no(ques, defalut = "no"):
	subprocess.call([get_script_name("prompt")])


# bash aliases?
ques = "Create/Reset aliases in .bash_aliases?"
if query_yes_no(ques, defalut = "yes"):
	subprocess.call([get_script_name("alias")])

# Setup wifi modules?
ques = "Install wifi drivers?"
if query_yes_no(ques, defalut = "yes"):
	subprocess.call([get_script_name("wifi")])

# install packages...
ques = "Install new packages?"
if query_yes_no(ques, defalut = "yes"):
	for package in packages:
		ques = "Install " + package + "?"
		if query_yes_no(ques, defalut = "yes"):
			subprocess.check_call([get_script_name("package") + str(packages[package][0]) + str(packages[package][1])])

# Configure Git
ques = "Configure Git?"
if query_yes_no(ques,defalut="yes"):
	subprocess.call([get_script_name("git")])
	ques = "Configure Git?"
	if query_yes_no(ques,defalut="yes"):


# Setup SSH keys
ques = "Setup new SSH Keys?"
if query_yes_no(ques,defalut="no"):
	print("Please save key in ~/.ssh/id_rsa")
	subprocess.call([get_script_name("ssh")])

# Copy key to Github
ques = "Add RSA key to Github?"
if query_yes_no(ques,defalut="no"):
	print("You Public Key will be copied to you clipboard")
	print("Please Add it as a new SSH Key in your github account")
	subprocess.call([get_script_name("copy-key")])
	subprocess.check_call([get_script_name("firefox") + "https://github.com/settings/keys"])

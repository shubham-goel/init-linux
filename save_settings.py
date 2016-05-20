import sys
import subprocess
import os

# Global Vars
file_path = {
	"to_save_config":"settings/config.csv",
	# "all_config":"../settings/all_config_folders",
}

script_name = {
	"aliases":"save-aliases.sh",
}

def get_contents(path):
	config_folders = []
	with open(path) as f:
		content = f.readlines()
	for line in content:
		spl = line.strip()
		config_folders.append(spl)

	return config_folders

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

ques = "List .config folders mared as \"to save\"?"
if query_yes_no(ques,default="yes"):
	current_folders = get_contents(file_path["to_save_config"])
	key=1
	for i in os.listdir('~/.config/'):
		i = i.strip().split('/')[-1]
		if i in current_folders:
			print("* " + str(key) + ". " + str(i))
		else:
			print("  " + str(key) + ". " + str(i))
	print("* Already listed as \"to save\"")
	ques = "Reset list and create again?"
	if query_yes_no(ques,default="yes"):
		if subprocess.call(["rm " + file_path("to_save_config")],shell=True) == 1:
			print("Exit Status error!")
		elif subprocess.call(["touch " + file_path("to_save_config")],shell=True) == 1:
			print("Exit Status error!")
		for i in os.listdir('~/.config/'):
			i = i.strip().split('/')[-1]
			ques = "Add " + i + " to list?"
			if query_yes_no(ques,default="yes"):
				if subprocess.call(["cat "+i+" >> "+file_path("to_save_config")],shell=True) == 1:
					 print("Exit Status error!")

ques = "Copy .config folders ?"
if query_yes_no(ques,default="yes"):
	config_folders = get_contents(file_path["to_save_config"])
	if config_folders:
		for folder in config_folders:
			ques = "Copy .config folders for " + str(folder) + " ?"
			if query_yes_no(ques,default="yes"):
				if subprocess.call(["sudo cp --recursive ~/.config/" + str(folder) + " ./settings/config"],shell=True) == 1 :
					print("Exit Status error!")
				else:
					print("SUCCESS!")
	else:
		print("No folders listed. Moving on...")


ques = "save bash aliases?"
if query_yes_no(ques,default="yes"):
	if subprocess.call([get_script_name("aliases")],shell=True) == 1 :
		print("Exit Status error!")
	else:
		print("SUCCESS!")


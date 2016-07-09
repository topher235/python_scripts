import pip, io, datetime
import os, sys, subprocess

#Recieve list of installed packages
installed_packages = pip.get_installed_distributions()

#Opens the text file containing the python modules
def open_file(filename):
	if(sys.platform == "win32"):
		os.startfile(filename)
	else:
		if(sys.platform == "darwin"):
			opener = "open"
		else:
			opener = "xdg-open"
		subprocess.call([opener, filename])

#Write the list of packages to file: installed_python_modules
try:
	with io.open('installed_python_modules', 'w') as file:
		for i in installed_packages:
			space = 40 - len(i.key)
			file.write("Key: " + i.key)
			file.write('{:>{space}}'.format("Version: " + i.version + '\n', space=space))
		today = datetime.date.today().isoformat()
		file.write("Date: "  + today)
		file.close()
		open_file('installed_python_modules')
except IOError:
	print("ERROR -- Could not open file")



#TODO: Fix formatting
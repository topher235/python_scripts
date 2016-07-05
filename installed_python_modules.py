import pip, io, datetime

#Recieve list of installed packages
installed_packages = pip.get_installed_distributions()

#Write the list of packages to file: installed_python_modules
try:
	with io.open('installed_python_modules', 'w') as file:
		for i in installed_packages:
			space = 40 - len(i.key)
			file.write("Key: " + i.key)
			file.write('{:>{space}}'.format("Version: " + i.version + '\n', space=space))
		today = datetime.date.today().isoformat()
		file.write("Date: "  + today)

except IOError:
	print("ERROR -- Could not open file")

#TODO: Fix formatting
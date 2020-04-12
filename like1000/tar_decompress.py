import tarfile

file_name = "1000.tar"

#check to see if a file is a valid tar file
try:
	print(file_name, tarfile.is_tarfile(file_name))
except IOError as err:
	print(file_name, err)

#provide the metadata for the .tar file
file_name = tarfile.open("1000.tar", "r")
print("Files contained in {}:".format(file_name))
files = file_name.getnames()
print(files)
file_name.close()

#extract file from .tar file
#file_name = tarfile.open("1000.tar", "r")
#file_name.extractall()
#file_name.close()

i = 1000
while i > 0:
	file_name = tarfile.open(str(i) + ".tar", "r")
	file_name.extractall()
	file_name.close()
	print("Extracting file {}".format(i))

	i -= 1

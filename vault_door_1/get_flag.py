import re

password_dict = {}
with open('password.txt', 'r') as p:
	for line in p:
		number = re.findall(r'\(\d\d?\)', line)
		flag = re.findall(r"'\w'", line)
		password_dict[number][0] = flag[0]
		print(password_dict)

import re

ro = re.compile(r"\((\d+)\)\s+==\s'(\w)'")

password_list = []

with open('password.txt', 'r') as p:
	for line in p:
		mo = ro.search(line)
		password_list.append((int(mo.group(1)), mo.group(2)))
	password_list.sort()
	
	flag = ""
	for flag_piece in password_list:
		flag += flag_piece[1]

	print(flag)

import os

#can be pulled completely from the command line using curl -s -H "User-Agent: picobrowser" "https://2019shell1.picoctf.com/problem/37829/flag" | grep -oE "picoCTF{.*?}"

URL = "https://2019shell1.picoctf.com/problem/37829/flag"
#would like to come back later and use the 're'module to actually pull the flag out of here
#match = 'picoCTF{.*?}'

os.system("curl -H 'User-Agent: picobrowser' {} | grep {}".format(URL, match))

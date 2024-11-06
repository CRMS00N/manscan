import socket
import time
import sys
import pyfiglet
Z1 = '\033[2;31m'
print(Z1)	
s1 = pyfiglet.figlet_format('C R M S 0 0 N')
print(s1)
print('_'*66)
g =  '\033[2;32m' 
print(g)
s2 = pyfiglet.figlet_format('MANSCAN ')
print(s2)
print('_'*66)



args = sys.argv
open = []
for port in range(int(args[2]) , int(args[3])):
	
	try:
		
		sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
		
		sock.settimeout(1)
		
		sock.connect((args[1], port))
		open.append(port)
		print(f"\033[1;39m{port} \033[1;32m[OPEN] \033[2;36m{socket.getservbyport(port)}")
	
	except:
		try:
			
			print(f"\033[1;39m{port} \033[1;31m[CLOSED] \033[2;36m{socket.getservbyport(port)}")
		except:
			print(f'\033[1;39m {port} \033[1;31m[CLOSED] \033[2;36m UNKOWN SERVICE')
		
print("_________________________")

for i in open:
	print(f"\033[1;39m{i} [OPEN]")
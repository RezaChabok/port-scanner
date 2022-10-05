import socket
import termcolor



def scan(target, ports):
	print("\n" + termcolor.colored((f"-> Starting Scan For {target}:"), "green"))
	for port in range (1, ports):
		try:
			sock = socket.socket()
			sock.settimeout(2)
			sock.connect((target, port))
			print(termcolor.colored((f"[+] Port Opened {port} -> "), "cyan"), socket.getservbyport(port))
		except TimeoutError :
			print("\n" + termcolor.colored((f"IP {target} is Not Available!!!"), "red"))
			break
		except : pass
def checker(ip):
	for num in ip.split('.'):
		if int(num) >= 250 :
			return False
	try:
		socket.inet_aton(ip)
	except socket.error:
		return False
	return True
def finder(ip, flag):
		count = 0
		loc = 0
		if flag == 8:
			end = 1
		else : end = 2
		while True:
			if count == end:
 				break
			elif ip.split("/")[0][loc] == ".":
				count +=1
			loc += 1
		return loc-1	
while True:
	targets = input(termcolor.colored(("[*] Enter Target To Scan(split them by ,): "), "blue"))
	ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want To Scan: "), "blue")))
	if ',' in targets:
		print(termcolor.colored(("[*] Scanning Multiple Targets") ,"green"))
		for ip_addr in targets.split(",") :
			if checker(ip_addr.split("/")[0]):	
				if '/' in ip_addr:
					if ip_addr.split("/")[1] == '32':
						scan(ip_addr.split("/")[0], ports)
					elif ip_addr.split("/")[1] == '24':
						for i in range(1, 250):
							if ip_addr.split("/")[0][-4] == ".":
								last = -3
							elif ip_addr.split("/")[0][-3] == ".":
								last = -2
							elif ip_addr.split("/")[0][-2] == ".":
								last = -1
							else:
								print(termcolor.colored(ip_addr," is have a problem !", "red"))
								break
							scan(ip_addr.split("/")[0][:last]+str(i), ports)
					elif ip_addr.split("/")[1] == '16':
						loc = finder((ip_addr.split("/")[0]), 16)
						for i in range(1,250):
							for j in range(1, 250):
								scan((ip_addr[:loc]+'.'+str(i)+'.'+str(j)), ports)
					elif ip_addr.split("/")[1] == '8':
						loc = finder((ip_addr.split("/")[0]), 8)
						for i in range(1, 250):
							for j in range(1,250):	
								for k in range(1, 250):
									scan((ip_addr[:loc]+'.'+str(i)+'.'+str(j)+'.'+str(k)), ports)
					else :
						a = ip_addr.split("/")[0]
						print(termcolor.colored("IP {a} is have a problem (just support ip/32 , ip/24 and ip/8)", "red"))
				else:scan(ip_addr.rstrip(' '), ports)
			else:
				print(termcolor.colored("IP is not Valid!", "red"))

	else : 
		if checker(targets.split("/")[0]):	
				if '/' in targets:
					if targets.split("/")[1] == '32':
						scan(targets.split("/")[0], ports)
					elif targets.split("/")[1] == '24':
						for i in range(1, 250):
							if targets.split("/")[0][-4] == ".":
								last = -3
							elif targets.split("/")[0][-3] == ".":
								last = -2
							elif targets.split("/")[0][-2] == ".":
								last = -1
							else:
								print(termcolor.colored(targets," is have a problem !", "red"))
								break
							scan(targets.split("/")[0][:last]+str(i), ports)
					elif targets.split("/")[1] == '16':
						loc = finder((targets.split("/")[0]), 16)
						for i in range(1,250):	
							for j in range(1, 250):
								scan((targets[:loc]+'.'+str(i)+'.'+str(j)), ports)
					elif targets.split("/")[1] == '8':
						loc = finder((targets.split("/")[0]), 8)
						for i in range(1, 250):
							for j in range(1, 250):
								for k in range(1, 250):
									scan((targets[:loc]+'.'+str(i)+'.'+str(j)+'.'+str(k)), ports)
					else :print(termcolor.colored(f"IP {targets} is have a problem (just support ip/32 , ip/24 and ip/8)", "red"))
				else:scan(targets.rstrip(' '), ports)
		else : print(termcolor.colored("IP is not valid !!!", "red"))
	choose = input("Do you Want Try Again?!(y/n) > ")
	if choose.lower() == 'n':
		break	
print("Thanks For Using <3")
# REZA CHABOK

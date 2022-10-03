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
	
while True:
	targets = input(termcolor.colored(("[*] Enter Target To Scan(split them by ,): "), "blue"))
	ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want To Scan: "), "blue")))
	if ',' in targets:
		print(termcolor.colored(("[*] Scanning Multiple Targets") ,"green"))
		for ip_addr in targets.split(",") :
			if checker(ip_addr.split("/")[0]):	
				if '/' in ip_addr:
					if ip_addr.split("/")[1] == '24':
						for i in range(1, 250):
							if ip_addr.split("/")[0][-4] == ".":
								last = -3
							elif ip_addr.split("/")[0][-3] == ".":
								last = -2
							elif ip_addr.split("/")[0][-2] == ".":
								last = -1
							else:
								print(ip_addr," is have a problem !")
								break
							scan(ip_addr.split("/")[0][:last]+str(i), ports)
					elif ip_addr.split("/")[1] == '16':
						for j in range(1,250):	
							for i in range(1, 250):
								count = 0
								loc = -1*len(ip_addr.split("/")[0])
								while True:
									if count == 2:
										break
									if ip_addr.split("/")[0][loc] == ".":
										count +=1
									loc += 1
								scan(ip_addr.split("/")[0][:loc]+'.'+str(j)+'.'+str(i), ports)
					elif ip_addr.split("/")[1] == '8':
						for k in range(1, 250):
							for j in range(1,250):	
								for i in range(1, 250):
									count = 0
									loc = -1*len(ip_addr.split("/")[0])
									while True:
										if count == 3:
											break
										if ip_addr.split("/")[0][loc] == ".":
											count +=1
										loc += 1
									scan(ip_addr.split("/")[0][:loc]+'.'+str(k)+'.'+str(j)+'.'+str(i), ports)
					else :print("IP is have a problem (just support ip/24 , ip/8")
				else:scan(ip_addr.rstrip(' '), ports)
			else:
				print("IP {} is not Valid!".format(ip_addr.split(" ")).split("/")[0])

	else : 
		if checker(targets.split("/")[0]):	
				if '/' in targets:
					if targets.split("/")[1] == '24':
						for i in range(1, 250):
							if targets.split("/")[0][-4] == ".":
								last = -3
							elif targets.split("/")[0][-3] == ".":
								last = -2
							elif targets.split("/")[0][-2] == ".":
								last = -1
							else:
								print(targets," is have a problem !")
								break
							scan(targets.split("/")[0][:last]+str(i), ports)
					elif targets.split("/")[1] == '16':
						for j in range(1,250):	
							for i in range(1, 250):
								count = 0
								loc = -1*len(targets.split("/")[0])
								while True:
									if count == 2:
										break
									if targets.split("/")[0][loc] == ".":
										count +=1
									loc += 1
								scan(targets.split("/")[0][:loc]+'.'+str(j)+'.'+str(i), ports)
					elif targets.split("/")[1] == '8':
						for k in range(1, 250):
							for j in range(1,250):	
								for i in range(1, 250):
									count = 0
									loc = -1*len(targets.split("/")[0])
									while True:
										if count == 3:
											break
										if targets.split("/")[0][loc] == ".":
											count +=1
										loc += 1
									scan(targets.split("/")[0][:loc]+'.'+str(k)+'.'+str(j)+'.'+str(i), ports)
					else :print("IP is have a problem (just support ip/24 , ip/8")
				else:scan(targets.rstrip(' '), ports)
	choose = input("Do you Want Try Again?!(y/n) > ")
	if choose.lower() == 'n':
		break	
print("Thanks For Using <3")
# REZA CHABOK

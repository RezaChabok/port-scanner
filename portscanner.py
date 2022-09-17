import socket
import termcolor



def scan(target, ports):
	print("\n" + termcolor.colored((f"-> Starting Scan For {target}:"), "red"))
	for port in range (1, ports):
		try:
			sock = socket.socket()
			sock.settimeout(3)
			sock.connect((target, port))
			print(termcolor.colored((f"[+] Port Opened {port} -> "), "cyan"), socket.getservbyport(port))
		except TimeoutError :
			print("\n" + termcolor.colored((f"IP {target} is Not Available!!!"), "red"))
			break
		except : pass


targets = input(termcolor.colored(("[*] Enter Target To Scan(split them by ,): "), "blue"))
ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want To Scan: "), "blue")))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets") ,"green"))
	for ip_addr in targets.split(",") :
		scan(ip_addr.rstrip(' '), ports)

else : scan(targets ,ports)
print("Thanks For Using <3")
# REZA CHABOK

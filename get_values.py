import os
from rich.console import Console
from rich.text import Text

console = Console()

CONF = {}

def gpr(string):
	console.print(Text(string,style="bold green"))

def rpr(string):
	console.print(Text(string,style="bold red"))

def activate():
	print("Activating the firewall...........")
	os.popen("sudo systemctl start firewalld").read()

def get_status():
	state = os.popen("sudo firewall-cmd --state").read()
	if state == "running\n":
		gpr("Firewall is active")
	else:
		rpr("Firewall is not active")
		activate()
	get_active_zones()	

def get_active_zones():
	print("\tGetting Active Zones..................")
	zone = os.popen("sudo firewall-cmd --get-active-zones").read()
	CONF["ZONE"] = zone.split("\n")[0]
	print(CONF)


def get_zone_list():
	print("Getting all zone list.....................")
	zone_lst = os.popen("sudo firewall-cmd --get-zones").read().split(" ")
	zone_lst[-1]=zone_lst[-1][:-1]
	return zone_lst

def reload():
	 print(os.popen("sudo firewall-cmd --reload").read())

def list_all(zone):
	print(os.popen("sudo firewall-cmd --list-all --zone="+zone+" --permanent").read())

def get_services():
	print("Service List.....")
	print(os.popen("sudo firewall-cmd --get-services").read()) 
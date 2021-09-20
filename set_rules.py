import os
from rich.prompt import Prompt
import get_values as gv




def add_port():
	print("Adding Port.....................")
	port_no = Prompt.ask("Enter the port number")
	proto = Prompt.ask("Enter the protocol",choices = ["tcp","udp"],default="tcp")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(), default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-port="+port_no+"/"+proto+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)


def add_services():
	gv.get_services()
	gv.get_active_zones()
	print("Adding Service................")
	service = Prompt.ask("Enter service name from the above list :")
	zone = Prompt.ask("Enter the zone",choices=gv.get_zone_list(),default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)	

def add_source_port():
	print("Adding Source Port..................")
	port_no = Prompt.ask("Enter the port number")
	proto = Prompt.ask("Enter the protocol",choices = ["tcp","udp"],default="tcp")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(), default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-source-port="+port_no+"/"+proto+" --zone="+zone+" --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)

def add_sources():
	print("Adding Source..................")
	port_no = Prompt.ask("Enter the port number")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(),default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-source="+port_no+" --zone="+zone+" --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)
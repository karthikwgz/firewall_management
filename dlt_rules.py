import os
import get_values as gv
from rich.prompt import Prompt


def delete_port():
	print("Deleting Port................")
	port_no = Prompt.ask("Enter the port number")
	proto = Prompt.ask("Enter the protocol",choices = ["tcp","udp"],default="tcp")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(), default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-port="+port_no+"/"+proto+" --zone="+zone+" --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)
	
def delete_services():
	print("Deleting Services................")
	gv.get_services()
	gv.get_active_zones()
	service = Prompt.ask("Enter service name from the above list :")
	zone = Prompt.ask("Enter the zone",choices=gv.get_zone_list(),default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-service="+service+" --zone="+zone+" --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)

def delete_source_port():
	print("Deleting Source Port................")
	port_no = Prompt.ask("Enter the port number")
	proto = Prompt.ask("Enter the protocol",choices = ["tcp","udp"],default="tcp")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(), default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-source-port="+port_no+"/"+proto+" --zone="+zone+" --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)

def delete_sources():
	print("Deleting Sources................")
	port_no = Prompt.ask("Enter the port number")
	gv.get_active_zones()
	zone = Prompt.ask("Enter the zone :",choices = gv.get_zone_list(), default=gv.CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-source="+port_no+ " --zone="+zone+ " --permanent"
	print(os.popen(cmd).read())
	gv.reload()
	gv.list_all(zone)
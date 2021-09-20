from rich import print
from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.prompt import Prompt

import set_rules as st
import dlt_rules as dt
import get_values as gv


grid = Table.grid(expand=True)
grid.add_column(justify="center", ratio=1)
grid.add_column(justify="right")
grid.add_row(
    "Firewall Management Tool",
    datetime.now().ctime().replace(":", "[blink]:[/]"),
)
print(Panel(grid, style="white on blue"))

def main_menu():
    grid1 = Table(expand=True,border_style="white")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","Status of firewall"
    )
    grid1.add_row(
        "2","set Rules"
    )
    grid1.add_row(
        "3","Delete rules"
    )
    grid1.add_row(
        "4","Exit"
    )
    print(grid1)
    gv.gpr("Enter your choice : ")

def setrl_menu():
    grid1 = Table(border_style="yellow")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","Add port"
    )
    grid1.add_row(
        "2","Add Services"
    )
    grid1.add_row(
        "3","Add Sources"
    )
    grid1.add_row(
        "4","Add  Source Port"
    )
    grid1.add_row(
        "5","Main menu"
    )
    print(grid1)
    gv.gpr("Enter your choice : ")

def dltrl_menu():
    grid1 = Table(border_style="red")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","Delete Port"
    )
    grid1.add_row(
        "2","Delete Services"
    )
    grid1.add_row(
        "3","Delete Sources"
    )
    grid1.add_row(
        "4","Delete Source Port"
    )
    grid1.add_row(
        "5","Main Menu"
    )
    print(grid1)

def dltrl_choice():
    dltrl_menu()
    ch = Prompt.ask("Enter your choice :",choices=["1","2","3","4","5"])
    if ch == "1":
        dt.delete_port()
        dltrl_choice()
    elif ch == "2":
        dt.delete_services()
        dltrl_choice()
    elif ch == "3":
        dt.delete_sources()
        dltrl_choice()
    elif ch == "4":
        dt.delete_source_port()
        dltrl_choice()
    elif ch == "5":
        main_choice()
    else:
        gv.rpr("\tWrong choice")
        dltrl_choice()

def setrl_choice():
    setrl_menu()
    ch = Prompt.ask("Enter your choice :",choices=["1","2","3","4","5"])
    if ch == "1":
        st.add_port()
        setrl_choice()
    elif ch == "2":
        st.add_services()
        setrl_choice()
    elif ch == "3":
        st.add_sources()
        setrl_choice()
    elif ch == "4":
        st.add_source_port()
        setrl_choice()
    elif ch == "5":
        main_choice()
    else:
        gv.rpr("\tWrong choice")
        setrl_choice()


def main_choice():
    main_menu()
    ch = Prompt.ask("\tEnter your choice :",choices=["1","2","3","4"])
    if ch == "1":
        gv.get_status()
        main_choice()
    elif ch == "2":
        setrl_choice()
    elif ch == "3":
        dltrl_choice()
    elif ch == "4":
        exit()
    else:
        gv.rpr("\tWrong choice")
        main_choice()
        
main_choice()

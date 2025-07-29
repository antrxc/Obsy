import click
from art import tprint
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
import os
import datetime




def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    options = ["admin","dev"]    
    terminalMenu = TerminalMenu(options)
    menuEntryIndex = terminalMenu.show()
    match menuEntryIndex:
        case 0:
            Options=["Add User","Remove User", "Export Data CSV","Exit"]
            Menu = TerminalMenu(Options)
            Choice = Menu.show()
        case 1:
            Options = ["clock IN", "clock OUT", "Project Switch", "Exit"]
            Menu = TerminalMenu(Options)
            Choice = Menu.show()

    
    
    




tprint("aXtrLabs")
if __name__ == "__main__":
    main()
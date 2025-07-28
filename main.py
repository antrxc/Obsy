import click
from art import tprint
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
import os
import datetime




def main():
    options = ["clock-IN", "clock-OUT", "Project Switch"]
    terminalMenu = TerminalMenu(options)
    menuEntryIndex = terminalMenu.show()
    print(menuEntryIndex)
    




tprint("axtrLabs")
if __name__ == "__main__":
    main()
import click
from art import tprint
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
import os
import datetime
#from db.model import User, Role, addUser




def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    options = ["admin","dev"]    
    terminalMenu = TerminalMenu(options)
    menuEntryIndex = terminalMenu.show()
    while True:
        match menuEntryIndex:
            case 0:
                adminOptions=["Add User","Remove User", "Export Data CSV","Exit"]
                adminMenu = TerminalMenu(adminOptions)
                adminChoice = adminMenu.show()
                match adminChoice:
                    case 0:
                        user = User(
                            name= input("Name: "),
                            userID=input("User ID: "),
                            email=input("Email: "),
                            role=Role(input("Role (admin/dev): "))
                        )
                        addUser(user)

                    
            case 1:
                Options = ["clock IN", "clock OUT", "Project Switch", "Exit"]
                Menu = TerminalMenu(Options)
                Choice = Menu.show()
            case 2:
                quit()

    
    
    




tprint("aXtrLabs")
if __name__ == "__main__":
    main()
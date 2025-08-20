import click
from art import tprint
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
import os
import datetime
import csv
from db.model import addUser, removeUser, User, Role, Project, addProject
from commands.clock import clockIn, clockOUT_User
from commands.export import export_time_logs_csv, export_users_csv, export_projects_csv
from db.connection import UserData, ClockData, ProjectData


def get_current_user():
    """Get current user ID - in a real app this would be from authentication"""
    return input("Enter your User ID: ")

def list_projects():
    """List all available projects"""
    projects = ProjectData.find({})
    project_list = []
    for project in projects:
        project_list.append(f"{project['name']} ({project['domain']}) - {project['hours']}h")
    return project_list

def export_menu():
    """Show export options menu"""
    export_options = ["Export Time Logs", "Export Users", "Export Projects", "Export All", "Back"]
    export_menu = TerminalMenu(export_options, title="Export Options:")
    choice = export_menu.show()
    
    if choice is None or choice == 4:  # Back
        return
        
    try:
        match choice:
            case 0:  # Export Time Logs
                filename = export_time_logs_csv()
                print(f"{Fore.GREEN}✓ Time logs exported to {filename}{Style.RESET_ALL}")
            case 1:  # Export Users
                filename = export_users_csv()
                print(f"{Fore.GREEN}✓ Users exported to {filename}{Style.RESET_ALL}")
            case 2:  # Export Projects
                filename = export_projects_csv()
                print(f"{Fore.GREEN}✓ Projects exported to {filename}{Style.RESET_ALL}")
            case 3:  # Export All
                logs_file = export_time_logs_csv()
                users_file = export_users_csv()
                projects_file = export_projects_csv()
                print(f"{Fore.GREEN}✓ All data exported:")
                print(f"  - Time logs: {logs_file}")
                print(f"  - Users: {users_file}")
                print(f"  - Projects: {projects_file}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}✗ Export failed: {e}{Style.RESET_ALL}")

def export_to_csv():
    """Export time logs to CSV"""
    try:
        filename = export_time_logs_csv()
        print(f"Data exported to {filename}")
        return True
    except Exception as e:
        print(f"Export failed: {e}")
        return False

def main():
    tprint("Obsy")
    print(f"{Fore.CYAN}Welcome to Obsy Time Tracking System{Style.RESET_ALL}")
    print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    while True:
        options = ["Admin Panel", "Developer Panel", "Exit"]    
        terminalMenu = TerminalMenu(options, title="Select your role:")
        menuEntryIndex = terminalMenu.show()
        
        if menuEntryIndex is None:  # User pressed Ctrl+C
            break
            
        match menuEntryIndex:
            case 0:  # Admin Panel
                while True:
                    adminOptions = ["Add User", "Remove User", "Add Project", "Export Data CSV", "View All Users", "Back to Main Menu"]
                    adminMenu = TerminalMenu(adminOptions, title="Admin Panel:")
                    adminChoice = adminMenu.show()
                    
                    if adminChoice is None:
                        break
                        
                    match adminChoice:
                        case 0:  # Add User
                            print(f"\n{Fore.GREEN}=== Add New User ==={Style.RESET_ALL}")
                            name = input("Name: ")
                            userID = input("User ID: ")
                            email = input("Email: ")
                            role_str = input("Role (admin/dev): ")
                            try:
                                role = Role.from_string(role_str)
                                user = User(name, userID, email, role)
                                if addUser(user):
                                    print(f"{Fore.GREEN}✓ User {name} added successfully!{Style.RESET_ALL}")
                                else:
                                    print(f"{Fore.RED}✗ User with ID {userID} already exists!{Style.RESET_ALL}")
                            except ValueError:
                                print(f"{Fore.RED}✗ Invalid role: {role_str}. Please use 'admin' or 'dev'.{Style.RESET_ALL}")
                            input("\nPress Enter to continue...")
                            
                        case 1:  # Remove User
                            print(f"\n{Fore.YELLOW}=== Remove User ==={Style.RESET_ALL}")
                            userID = input("Enter User ID to remove: ")
                            user_data = UserData.find_one({"userID": userID})
                            if user_data:
                                user = User.from_dict(user_data)
                                if removeUser(user):
                                    print(f"{Fore.GREEN}✓ User {userID} removed successfully!{Style.RESET_ALL}")
                                else:
                                    print(f"{Fore.RED}✗ Failed to remove user {userID}{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}✗ User {userID} not found!{Style.RESET_ALL}")
                            input("\nPress Enter to continue...")
                            
                        case 2:  # Add Project
                            print(f"\n{Fore.GREEN}=== Add New Project ==={Style.RESET_ALL}")
                            name = input("Project Name: ")
                            domain = input("Project Domain: ")
                            project = Project(name, domain)
                            if addProject(project):
                                print(f"{Fore.GREEN}✓ Project {name} added successfully!{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}✗ Project {name} already exists!{Style.RESET_ALL}")
                            input("\nPress Enter to continue...")
                            
                        case 3:  # Export Data CSV
                            print(f"\n{Fore.BLUE}=== Export Data ==={Style.RESET_ALL}")
                            export_menu()
                            input("\nPress Enter to continue...")
                            
                        case 4:  # View All Users
                            print(f"\n{Fore.BLUE}=== All Users ==={Style.RESET_ALL}")
                            users = UserData.find({})
                            for user in users:
                                print(f"• {user['name']} ({user['userID']}) - {user['role']} - {user['email']}")
                            input("\nPress Enter to continue...")
                            
                        case 5:  # Back to Main Menu
                            break
                            
            case 1:  # Developer Panel
                userID = get_current_user()
                user_data = UserData.find_one({"userID": userID})
                if not user_data:
                    print(f"{Fore.RED}✗ User ID {userID} not found!{Style.RESET_ALL}")
                    input("Press Enter to continue...")
                    continue
                    
                print(f"\n{Fore.CYAN}Welcome, {user_data['name']}!{Style.RESET_ALL}")
                
                while True:
                    devOptions = ["Clock IN", "Clock OUT", "Project Switch", "View My Logs", "Back to Main Menu"]
                    devMenu = TerminalMenu(devOptions, title="Developer Panel:")
                    devChoice = devMenu.show()
                    
                    if devChoice is None:
                        break
                        
                    match devChoice:
                        case 0:  # Clock IN
                            print(f"\n{Fore.GREEN}=== Clock IN ==={Style.RESET_ALL}")
                            projects = list(ProjectData.find({}))
                            if not projects:
                                print(f"{Fore.RED}No projects available. Contact admin to add projects.{Style.RESET_ALL}")
                                input("Press Enter to continue...")
                                continue
                                
                            project_names = [p['name'] for p in projects]
                            project_menu = TerminalMenu(project_names, title="Select Project:")
                            project_choice = project_menu.show()
                            
                            if project_choice is not None:
                                selected_project = project_names[project_choice]
                                
                                # Check if already clocked in today
                                today = datetime.datetime.now().date()
                                existing_log = ClockData.find_one({
                                    "userID": userID, 
                                    "date": str(today),
                                    "clockOUT": None
                                })
                                
                                if existing_log:
                                    print(f"{Fore.YELLOW}⚠ You are already clocked in for today!{Style.RESET_ALL}")
                                else:
                                    log = clockIn(userID, selected_project)
                                    print(f"{Fore.GREEN}✓ Clocked IN at {log.clockIN.strftime('%H:%M:%S')} for project: {selected_project}{Style.RESET_ALL}")
                            input("\nPress Enter to continue...")
                            
                        case 1:  # Clock OUT
                            print(f"\n{Fore.YELLOW}=== Clock OUT ==={Style.RESET_ALL}")
                            today = datetime.datetime.now().date()
                            active_log = ClockData.find_one({
                                "userID": userID,
                                "date": str(today),
                                "clockOUT": None
                            })
                            
                            if not active_log:
                                print(f"{Fore.RED}✗ No active clock-in found for today!{Style.RESET_ALL}")
                            else:
                                if clockOUT_User(userID, datetime.datetime.now()):
                                    print(f"{Fore.GREEN}✓ Clocked OUT at {datetime.datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
                                else:
                                    print(f"{Fore.RED}✗ Failed to clock out!{Style.RESET_ALL}")
                            input("\nPress Enter to continue...")
                            
                        case 2:  # Project Switch
                            print(f"\n{Fore.BLUE}=== Project Switch ==={Style.RESET_ALL}")
                            projects = list(ProjectData.find({}))
                            if not projects:
                                print(f"{Fore.RED}No projects available.{Style.RESET_ALL}")
                                input("Press Enter to continue...")
                                continue
                                
                            project_names = [f"{p['name']} - {p['domain']} ({p['hours']}h)" for p in projects]
                            for i, project in enumerate(project_names):
                                print(f"{i+1}. {project}")
                            input("\nPress Enter to continue...")
                            
                        case 3:  # View My Logs
                            print(f"\n{Fore.BLUE}=== Your Time Logs ==={Style.RESET_ALL}")
                            logs = ClockData.find({"userID": userID}).sort("date", -1).limit(10)
                            for log in logs:
                                clock_in = log.get('clockIN', 'N/A')
                                clock_out = log.get('clockOUT', 'Not clocked out')
                                date = log.get('date', 'N/A')
                                project = log.get('project', 'N/A')
                                print(f"📅 {date} | 🏢 {project} | ⏰ {clock_in} - {clock_out}")
                            input("\nPress Enter to continue...")
                            
                        case 4:  # Back to Main Menu
                            break
                            
            case 2:  # Exit
                print(f"\n{Fore.GREEN}Thank you for using Obsy Time Tracking System!{Style.RESET_ALL}")
                break

if __name__ == "__main__":
    main()
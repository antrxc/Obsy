#!/usr/bin/env python3
"""
Setup script for aXtrLabs Login System
Creates initial admin user and sample project
"""

from db.model import addUser, addProject, User, Role, Project
from db.connection import UserData, ProjectData
from colorama import Fore, Style

def setup_initial_data():
    """Setup initial admin user and sample project"""
    print(f"{Fore.CYAN}=== aXtrLabs Login System Setup ==={Style.RESET_ALL}")
    
    # Check if admin user already exists
    admin_exists = UserData.find_one({"role": "admin"})
    if admin_exists:
        print(f"{Fore.YELLOW}⚠ Admin user already exists: {admin_exists['name']} ({admin_exists['userID']}){Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}Creating initial admin user...{Style.RESET_ALL}")
        name = input("Admin Name: ")
        userID = input("Admin User ID: ")
        email = input("Admin Email: ")
        
        admin_user = User(name, userID, email, Role.ADMIN)
        if addUser(admin_user):
            print(f"{Fore.GREEN}✓ Admin user created successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed to create admin user{Style.RESET_ALL}")
    
    # Check if any projects exist
    project_exists = ProjectData.find_one({})
    if project_exists:
        print(f"{Fore.YELLOW}⚠ Projects already exist in database{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}Creating sample project...{Style.RESET_ALL}")
        sample_project = Project("Sample Project", "Development")
        if addProject(sample_project):
            print(f"{Fore.GREEN}✓ Sample project created successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ Failed to create sample project{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}Setup complete! You can now run: python main.py{Style.RESET_ALL}")

if __name__ == "__main__":
    setup_initial_data()

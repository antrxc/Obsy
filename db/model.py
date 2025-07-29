'''
imports for the model.py file
Defines User and Project classes with helper functions for MongoDB operations.
Defines Role enum for user roles.
Defines functions for adding and removing users and projects.
Defines functions for checking user roles.
'''

from enum import Enum
from typing import Optional,List
from db.connection import UserData,ProjectData


class Role(Enum):
    ADMIN = "admin"
    DEV = "dev"

    @staticmethod
    def from_string(roleStr:str):
        for role in Role:
            if role.value == roleStr.lower():
                return role
        raise ValueError("Not valid role")

        
'''
Defines User class and functions: 
addUser(user:User) -> bool
removeUser(user:User) -> bool

TODO add functionalities: ListUsers

'''

class User:
    def __init__(self, name: str, userID: str, email: str, role: Role):
        self.name = name
        self.userID = userID
        self.email = email
        self.role = role

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "userID": self.userID,
            "email": self.email,
            "role": self.role.value
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            name=data.get("name", ""),
            userID=data.get("userID", ""),
            email=data.get("email", ""),
            role=Role.from_string(data.get("role", "dev"))
        )


'''
Defines Project class and functions:
addProject(project:Project) -> bool
statusUpdate(project:Project) -> bool
addHours(project:Project, hours:int) -> bool

'''

class Project:
    def __init__(self, name:str, domain:str):
        self.name = name
        self.domain = domain
        self.hours = 0
        self.status = "initiated"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "domain": self.domain,
            "hours": self.hours,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            name=data.get("name", ""),
            domain=data.get("domain", ""),
            hours=data.get("hours", "")
            status=data.get("status")
        )

    
#User CRUD functions 

def addUser(user:User)->bool:
    if UserData.find_one({"userID":user.userID}):
        return False
    UserData.insert_one(user.to_dict())
    return True


def removeUser(user:User)->bool:
    res = UserData.delete_one({"userID":user.userID})
    return res.delete_count > 0



#Project CRUD functions

def addProject(project:Project)->bool:
    if ProjectData.find_one({"name":project.name}):
        return False
    ProjectData.insert_one(project.to_dict())
    return True


def statusUpdate(project:Project)->bool:
    res = ProjectData.update_one(
        {"name": project.name}, 
        {"$set": {"status": project.status}}
    )
    return res.modified_count > 0

def addHours(project:Project, hours:int)-> bool:
    project.hours += hours
    res = ProjectData.update_one(
        {"name": project.name}, 
        {"$inc": {"hours": project.hours}}
    )
    return res.modified_count > 0

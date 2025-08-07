'''
Access control:

Admin -> can access anything and can make changes to anything
Dev -> can clockIN, clockOUT, switch projects


defines functions for checking user roles:
isAdmin(user:User) -> bool
isDev(user:User) -> bool
'''

from db.model import User, Role


def isAdmin(user: User) -> bool:
    if user.role == Role.ADMIN:
        return True
    return False

def isDev(user: User) -> bool:
    if user.role == Role.DEV:
        return True
    return False

def hasPermission(user: User, action: str) -> bool:
    """Check if user has permission for specific action"""
    if isAdmin(user):
        return True  # Admin can do everything
    
    if isDev(user):
        allowed_actions = ['clock_in', 'clock_out', 'view_logs', 'switch_project']
        return action in allowed_actions
    
    return False

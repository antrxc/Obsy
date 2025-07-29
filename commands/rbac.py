 '''
Access control:

Admin -> can access anything and can make changes to anything
Dev -> can clockIN, clockOUT, switch projects


defines functions for checking user roles:
isAdmin(user:User) -> bool
isDev(user:User) -> bool
'''

def isAdmin(user:User)->bool:
    if (user.role == ADMIN):
        return True
    return False

def isDev(user:User)->bool:
    if (user.role == DEV):
        return True
    return False

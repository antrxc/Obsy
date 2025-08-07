from datetime import datetime
from db.connection import ClockData
import os
'''
Defines Log class and functions:
clock_in(userID, project, time=None) -> Log
clockOUT_User(userID, time=None) -> bool
get_logs(userID=None, date=None) -> list[Log]
'''
class Log:
    def __init__(self, userID: str, clockIN: datetime, project: str):
        self.userID = userID
        self.clockIN = clockIN
        self.clockOUT = None  # Initialize as None
        self.project = project
        self.date = clockIN.date()
    
    def to_dict(self):
        return {
            "userID": self.userID,
            "clockIN": self.clockIN.isoformat(),
            "clockOUT": self.clockOUT.isoformat() if self.clockOUT else None,
            "date": str(self.date),
            "project": self.project
        }
    

def clockIn(userID: str, project: str) -> Log:
    clock_time = datetime.now()
    log = Log(userID,clock_time, project)
    ClockData.insert_one(log.to_dict())
    return log

def clockOUT_User(userID: str, time: datetime) -> bool:
    clock_time = time or datetime.now()
    result = ClockData.update_one(    
        {"userID": userID, "clockOUT": None},  # clockIN entry not clocked out yet
        {"$set": {"clockOUT": clock_time.isoformat()}}
    )
    return result.modified_count > 0
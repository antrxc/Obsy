from datetime import datetime
from db.connection import ClockData
import os

class Log:
    def __init__(self, userID: str, clockIN: datetime, project: str, date: str = None, clockOUT: datetime = None):
        self.userID = userID
        self.clockIN = clockIN
        self.clockOUT = clockOUT
        self.project = project
        self.date = date or clockIN.date()
    
    def to_dict(self):
        return {
            "userID": self.userID,
            "clockIN": self.clockIN.isoformat(),
            "clockOUT": self.clockOUT.isoformat() if self.clockOUT else None,
            "date": str(self.date),
            "project": self.project
        }
    
    def clock_out(self, time: datetime):
        self.clockOUT = time

def clock_in(userID: str, project: str, time: datetime = None) -> Log:
    clock_time = time or datetime.now()
    log = Log(userID=userID, clockIN=clock_time, project=project)
    
    clock_data = ClockData()
    clock_data.insert_clock_entry(log.to_dict())
    
    return log

def clock_out_user(userID: str, time: datetime = None) -> bool:
    clock_time = time or datetime.now()
    clock_time = datetime.now() if not clock_time else clock_time
    clock_data = ClockData()
    return clock_data.update_clock_out(userID, clock_time.isoformat())

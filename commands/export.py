"""
Export functionality for time tracking data
"""
import csv
import datetime
from db.connection import ClockData, UserData, ProjectData

def export_time_logs_csv(filename=None):
    """Export all time logs to CSV format"""
    if not filename:
        filename = f"time_logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        logs = ClockData.find({})
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['userID', 'userName', 'clockIN', 'clockOUT', 'date', 'project', 'hoursWorked']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for log in logs:
                # Get user name
                user = UserData.find_one({"userID": log.get('userID')})
                user_name = user['name'] if user else 'Unknown'
                
                # Calculate hours worked
                hours_worked = ""
                if log.get('clockIN') and log.get('clockOUT'):
                    try:
                        clock_in = datetime.datetime.fromisoformat(log['clockIN'])
                        clock_out = datetime.datetime.fromisoformat(log['clockOUT'])
                        duration = clock_out - clock_in
                        hours_worked = f"{duration.total_seconds() / 3600:.2f}"
                    except:
                        hours_worked = "Error calculating"
                
                writer.writerow({
                    'userID': log.get('userID', ''),
                    'userName': user_name,
                    'clockIN': log.get('clockIN', ''),
                    'clockOUT': log.get('clockOUT', ''),
                    'date': log.get('date', ''),
                    'project': log.get('project', ''),
                    'hoursWorked': hours_worked
                })
        
        return filename
    except Exception as e:
        raise Exception(f"Export failed: {e}")

def export_users_csv(filename=None):
    """Export all users to CSV format"""
    if not filename:
        filename = f"users_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        users = UserData.find({})
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'userID', 'email', 'role']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for user in users:
                writer.writerow({
                    'name': user.get('name', ''),
                    'userID': user.get('userID', ''),
                    'email': user.get('email', ''),
                    'role': user.get('role', '')
                })
        
        return filename
    except Exception as e:
        raise Exception(f"Export failed: {e}")

def export_projects_csv(filename=None):
    """Export all projects to CSV format"""
    if not filename:
        filename = f"projects_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        projects = ProjectData.find({})
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'domain', 'hours', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for project in projects:
                writer.writerow({
                    'name': project.get('name', ''),
                    'domain': project.get('domain', ''),
                    'hours': project.get('hours', 0),
                    'status': project.get('status', '')
                })
        
        return filename
    except Exception as e:
        raise Exception(f"Export failed: {e}")
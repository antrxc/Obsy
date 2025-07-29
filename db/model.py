from pymongo import MongoClient
from enum import Enum

class Role(enum):
    ADMIN = "admin"
    DEV = "dev"

class User:
    def __init__(self, name:str, userID:str,email:str, role:Role )->None:
        self.name=name
        self.userID=userID
        self.role=role
        self.email=email
    
    def todict(self):
        return {
            "name": self.name,
            "userID": self.userID,
            "email": self.email,
            "role": self.role.value  # store as string in Mongo
        }

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
dbName = client["aXtr-Logs"]
UserData = dbName["User-table"]

    
#Function to add new user
def addUser(user:User)->bool:
    exists = userData.find_one({"userID":user.userID})
    if exists:
        return False
    
    rec = dbName.UserData.insert(user.todict())
    return True 


    
    
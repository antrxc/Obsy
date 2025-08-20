# 🚀 Quick Start Guide - Obsy Login System

## Prerequisites
- Python 3.7+
- MongoDB (local or cloud)

## 5-Minute Setup

### 1. Setup Environment
```bash
# Clone and navigate
cd login-sys

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Database
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your MongoDB URI
# For local: MONGO_URI=mongodb://localhost:27017/
# For Atlas: MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/
```

### 3. Initialize System
```bash
python setup.py
```
Enter your admin details when prompted.

### 4. Run Application
```bash
python main.py
```

## First Time Usage

### As Admin (user001):
1. Select "Admin Panel"
2. Add some developers using "Add User"
3. Create projects using "Add Project"

### As Developer:
1. Select "Developer Panel"
2. Enter your User ID
3. Clock IN to start tracking time
4. Clock OUT when done

## Features Overview

### 👑 Admin Panel
- 👤 **User Management**: Add/remove users
- 📁 **Project Management**: Create and organize projects  
- 📊 **Data Export**: Export logs to CSV with hours calculation
- 👥 **View Users**: See all registered users

### 💻 Developer Panel
- ⏰ **Time Tracking**: Clock in/out with project selection
- 📈 **View Logs**: See your time tracking history
- 🔄 **Project Info**: Browse available projects

## Example Workflow

1. **Admin creates projects**: "Website Redesign", "API Development"
2. **Dev clocks in**: Select project → automatic time start
3. **Dev clocks out**: Time automatically calculated and saved
4. **Admin exports data**: Get CSV with user hours per project

## Troubleshooting

**Connection Issues**: Check your .env MONGO_URI
**Import Errors**: Ensure virtual environment is activated
**Menu Navigation**: Use arrow keys and Enter to select

---
🎉 **You're all set!** Your time tracking system is ready to use.

# Login System - axtrLabs

A terminal-based employee time tracking and login system with MongoDB integration.

## Features

- **Time Tracking**: Clock in/out functionality for employees
- **User Management**: Support for different user roles (Admin, Employee, Manager)
- **Terminal Interface**: Interactive menu-driven CLI using simple-term-menu
- **MongoDB Integration**: Persistent data storage for time logs and user data
- **Project Switching**: Support for switching between different projects

## Project Structure

```
login-sys/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── commands/           # Command modules
│   ├── __init__.py
│   ├── abac.py         # Access control (placeholder)
│   ├── clock.py        # Clock in/out functionality
│   └── export.py       # Data export functionality (placeholder)
├── db/                 # Database models and utilities
│   ├── __init__.py
│   └── model.py        # User model and database operations
└── utils/              # Utility functions
    └── __init__.py
```

## Requirements

- Python 3.7+
- MongoDB instance
- Required Python packages (see Installation section)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd login-sys
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your MongoDB connection string:
   ```env
   MONGO_URI=mongodb://localhost:27017/
   # OR for MongoDB Atlas:
   # MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
   ```

5. **Initialize the system**:
   ```bash
   python setup.py
   ```
   This will create an initial admin user and sample project.

## Usage

### Running the Application

```bash
source venv/bin/activate  # Activate virtual environment
python main.py
```

The application displays the axtrLabs ASCII logo and presents role-based menus.

### Admin Panel Features
- **Add User**: Create new users with admin or dev roles
- **Remove User**: Delete existing users from the system
- **Add Project**: Create new projects for time tracking
- **Export Data**: Export time logs, users, or projects to CSV
- **View All Users**: Display all registered users

### Developer Panel Features
- **Clock IN**: Start time tracking for a selected project
- **Clock OUT**: End current time tracking session
- **Project Switch**: View available projects and their details
- **View My Logs**: See your recent time tracking history
- **Back to Main Menu**: Return to role selection

### Database Schema

#### User Collection
```json
{
  "name": "John Doe",
  "userID": "unique_user_id",
  "email": "john@example.com",
  "role": "employee|manager|admin"
}
```

#### Time Logs Collection
```json
{
  "userID": "unique_user_id",
  "clockIN": "2025-07-28T09:00:00",
  "clockOUT": "2025-07-28T17:00:00",
  "date": "2025-07-28"
}
```

## Features in Detail

### Clock In/Out System
- Prevents duplicate clock-in entries for the same date
- Stores timestamp in ISO format
- Links entries to specific user IDs

### User Management
- Support for three role types: Admin, Employee, Manager
- User validation to prevent duplicate user IDs
- MongoDB integration for persistent storage

### Terminal Interface
- Colorful ASCII art banner
- Interactive menu navigation
- Real-time timestamp display

## Development Status

✅ **Project is now COMPLETE and fully functional!**

### ✅ Completed Features
- ✅ **Terminal Interface**: Beautiful ASCII art and colorful menus
- ✅ **User Management**: Add/remove users with role validation (Admin/Dev)
- ✅ **Time Tracking**: Complete clock in/out system with project assignment
- ✅ **Project Management**: Create and manage projects with status tracking
- ✅ **Data Export**: Export time logs, users, and projects to CSV format
- ✅ **Role-Based Access**: Admin and Developer panels with appropriate permissions
- ✅ **MongoDB Integration**: Full database operations with proper error handling
- ✅ **Data Validation**: Prevents duplicate entries and validates user inputs
- ✅ **Setup Script**: Automated initial system setup with admin user creation
- ✅ **Virtual Environment**: Proper Python environment management
- ✅ **Error Handling**: Comprehensive validation and user feedback
- ✅ **Time Calculation**: Automatic work hours calculation in exports

### 🎯 Key Improvements Made
- **Complete Menu System**: All menu options now fully implemented
- **Enhanced Export**: Multiple export formats with calculated hours
- **Better UX**: Colored output, clear feedback, and intuitive navigation
- **Robust Error Handling**: Graceful handling of edge cases
- **Proper Architecture**: Clean separation of concerns across modules
- **Production Ready**: Setup script, virtual environment, and proper dependencies

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Configuration

### Environment Variables
- `MONGO_URI`: MongoDB connection string (default: mongodb://localhost:27017/)

### Database Configuration
- Database name: `aXtr-Logs`
- Collections:
  - `TimeLogs`: Employee time tracking data
  - `User-table`: User information and roles

## License [subject to change]

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For support or questions, please contact the axtrLabs development team.
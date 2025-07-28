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

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   MONGO_URI=mongodb://localhost:27017/
   ```

4. **Install required packages** (if requirements.txt is empty):
   ```bash
   pip install pymongo click art colorama simple-term-menu python-dotenv
   ```

## Usage

### Running the Application

```bash
python main.py
```

The application will display the axtrLabs logo and present a menu with the following options:
- **clock-IN**: Record employee arrival time
- **clock-OUT**: Record employee departure time
- **Project Switch**: Switch between different projects

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

🚧 **This project is currently in development**

### Completed Features
- ✅ Basic terminal interface
- ✅ Clock in/out functionality
- ✅ User model structure
- ✅ MongoDB integration setup

### Planned Features
- 🔄 Access control system (ABAC)
- 🔄 Data export functionality
- 🔄 Project switching implementation
- 🔄 Error handling and validation
- 🔄 Logging and audit trails

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
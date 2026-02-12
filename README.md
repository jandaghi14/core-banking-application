# 🏦 Core Banking Application

A desktop banking application built with Python and Tkinter, featuring modern UI components, security features, and clean architecture principles.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![PIL](https://img.shields.io/badge/Images-Pillow-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 👨‍💻 Author

**Armin Yaghoubi**
- GitHub: [@arminyaghoubi](https://github.com/arminyaghoubi)
- LinkedIn: [Armin Yaghoubi](https://www.linkedin.com/in/arminyaghoubi1/)

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [License](#license)

## ✨ Features

### 🔐 Security
- **Password Hashing**: MD5 encryption for secure password storage
- **CAPTCHA System**: Image-based CAPTCHA with PIL for bot prevention
- **Input Validation**: Username and password validation rules

### 👤 User Management
- **User Registration**: Complete registration system with form validation
- **User Login**: Secure login with status checking (pending/active/inactive)
- **Session Management**: User status tracking and authentication

### 🎨 Modern UI Components
- **Custom Password Entry**: Eye icon toggle for show/hide password
- **CAPTCHA Component**: Reusable CAPTCHA with refresh functionality
- **Responsive Design**: Grid-based layout with proper spacing
- **Page Navigation**: Smooth transitions between Login and Register pages

### 🏗️ Clean Architecture
- **3-Layer Architecture**: Presentation → Business → Data Access
- **Dependency Injection**: Loose coupling between components
- **Repository Pattern**: Abstract data access layer
- **DTO Pattern**: Standardized response objects
- **Reusable Components**: Modular UI components

## 🏛️ Architecture

The application follows a clean 3-layer architecture:
```
┌─────────────────────────────────────┐
│      PRESENTATION LAYER             │
│  - Views (Login, Register)          │
│  - UI Components (Password, CAPTCHA)│
│  - View Manager (Navigation)        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      BUSINESS LOGIC LAYER           │
│  - Validation Rules                 │
│  - Password Hashing                 │
│  - Business Rules                   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      DATA ACCESS LAYER              │
│  - Repository Pattern               │
│  - SQLite Database                  │
│  - CRUD Operations                  │
└─────────────────────────────────────┘
```

## 🛠️ Technologies

- **Python 3.8+**
- **Tkinter**: GUI framework
- **Pillow (PIL)**: Image processing for CAPTCHA and icons
- **SQLite3**: Database management
- **hashlib**: Password encryption

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/arminyaghoubi/core-banking-application.git
cd core-banking-application
```

2. **Install dependencies**
```bash
pip install pillow
```

3. **Run the application**
```bash
python main.py
```

## 🚀 Usage

### First Time Setup

1. Run the application
2. Click "Go to Register" to create a new account
3. Fill in the registration form:
   - First Name
   - Last Name
   - Username (minimum 3 characters)
   - Password (minimum 6 characters)
   - Enter the CAPTCHA code
4. Click "Register"

### Login

1. Enter your username and password
2. Enter the CAPTCHA code
3. Click "Login"

### CAPTCHA

- The CAPTCHA refreshes automatically after each attempt
- Click the "🔄 Refresh" button to generate a new CAPTCHA
- CAPTCHA is case-insensitive

### Password Visibility

- Click the eye icon to toggle password visibility
- 🔒 Closed eye = password hidden
- 👁️ Open eye = password visible

## 📁 Project Structure
```
core-banking-application/
├── main.py                              # Application entry point
├── CoreBankingDB.db                     # SQLite database
├── Presentation/
│   └── Desktop/
│       ├── window.py                    # Custom Tkinter window
│       ├── view_manager.py              # Page navigation manager
│       ├── Frames/
│       │   ├── login.py                 # Login page
│       │   └── register.py              # Register page
│       └── UiComponents/
│           ├── password_entry.py        # Password input with eye icon
│           ├── captcha_component.py     # CAPTCHA generator
│           └── assets/
│               ├── open_eye.png         # Open eye icon
│               └── close_eye.png        # Closed eye icon
├── Business/
│   └── employee_business.py             # Business logic layer
├── DataAccess/
│   └── Repositories/
│       └── SQLiteRepositories/
│           └── employee_repository.py   # Data access layer
├── Common/
│   ├── Entities/
│   │   └── employee.py                  # Employee entity
│   ├── DTO/
│   │   └── response.py                  # Response object
│   └── Repositories/
│       └── iemployee_repository.py      # Repository interface
└── README.md
```

## 📸 Screenshots

### Login Page
- Clean login interface
- CAPTCHA verification
- Password toggle with eye icon

### Register Page
- User-friendly registration form
- Real-time validation
- CAPTCHA security

### CAPTCHA Component
- Random text generation
- Visual noise for security
- Refresh functionality

## 🔑 Key Concepts Demonstrated

### Design Patterns
- **Repository Pattern**: Abstract data access
- **Dependency Injection**: Loose coupling
- **Factory Pattern**: Frame creation
- **Observer Pattern**: Event handling
- **DTO Pattern**: Data transfer objects

### Security Best Practices
- Password hashing (never store plain text)
- CAPTCHA bot prevention
- Input validation and sanitization
- SQL injection prevention (parameterized queries)

### Software Engineering Principles
- **Separation of Concerns**: 3-layer architecture
- **Single Responsibility**: Each class has one purpose
- **DRY (Don't Repeat Yourself)**: Reusable components
- **Open/Closed Principle**: Easy to extend
- **Interface Segregation**: Abstract base classes

## 📝 Database Schema
```sql
Table: Employee
- Id (INTEGER PRIMARY KEY)
- FirstName (TEXT)
- LastName (TEXT)
- Username (TEXT UNIQUE)
- Password (TEXT)  -- MD5 hashed
- EmployeeStatusId (INTEGER)
  -- 1: Pending
  -- 2: Active
  -- 3: Inactive
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as part of Python Development course
- Inspired by modern banking application UX
- Special thanks to the Tkinter and PIL communities

## 📧 Contact

Armin Yaghoubi
- GitHub: [@arminyaghoubi](https://github.com/arminyaghoubi)
- LinkedIn: [Armin Yaghoubi](https://www.linkedin.com/in/arminyaghoubi1/)

---

⭐ **Star this repository if you find it helpful!**
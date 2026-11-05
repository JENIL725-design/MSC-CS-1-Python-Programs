MSC-CS-1-Python-Programs 🚀

This repository contains a comprehensive collection of Python programs completed for the M.Sc. Cyber Security coursework. The practicals cover a wide range of topics from fundamental programming to database management, data visualization, and network security concepts.

Author: Jenil N Makwana

Enrollment: 92600565009

Program: M.Sc. Cyber Security

Repository: JENIL725-design/MSC-CS-1-Python-Programs

📚 Topics Covered

The repository is structured around 50 practical assignments, encompassing the following key areas:

Core Python: Variables, loops, conditionals, functions, and file handling (I/O).

Object-Oriented Programming (OOP): Classes, objects, inheritance, and exception handling.

Database Management: MySQL integration, creating databases, and performing CRUD (Create, Read, Update, Delete) operations using mysql.connector.

Data Science & Visualization: Data manipulation with DataFrames and data visualization (Pie, Bar, Line, Histogram) using pandas and matplotlib.

Networking & Security:

WHOIS domain lookups

DNS resolution and IP extraction (socket)

Subprocess execution for network commands (nslookup)

Cryptographic hashing (MD5, SHA-256) using hashlib

🛠️ Technologies & Libraries

Language: Python 3.x

Database: MySQL (via XAMPP / Laragon)

Key Libraries Used:

mysql-connector-python (Database connectivity)

pandas (DataFrames and data structures)

matplotlib (Graph plotting and data visualization)

python-whois (Domain registration lookups)

Built-in modules: socket, subprocess, hashlib, os

⚙️ Setup & Installation

1. Clone the repository:

git clone https://github.com/JENIL725-design/MSC-CS-1-Python-Programs.git
cd MSC-CS-1-Python-Programs


2. Install dependencies:
Make sure Python is installed on your Windows machine, then run:

pip install mysql-connector-python pandas matplotlib python-whois


3. Database Configuration (For MySQL Practicals):
Ensure your local MySQL server is running. The scripts are configured to connect to localhost with the default credentials.

🚀 How to Run

Navigate to the directory in your terminal (e.g., VS Code integrated terminal) and execute the files using the py command:

# Example: Running Practical 50
py 50.py


📌 Note on Network Commands (Practical 45)

Practical 45 involves performing DNS lookups via terminal commands. Since the dig command is native to Linux, the script has been optimized for Windows environments using the native nslookup command via the subprocess module to ensure flawless execution without requiring BIND9 tools or WSL.

MSC-CS-1-Python-Programs 🚀

This repository contains a comprehensive collection of Python programs completed for the M.Sc. Cyber Security coursework at Marwadi University. The practicals cover a wide range of topics from fundamental programming to database management, data visualization, and network security concepts.

Author: Jenil N Makwana

Enrollment: 92600565009

Program: M.Sc. Cyber Security

Repository: JENIL725-design/MSC-CS-1-Python-Programs

📁 File Directory & Code Mapping

Below is the complete breakdown of all 50 practical files in this repository and what each program does:

Part 1: Core Python Fundamentals

1.py to 32.py: These files cover the foundational concepts of Python programming, including variables, data types, control flow (if/else), loops (for/while), functions, and basic data structures (Lists, Dictionaries, Tuples, Sets). (Note: Refer to the specific file headers for the exact aim of each program in this range).

Part 2: Database Management (MySQL)

33.py: Connects to a local MySQL server and creates a database and tables.

34.py: Performs complete CRUD (Create, Read, Update, Delete) operations using mysql.connector.

Part 3: Data Science & Visualization

35.py: Demonstrates the basic use of Pandas DataFrames to structure data.

36.py: Explores different ways to create DataFrames (Dictionaries, Lists, Series).

37.py: Creates a Pie Chart using Matplotlib.

38.py: Creates a Histogram using Matplotlib.

39.py: Creates a Bar Graph using Matplotlib.

40.py: Creates a Line Graph using Matplotlib.

Part 4: Networking & Cyber Security Tools

41.py: Hardcoded WHOIS lookup to fetch domain registration details.

42.py: Interactive WHOIS lookup that accepts a domain name from the user.

43.py: Advanced WHOIS parsing to extract specific Name Servers and Contact Emails.

44.py: Uses the socket module to find the IPv4 address of a given domain name.

45.py: Uses the subprocess module to run native OS commands (nslookup) for DNS record retrieval.

46.py: Uses the hashlib module to generate secure cryptographic hashes (MD5 and SHA-256) of strings.

Part 5: System Operations & Advanced Concepts

47.py: Uses the os module to fetch the Current Working Directory (CWD) and list all local files.

48.py: Demonstrates robust Exception Handling using try, except, and finally blocks (e.g., handling ZeroDivisionError).

49.py: Demonstrates File I/O Handling (creating, writing to, and reading from a .txt file).

50.py: Demonstrates Object-Oriented Programming (OOP) concepts by building a Student class and creating instantiated objects.

🛠️ Technologies & Libraries

Language: Python 3.x

Database: MySQL (via XAMPP / Laragon)

External Libraries Required:

mysql-connector-python

pandas

matplotlib

python-whois

Built-in Modules Used: socket, subprocess, hashlib, os

⚙️ Setup & Installation

1. Clone the repository:

git clone https://github.com/JENIL725-design/MSC-CS-1-Python-Programs.git
cd MSC-CS-1-Python-Programs


2. Install dependencies:
Make sure Python is installed, then run the following in your terminal:

pip install mysql-connector-python pandas matplotlib python-whois


3. Database Configuration (For MySQL Practicals):
Ensure your local MySQL server (like XAMPP) is active. The scripts are configured to connect to localhost with the default root user credentials.

🚀 How to Run

Navigate to the directory in your terminal and execute the files using the standard Python command. Since these are numbered, just call the specific file:

# Example: Running the WHOIS lookup program
py 41.py

# Example: Running the Matplotlib Bar Graph program
py 39.py


📌 Note on Network Commands (Practical 45)

Practical 45 involves performing DNS lookups via terminal commands. Since the dig command is native to Linux, the script has been optimized for Windows environments using the native nslookup command via the subprocess module to ensure flawless execution.

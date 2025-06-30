# HTX xCode Technical Assessment - Backend

## 🧾 Overview
This repository provides a simple Python-based Command-line interface (CLI) application for checking if an input is a valid palindrome. 

It contains two core functionalities:
1. **String Palindrome Check** – Determines whether a given string is a palindrome by ignoring punctuation, spaces, and case sensitivity.
2. **Number Palindrome Check** – Determines whether a given integer is a numeric palindrome without converting the number to a string.

### 🧰 Features

- ✅ Simple CLI with menu-driven interaction
- ✅ **String Palindrome Check**: Cleans and normalizes string input before checking
- ✅  **Number Palindrome Check**: Handles numeric palindrome check without string conversion
- ✅ Validates input types and constraints
- ✅ Includes unit tests for both string and numeric checkers using `pytest`

## 🛠 Prerequisites

Ensure you have the following installed:

- Python 3.10+
- Git

## 📦 Setup

1. **Clone or download the repo as zip file:**

   ```bash
   git clone https://github.com/xihao-zhou/xihao-htx-tech-assessment-be.git
   cd xihao-htx-tech-assessment-be
   ```

2. **Create and activate a virtual environment:**

   **Linux/MacOs**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

   deactivate #command to deactivate virtual environment
   ```

   **Windows**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate

   deactivate #command to deactivate virtual environment
   ```
   
3. **Install dependencies:**
   
   **Linux/MacOs**
   ```bash
   pip3 install -r requirements.txt
   ```

   **Windows**
   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Running the App

   **Linux/MacOs**
   ```bash
   # Running as simple CLI App
   python3 app/main.py

   # Running script for each question independently

   ## Question 1: Palindrome Check
   python3 app/palindrome_check.py --input [Enter a string to perform palindrome check.]

   ## Question 2: Number Palindrome Check
   python3 app/num_palindrome_check.py --input [Enter a number to perform palindrome check.]
   ```
   
   **Windows**
   ```bash
   # Running as simple CLI App
   python .\app\main.py

   # Running script for each question independently

   ## Question 1: Palindrome Check
   python .\app\palindrome_check.py --input [Enter a string to perform palindrome check.]

   ## Question 2: Number Palindrome Check
   python .\app\num_palindrome_check.py --input [Enter a number to perform palindrome check.]
   ```

## ✅ Running Unit Tests
   ```bash
   # Run tests for whole app 
   pytest -v test

   # Run tests for or each question independently

   ## Question 1: Palindrome Check
   pytest -v test/palindrome_check_test.py

   ## Question 2: Number Palindrome Check
   pytest -v test/nunm_palindrome_check_test.py
   ```

## 📁 Project Struture

```plaintext
xihao-htx-tech-assessment-be/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── num_palindrome_check.py
│   └── palindrome_check.py
├── tests/
│   ├── __init__.py
│   ├── palindrome_check_test.py
│   └── num_palindrome_check_test.py
├── requirements.txt
└── README.md
```
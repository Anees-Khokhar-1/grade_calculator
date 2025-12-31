# 🎓 Grade Calculator (Python CLI)

A **professional Python console application** that calculates student grades, generates a **class merit list**, identifies **position holders (1st, 2nd, 3rd)**, and exports results to CSV files. This project is beginner-friendly yet structured for real-world usage.

---

## 🔍 Features

✔ Supports **multiple students**  
✔ Accepts both **default and custom subjects**  
✔ Calculates:
- Total marks
- Average marks
- Grade (A+, A, B, C, D, F)

✔ Generates:
- Full **class merit list**
- **Position holders** (top 3 based on average)

✔ Handles **tie positions** correctly  
✔ Exports results to CSV files (`results.csv`, `position_holders.csv`)  
✔ Clean, modular project structure

---

## 📁 Project Structure

grade_calculator/
│
├── grade_calculator/
│ ├── init.py
│ ├── grading.py # Total and grade calculation logic
│ ├── ranking.py # Merit list & ranking logic
│ ├── export.py # CSV export logic
│ └── cli.py # Command-line interface
│
├── data/
│ ├── results.csv
│ └── position_holders.csv
│
├── tests/ # (Optional) Your future unit tests
│
├── run.py # Main entry point
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy code

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Anees-Khokhar-1/grade_calculator.git
cd grade_calculator
2. Run the application
bash
Copy code
python run.py
Follow the on-screen prompts to enter subjects and student marks.

💾 Exported Output
Results will be saved to:

File	Description
data/results.csv	Full list of students, totals, averages, and grades
data/position_holders.csv	Top 3 position holders with positions, averages, and grades

🧠 What This Project Does
Asks for default subjects or allows custom subjects

Accepts marks for each student

Calculates total and average marks

Assigns grades using a standard grading scale

Ranks students based on average

Displays academic ranking in the terminal

Saves results and toppers to CSV

📦 Requirements
Python 3.8 or higher

No external libraries required (only built-in modules)

Flask, pandas, and numpy were listed in the original requirements but are not used in this CLI version. You can add them later for web or analytics features.

🛠️ Next Improvements (Optional)
You may choose to extend this project with:

✨ A Flask web interface
📊 Visual charts of class performance
📄 Export to Excel or PDF formats
🏅 Certificates for position holders
🧪 Unit tests (pytest integration)

👨‍💻 About
Grade Calculator is a CLI-based Python project designed for education, small classes, and learning purposes. It is structured to be both simple and scalable, perfect for showcasing in portfolios or GitHub profiles.


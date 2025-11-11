# grade_calculator.py
"""
Student Grade Calculator
- Input marks for multiple subjects
- Calculates total, average, and grade
- Optionally saves results to a CSV file
"""

import csv
from typing import List, Tuple

SUBJECTS_DEFAULT = ["Math", "Physics", "Chemistry", "English", "Computer"]

def calculate_total_and_average(marks: List[float]) -> Tuple[float, float]:
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    return total, average

def assign_grade(average: float) -> str:
    # Classic grade boundaries
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"

def input_marks(subjects: List[str]) -> List[float]:
    marks = []
    for sub in subjects:
        while True:
            try:
                val = input(f"Enter marks for {sub} (0-100): ").strip()
                mark = float(val)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def save_results_csv(filename: str, results: List[dict]):
    keys = ["name", "total", "average", "grade"]
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print(f"Results saved to {filename}")

def main():
    print("=== Student Grade Calculator ===")
    subjects = SUBJECTS_DEFAULT.copy()
    print("Default subjects:", ", ".join(subjects))
    custom = input("Do you want to edit subject list? (y/N): ").strip().lower()
    if custom == "y":
        subjects = []
        n = int(input("How many subjects? "))
        for i in range(n):
            subjects.append(input(f"Name of subject #{i+1}: ").strip())

    results = []
    while True:
        name = input("\nEnter student name (or press Enter to quit): ").strip()
        if name == "":
            break
        marks = input_marks(subjects)
        total, average = calculate_total_and_average(marks)
        grade = assign_grade(average)
        print(f"\n{name} -> Total: {total:.2f}, Average: {average:.2f}, Grade: {grade}")
        results.append({"name": name, "total": f"{total:.2f}", "average": f"{average:.2f}", "grade": grade})

    if results:
        save = input("\nSave results to CSV? (Y/n): ").strip().lower()
        if save != "n":
            filename = input("Enter filename (default results.csv): ").strip() or "results.csv"
            save_results_csv(filename, results)

    print("Goodbye!")

if __name__ == "__main__":
    main()

from typing import List
from .grading import calculate_total_and_average, assign_grade
from .ranking import rank_students, get_position_holders
from .export import save_results_csv, save_position_holders_csv


DEFAULT_SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Computer"]


def input_marks(subjects: List[str]) -> List[float]:
    marks = []
    for sub in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {sub} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")
    return marks


def display_merit_list(ranked_results: List[dict]):
    print("\n📋 CLASS MERIT LIST")
    print("-" * 50)
    for s in ranked_results:
        print(
            f"{s['position']:>2} | {s['name']:<15} "
            f"| Avg: {s['average']:.2f} "
            f"| Grade: {s['grade']}"
        )


def display_position_holders(position_holders: List[dict]):
    print("\n🏆 POSITION HOLDERS")
    print("-" * 50)
    for s in position_holders:
        print(
            f"{s['position']} Position: {s['name']} "
            f"({s['average']:.2f}%)"
        )


def start_cli():
    print("=== Student Grade Calculator ===")

    subjects = DEFAULT_SUBJECTS.copy()
    if input("Edit subject list? (y/N): ").lower() == "y":
        subjects = []
        count = int(input("How many subjects? "))
        for i in range(count):
            subjects.append(input(f"Subject {i+1} name: ").strip())

    results = []

    while True:
        name = input("\nEnter student name (or press Enter to finish): ").strip()
        if not name:
            break

        marks = input_marks(subjects)
        total, average = calculate_total_and_average(marks)
        grade = assign_grade(average)

        print(f"{name} → Total: {total:.2f}, Average: {average:.2f}, Grade: {grade}")

        results.append({
            "name": name,
            "total": total,
            "average": average,
            "grade": grade
        })

    if not results:
        print("No data entered.")
        return

    ranked_results = rank_students(results)
    position_holders = get_position_holders(ranked_results)

    display_merit_list(ranked_results)
    display_position_holders(position_holders)

    if input("\nSave results to CSV? (Y/n): ").lower() != "n":
        save_results_csv("data/results.csv", ranked_results)
        print("Results saved to data/results.csv")

    if input("Save position holders to CSV? (Y/n): ").lower() != "n":
        save_position_holders_csv("data/position_holders.csv", position_holders)
        print("Position holders saved to data/position_holders.csv")

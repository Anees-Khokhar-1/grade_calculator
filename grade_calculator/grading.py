from typing import List, Tuple


def calculate_total_and_average(marks: List[float]) -> Tuple[float, float]:
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    return total, average


def assign_grade(average: float) -> str:
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

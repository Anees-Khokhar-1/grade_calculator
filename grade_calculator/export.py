import csv
from typing import List


def save_results_csv(filename: str, results: List[dict]):
    fieldnames = ["name", "total", "average", "grade"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "name": r["name"],
                "total": f"{r['total']:.2f}",
                "average": f"{r['average']:.2f}",
                "grade": r["grade"]
            })


def save_position_holders_csv(filename: str, position_holders: List[dict]):
    fieldnames = ["position", "name", "average", "grade"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for s in position_holders:
            writer.writerow({
                "position": s["position"],
                "name": s["name"],
                "average": f"{s['average']:.2f}",
                "grade": s["grade"]
            })

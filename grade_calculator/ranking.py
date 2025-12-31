from typing import List


def rank_students(results: List[dict]) -> List[dict]:
    # Sort by average descending
    sorted_results = sorted(
        results,
        key=lambda x: x["average"],
        reverse=True
    )

    position = 1
    for i, student in enumerate(sorted_results):
        if i > 0 and student["average"] == sorted_results[i - 1]["average"]:
            student["position"] = sorted_results[i - 1]["position"]
        else:
            student["position"] = position
        position += 1

    return sorted_results


def get_position_holders(ranked_results: List[dict], top_n: int = 3) -> List[dict]:
    return [s for s in ranked_results if s["position"] <= top_n and s["grade"] != "F"]

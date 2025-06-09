from .models import Employee, Building
from typing import Callable, List, Tuple

Filter = Callable[[Employee], bool]

def requirements(building: Building) -> List[Tuple[Filter, int]]:
    if building.type == "single":
        return [(lambda e: e.role == "certified", 1)]
    if building.type == "two":
        return [
            (lambda e: e.role == "certified", 1),
            (lambda e: e.role in {"pending", "laborer"}, 1),
        ]
    if building.type == "commercial":
        return [
            (lambda e: e.role == "certified", 2),
            (lambda e: e.role == "pending", 2),
            (lambda e: True, 4),
        ]
    raise ValueError(f"Unknown building type {building.type}")

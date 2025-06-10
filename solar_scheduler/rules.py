from .models import Employee, Building
from typing import Callable, List, Tuple

Filter = Callable[[Employee], bool]

def requirements(building: Building) -> List[Tuple[Filter, int]]:
    """
    Returns a list of (filter, count) tuples specifying how many employees
    matching each filter are required for the given building type.
    """

    if building.type == "single":
        # Needs exactly 1 certified installer
        return [(lambda e: e.role == "certified", 1)]
    if building.type == "two":
        # Needs exactly 1 certified installer and 1 pending-certification installer or laborer
        return [
            (lambda e: e.role == "certified", 1),
            (lambda e: e.role in {"pending", "laborer"}, 1),
        ]
    if building.type == "commercial":
        # Needs exactly 2 certified installers, 2 pending-certification installers, and 4 laborers
        return [
            (lambda e: e.role == "certified", 2),
            (lambda e: e.role == "pending", 2),
            (lambda e: True, 4),
        ]
    # Unknown building type
    raise ValueError(f"Unknown building type {building.type}")

from typing import Dict, List, Tuple
from .models import Building, Employee
from .rules import requirements


def schedule(
    buildings: List[Building],
    employees: List[Employee],
) -> Dict[int, List[Tuple[Building, List[Employee]]]]:
    """
    Schedule buildings for the next 5 days (Monday to Friday).
    Each employee can only work on one building per day, but can work on different days.
    Employee availability resets each day.

    Args:
        buildings: List of buildings to schedule
        employees: List of employees with their available days

    Returns:
        Dictionary mapping days (0=Monday to 4=Friday) to lists of tuples of (building, crew)
    """
    # Map day indices
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    # Initialize empty schedule for each day
    plan = {day: [] for day in range(5)}

    # Process each building in order
    for building in buildings:
        # Try to schedule the building on the earliest possible day
        for day in range(5):
            # Skip if employee isn't available this day
            available_employees = [
                e for e in employees if day_names[day] in e.available_days
            ]
            # Filter out employees already assigned to a building this day
            assigned_employee_ids = {e.id for b, crew in plan[day] for e in crew}
            available_employees = [
                e for e in available_employees if e.id not in assigned_employee_ids
            ]

            # Try to build a crew that meets all requirements
            crew: List[Employee] = []
            crew_ids = set()

            for filter, amount in requirements(building):
                # Find available employees matching the filter and not already in crew
                matches = [
                    e for e in available_employees if filter(e) and e.id not in crew_ids
                ]

                if len(matches) < amount:
                    break  # Not enough employees for this requirement

                # Add the required number of employees to the crew
                selected = matches[:amount]
                crew.extend(selected)
                crew_ids.update(e.id for e in selected)

            else:  # All requirements met
                plan[day].append((building, crew))
                break  # Move to next building

    return plan

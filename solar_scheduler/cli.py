from solar_scheduler.models import Employee, Building
from solar_scheduler.scheduler import schedule


import random


def random_availability(available_prob=0.8):
    """Generate a random availability list with given probability of being available.

    Returns:
        List of day names (e.g., ["Mon", "Tue", "Fri"]) that the employee is available
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    return [day for day in days if random.random() < available_prob]


def demo_data():
    # Create employees with random but realistic availability patterns
    # Each employee is available on each day with 80% probability by default
    employees = [
        # Certified installers
        Employee(
            id=1,
            role="certified",
            name="Certified 1",
            available_days=random_availability(0.9),  # 90% available
        ),
        Employee(
            id=2,
            role="certified",
            name="Certified 2",
            available_days=random_availability(0.8),
        ),
        Employee(
            id=3,
            role="certified",
            name="Certified 3",
            available_days=random_availability(0.7),  # Less available
        ),
        # Pending certification
        Employee(
            id=4,
            role="pending",
            name="Pending 1",
            available_days=random_availability(0.8),
        ),
        Employee(
            id=5,
            role="pending",
            name="Pending 2",
            available_days=random_availability(0.8),
        ),
        Employee(
            id=6,
            role="pending",
            name="Pending 3",
            available_days=random_availability(0.7),  # Less available
        ),
        # Laborers
        Employee(
            id=7,
            role="laborer",
            name="Laborer 1",
            available_days=random_availability(0.8),
        ),
        Employee(
            id=8,
            role="laborer",
            name="Laborer 2",
            available_days=random_availability(0.6),  # Part-time
        ),
        Employee(
            id=9,
            role="laborer",
            name="Laborer 3",
            available_days=random_availability(0.9),  # Mostly available
        ),
        Employee(
            id=10,
            role="laborer",
            name="Laborer 4",
            available_days=random_availability(0.5),  # Only half available
        ),
    ]
    # Buildings are processed in the order they appear in this list
    # Earlier buildings have higher priority for scheduling
    buildings = [
        # High priority buildings (will be scheduled first)
        Building(id=1, type="commercial"),
        Building(id=2, type="single"),
        Building(id=3, type="two"),
        # Medium priority buildings
        Building(id=4, type="commercial"),
        Building(id=5, type="single"),
        Building(id=6, type="two"),
        # Lower priority buildings
        Building(id=7, type="commercial"),
        Building(id=8, type="single"),
        Building(id=9, type="two"),
        # Lowest priority buildings (will be scheduled last)
        Building(id=10, type="commercial"),
        Building(id=11, type="single"),
        Building(id=12, type="two"),
        Building(id=13, type="commercial"),
    ]

    return buildings, employees


def format_crew(crew):
    """Format crew list with role and id (e.g., 'C1' for certified employee 1)"""
    return [f"{e.role[0].upper()}{e.id}" for e in crew]


def get_unscheduled_buildings(buildings, scheduled_ids):
    """Return list of buildings that haven't been scheduled yet"""
    return [b for b in buildings if b.id not in scheduled_ids]


def main():
    buildings, employees = demo_data()

    if not buildings:
        print("No buildings provided for scheduling. Exiting.")
        return

    if not employees:
        print("No employees available for scheduling. Exiting.")
        return

    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    week_number = 1
    scheduled_building_ids = set()

    while True:
        # Get buildings not yet scheduled
        remaining_buildings = get_unscheduled_buildings(
            buildings, scheduled_building_ids
        )

        if not remaining_buildings:
            print("ALL BUILDINGS HAVE BEEN SCHEDULED!")
            break

        # Print week header
        print("-" * 60)
        print(f"WEEK {week_number}")
        print("-" * 60)

        # Schedule remaining buildings for this week
        plan = schedule(remaining_buildings, employees)

        # Track newly scheduled buildings this week
        new_scheduled = set()

        # Print each day's schedule
        for day_idx, day_name in enumerate(day_names):
            print(f"{day_name}:")
            print("-" * (len(day_name) + 1))

            day_assignments = plan.get(day_idx, [])

            if not day_assignments:
                print("  No buildings scheduled\n")
                continue

            for building, crew in day_assignments:
                crew_list = ", ".join(format_crew(crew))
                print(f"  Building {building.id} ({building.type}) -> {crew_list}")
                new_scheduled.add(building.id)
            print()

        # Update scheduled buildings
        scheduled_building_ids.update(new_scheduled)

        # Calculate and print weekly summary
        total_buildings = len(buildings)
        scheduled_buildings = len(scheduled_building_ids)
        pending_buildings = total_buildings - scheduled_buildings

        print("-" * 40)
        print(f"WEEK {week_number} SUMMARY")
        print(f"Buildings scheduled this week: {len(new_scheduled)}")
        print(f"Total scheduled to date:      {scheduled_buildings}/{total_buildings}")
        print(f"Remaining buildings:          {pending_buildings}")
        print("-" * 40)

        if pending_buildings > 0:
            pending_buildings = [b for b in buildings if b.id not in scheduled_building_ids]
            pending_ids = [str(b.id) for b in pending_buildings]
            print(f"\nPending Building IDs: {', '.join(pending_ids)}")

        # Prevent infinite loop if no progress is made
        if not new_scheduled and pending_buildings:
            print("\nCould not schedule any of the remaining buildings with the current employee availability.")
            print("Further scheduling attempts would result in an infinite loop. Exiting.")
            break

        week_number += 1


if __name__ == "__main__":
    main()

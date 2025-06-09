from solar_scheduler.models import Employee, Building
from solar_scheduler.scheduler import schedule


def demo_data():
    # Using numeric IDs and string availability markers
    emp = [
        Employee(
            id=1,
            role="certified",
            name="Certified 1",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=2,
            role="certified",
            name="Certified 2",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=3,
            role="certified",
            name="Certified 3",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=4,
            role="pending",
            name="Pending 1",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=5,
            role="pending",
            name="Pending 2",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=6,
            role="pending",
            name="Pending 3",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=7,
            role="laborer",
            name="Laborer 1",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=8,
            role="laborer",
            name="Laborer 2",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
        Employee(
            id=9,
            role="laborer",
            name="Laborer 3",
            available_days=["Mon", "Tue", "Wed", "Thu", "Fri"],
        ),
    ]
    bld = [
        Building(id=1, type="commercial"),
        Building(id=2, type="single"),
        Building(id=3, type="two"),
        Building(id=4, type="commercial"),
        Building(id=5, type="single"),
        Building(id=6, type="two"),
        Building(id=7, type="commercial"),
        Building(id=8, type="single"),
        Building(id=9, type="two"),
        Building(id=10, type="commercial"),
        Building(id=11, type="single"),
        Building(id=12, type="two"),
        Building(id=13, type="commercial"),
    ]
    return bld, emp


def format_crew(crew):
    """Format crew list with role and id (e.g., 'C1' for certified employee 1)"""
    return [f"{e.role[0].upper()}{e.id}" for e in crew]


def get_unscheduled_buildings(buildings, scheduled_ids):
    """Return list of buildings that haven't been scheduled yet"""
    return [b for b in buildings if b.id not in scheduled_ids]


def main():
    all_buildings, employees = demo_data()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    week_number = 1
    scheduled_building_ids = set()

    while True:
        # Get buildings not yet scheduled
        remaining_buildings = get_unscheduled_buildings(all_buildings, scheduled_building_ids)

        if not remaining_buildings:
            print("\n" + "=" * 60)
            print("ALL BUILDINGS HAVE BEEN SCHEDULED!".center(60))
            print("=" * 60)
            break

        # Print week header
        print("\n" + "#" * 60)
        print(f" WEEK {week_number} ".center(60, "#"))
        print("#" * 60 + "\n")

        # Schedule remaining buildings for this week
        plan = schedule(remaining_buildings, employees)

        # Track newly scheduled buildings this week
        new_scheduled = set()

        # Print each day's schedule
        for day_idx, day_name in enumerate(day_names):
            print(f"{day_name}:")
            print("-" * (len(day_name) + 1))

            day_assignments = plan[day_idx] if day_idx < len(plan) else []

            if not day_assignments:
                print("  No buildings scheduled\n")
                continue

            for building, crew in day_assignments:
                crew_list = ", ".join(format_crew(crew))
                print(f"  Building {building.id} ({building.type:10}) -> {crew_list}")
                new_scheduled.add(building.id)
            print()  # Add space between days

        # Update scheduled buildings
        scheduled_building_ids.update(new_scheduled)

        # Calculate and print weekly summary
        total_buildings = len(all_buildings)
        scheduled_buildings = len(scheduled_building_ids)
        pending_buildings = total_buildings - scheduled_buildings

        print("\n" + "=" * 60)
        print(f" WEEK {week_number} SUMMARY ".center(60, "-"))
        print(f"Buildings scheduled this week: {len(new_scheduled)}")
        print(f"Total scheduled to date:      {scheduled_buildings}/{total_buildings}")
        print(f"Remaining buildings:          {pending_buildings}")

        if pending_buildings > 0:
            pending_ids = sorted(set(b.id for b in all_buildings) - scheduled_building_ids)
            print(f"\nPending Building IDs: {', '.join(map(str, pending_ids))}")

        print("=" * 60)

        week_number += 1


if __name__ == "__main__":
    main()

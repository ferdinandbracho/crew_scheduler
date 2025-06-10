# Aurora Solar Scheduler

A scheduling system for solar installation crews that optimizes the assignment of employees to building installations based on project requirements and employee availability. The system handles multi-week scheduling, respects employee availability, and maintains building priority order.

## Features

- **Building Types**:
  - Single story homes: 1 certified installer
  - Two story homes: 1 certified installer + 1 pending-certification installer or laborer
  - Commercial buildings: 2 certified installers + 2 pending-certification installers + 4 laborers
- **Employee Management**:
  - Tracks daily availability (Mon-Fri)
  - Handles different employee roles (certified, pending, laborers)
  - Prevents double-booking of employees
- **Scheduling**:
  - Multi-week scheduling until all buildings are assigned
  - Maintains building priority order
  - Daily and weekly schedule output
  - Progress tracking with scheduled vs pending buildings

## Project Structure

```text
solar_scheduler/
├── cli.py           # Command-line interface and demo data
├── models.py        # Pydantic models for Buildings and Employees
├── scheduler.py     # Core scheduling algorithm
└── rules.py        # Business rules for crew requirements
```

## Requirements

- Python 3.13+
- Pydantic (for data validation)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd aurora
   ```

2. Set up the development environment:

   ```bash
   make setup
   ```
   
   This will:
   - Install `uv` (if not already installed)
   - Install all Python dependencies
   - Set up the package in development mode

## Quick Start

Run the demo scheduler with:

```bash
make demo
# or alternatively
make run
```

For direct execution without Make:

```bash
uv run python -m solar_scheduler.cli
```

## Edge Cases Handled

1. **Employee Availability**:
   - Employees can be marked as unavailable on specific weekdays
   - Employees can only work on one building per day

2. **Building Priority**:
   - Buildings are scheduled in the order they are provided
   - Failed assignments don't block lower priority buildings

3. **Crew Requirements**:
   - Strict enforcement of crew requirements per building type
   - Certified installers can be used as laborers if needed

## Future Considerations

This section outlines potential areas for future development, including unaddressed edge cases, improvements, and further testing.

### Enhanced Edge Case Handling & Robustness

- Support for more complex employee availability (e.g., partial days).
- Consideration of granular employee skills beyond basic roles.
- Optimization for travel time and logistics.

### System & Feature Improvements

- Exploration of more advanced scheduling algorithms for optimization.
- Implementation of employee workload balancing features.
- Configuration options for work parameters (e.g., weekend work).
- Data persistence for schedules (save/load).

### Comprehensive Testing

- Expanded unit tests for core logic (`scheduler.py`, `rules.py`).
- More integration tests for the CLI with diverse scenarios.
- Property-based testing to cover a wider range of inputs.
- Performance testing with larger datasets.

## Example Output

```text
WEEK 1
-------
Monday:
  Building 1 (commercial) -> C1, C2, P4, P5, C3, L7, L8, L9
  Building 2 (single) -> C4
Tuesday:
  Building 3 (two) -> C1, P4
...
```

## Development

### Available Commands

The project includes a Makefile with helpful commands:

```bash
make setup    # Set up the development environment
make demo     # Run the demo (same as make run)
make run      # Run the scheduler
make help     # Show all available commands
```


## Technical Implementation

The scheduler follows these steps:

1. **Process Buildings in Order**:
   - Buildings are handled in the order they're provided (assumed to be by priority)

2. **Find Earliest Available Slot**:
   - For each building, finds the first day where:
     - Required crew members are available
     - Building type requirements are met

3. **Update Availability**:
   - Once scheduled, marks assigned employees as unavailable for that day

4. **Repeat Until Complete**:
   - Continues until all buildings are scheduled


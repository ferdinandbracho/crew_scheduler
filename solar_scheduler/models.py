from typing import List

from pydantic import BaseModel, Field


class Employee(BaseModel):
    """Represents an employee with their availability.

    Attributes:
        id: Unique identifier for the employee (positive integer)
        role: Role of the employee (certified, pending, or laborer)
        available_days: List of days the employee is available (list of strings)
        name: Optional name of the employee
    """

    id: int = Field(..., gt=0, description="Unique identifier for the employee")
    role: str = Field(..., description="Role of the employee (certified, pending, or laborer)")
    available_days: List[str] = Field(
        ..., description="List of days the employee is available"
    )
    name: str | None = Field(None, description="Optional name of the employee")



class Building(BaseModel):
    """Represents a building with its basic information.

    Attributes:
        id: Unique identifier for the building (positive integer)
        type: Category or classification of the building (non-empty string)
    """

    id: int = Field(..., gt=0, description="Unique identifier for the building")
    type: str = Field(
        ..., min_length=1, description="Category or classification of the building"
    )

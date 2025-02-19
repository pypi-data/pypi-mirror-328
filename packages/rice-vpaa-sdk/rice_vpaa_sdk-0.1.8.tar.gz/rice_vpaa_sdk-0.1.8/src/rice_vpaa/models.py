from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date

class Department(BaseModel):
    """A department or program within a division."""
    unit_id: int = Field(description="The ID of the department as used inside Interfolio.")
    unit_name: str = Field(description="The name of the department.")

class Division(BaseModel):
    """A school or division that may contain departments."""
    unit_id: int = Field(description="The ID of the unit used inside Interfolio.")
    unit_name: str = Field(description="The name of the unit.")
    departments: List[Department] = Field(default_factory=list, description="The departments that are part of this unit.")

class DivisionResponse(BaseModel):
    """Response containing all divisions and their departments."""
    divisions: List[Division] = Field(description="List of all divisions and their departments")

class FacultyProfile(BaseModel):
    """Faculty profile information."""
    email: str
    employment_status: str = Field(alias="employmentstatus")
    first_name: str = Field(alias="firstname")
    last_name: str = Field(alias="lastname")
    last_login: Optional[date] = Field(alias="lastlogin", default=None)
    middle_name: str = Field(alias="middlename", default="")
    pid: int
    position: Optional[str] = None
    primary_unit: Optional[int] = Field(alias="primaryunit", default=None)
    rank: Optional[str] = None
    user_id: str = Field(alias="userid")
    web_profile: bool

    class Config:
        populate_by_name = True  # Allows both alias and field name to be used
        alias_generator = None   # Don't auto-generate aliases

class FacultyResponse(BaseModel):
    """Response containing faculty profiles."""
    faculty: List[FacultyProfile]

class Position(BaseModel):
    """An open faculty position."""
    location: str
    unit_name: str
    name: str
    open_date: str
    deadline: str
    legacy_position_id: str

class PositionsResponse(BaseModel):
    """Response containing open positions."""
    results: List[Position]

class TeachingActivity(BaseModel):
    """Individual teaching activity record from Interfolio."""
    user_id: str = Field(alias="userid", description="Faculty member's Interfolio user ID")
    crn: str = Field(description="Course Registration Number")
    term: str = Field(description="Academic term, in Banner format")
    prefix: str = Field(description="Course code, e.g., ENGL")
    number: str = Field(description="Course number, e.g., 101")
    section: str = Field(description="Course section, e.g., 001")
    title: str = Field(description="Course title")
    credit_hours: Optional[float] = Field(description="Number of credit hours")
    enrollment: Optional[int] = Field(description="Number of enrolled students")
    course_quality: Optional[float] = Field(description="Course quality rating")
    instructor_effectiveness: Optional[float] = Field(description="Instructor effectiveness rating")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "userid": "12345",
                "crn": "12345",
                "term": "2023/01",
                "prefix": "ENGL",
                "number": "101",
                "section": "001",
                "title": "Introduction to Literature",
                "credit_hours": 3.0,
                "enrollment": 25,
                "course_quality": 1.5,
                "instructor_effectiveness": 1.2
            }]
        }
    }

class TeachingActivityResponse(BaseModel):
    """Response model containing a list of teaching activities."""
    activities: List[TeachingActivity] = Field(description="List of teaching activities")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "activities": [{
                    "userid": "12345",
                    "crn": "12345",
                    "term": "2023/01",
                    "prefix": "ENGL",
                    "number": "101",
                    "section": "001",
                    "title": "Introduction to Literature",
                    "credit_hours": 3.0,
                    "enrollment": 25,
                    "course_quality": 1.5,
                    "instructor_effectiveness": 1.2
                }]
            }]
        }
    }
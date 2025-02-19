from typing import List, Optional
import requests
from .models import (
    DivisionResponse, FacultyResponse, PositionsResponse, TeachingActivityResponse
)
from .config import BASE_URL

class VPAAClient:
    def __init__(self, api_key: str):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": api_key,
            "Accept": "application/json"
        })
    
    def get_divisions(self, departments_only: bool = False) -> DivisionResponse:
        response = self.session.get(
            f"{self.base_url}/interfolio/faculty-activity-reporting/divisions",
            params={"departments_only": departments_only}
        )
        if response.status_code == 403:
            raise ValueError(
                "Invalid or missing API key. "
                "Make sure VPAA_API_KEY environment variable is set and contains a valid key."
            )
        response.raise_for_status()
        return DivisionResponse.model_validate(response.json())
    
    def get_faculty(
        self,
        unit_ids: Optional[List[int]] = None,
        tenure_statuses: Optional[List[str]] = None,
        employment_statuses: Optional[List[str]] = None
    ) -> FacultyResponse:
        params = {}
        if unit_ids:
            params["unit_ids"] = unit_ids
        if tenure_statuses:
            params["tenure_statuses"] = tenure_statuses
        if employment_statuses:
            params["employment_statuses"] = employment_statuses
            
        response = self.session.get(
            f"{self.base_url}/interfolio/faculty-activity-reporting/faculty",
            params=params
        )
        response.raise_for_status()
        return FacultyResponse.model_validate(response.json())
    
    def get_open_positions(self) -> PositionsResponse:
        response = self.session.get(
            f"{self.base_url}/interfolio/faculty-search/open-positions"
        )
        response.raise_for_status()
        return PositionsResponse.model_validate(response.json())

    def get_teaching_activities(
        self,
        unit_ids: Optional[List[int]] = None,
        tenure_statuses: Optional[List[str]] = None,
        employment_statuses: Optional[List[str]] = None
    ) -> TeachingActivityResponse:
        """
        Get teaching activities for faculty members, optionally filtered by unit, tenure status, and employment status.
        
        Args:
            unit_ids: Optional list of unit IDs to filter faculty by department/division
            tenure_statuses: Optional list of tenure statuses to filter by ("TTT", "NTT", "PNTT", "Other")
            employment_statuses: Optional list of employment statuses to filter by ("Full Time", "Part Time")
            
        Returns:
            TeachingActivityResponse containing a list of teaching activities
        """
        params = {}
        if unit_ids:
            params["unit_ids"] = unit_ids
        if tenure_statuses:
            params["tenure_statuses"] = tenure_statuses
        if employment_statuses:
            params["employment_statuses"] = employment_statuses
            
        response = self.session.get(
            f"{self.base_url}/interfolio/faculty-activity-reporting/teaching-activities",
            params=params
        )
        response.raise_for_status()
        return TeachingActivityResponse.model_validate(response.json())
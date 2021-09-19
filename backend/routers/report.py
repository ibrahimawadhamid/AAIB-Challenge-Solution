from fastapi import APIRouter, HTTPException
from typing import List
from .. import crud, schemas

router = APIRouter(tags=["report"])


@router.get("/reports", response_model=List[schemas.report.Report])
def reports():
    """Returns all reports in the system"""
    reports = crud.report.get_reports()
    return reports


@router.get("/reports/{report_id}", response_model=schemas.report.Report)
def get_report_by_id(report_id: str):
    """Returns a single report filtered by id."""
    report = crud.report.get_report_by_id(report_id=report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Not found")
    return report


@router.put("/reports/{report_id}", response_model=schemas.report.Report)
def update_report_state(report_id: str, updated_report_state: schemas.report.UpdatedState):
    """Update a report state with the provided state."""
    report = crud.report.update_report_state(report_id=report_id, state=updated_report_state.ticketState)
    if report is None:
        raise HTTPException(status_code=404, detail="Not found")
    return report

from fastapi import APIRouter
from typing import List
from .. import crud, schemas

router = APIRouter(tags=["report"])


@router.get("/reports/", response_model=List[schemas.report.Report])
def reports():
    """Returns all reports in the system"""
    reports = crud.report.get_reports()
    return reports

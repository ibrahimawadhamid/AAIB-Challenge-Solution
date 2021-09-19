import os
import json
from typing import List
from ..schemas.report import Report as ReportSchema


# start loading initial data "simulate a database"
reports = []

with open(os.path.join("backend", "data.json")) as f:
    data = json.load(f)
    for element in data["elements"]:
        report = ReportSchema(
            id=element["id"], type=element["payload"]["reportType"], state=element["state"],
            message=element["payload"]["reportType"], created=element["created"]
        )
        reports.append(report)


def get_reports() -> List[ReportSchema]:
    """Get all reports from the simulated database."""
    return [report for report in reports if report.state != "BLOCKED"]


def get_report_by_id(report_id: str) -> ReportSchema:
    """Return a list of reports filtered by id."""
    reports_result = [report for report in reports if report.id == report_id]
    if len(reports_result) > 0:
        return reports_result[0]
    else:
        return None


def update_report_state(report_id: str, state: str) -> ReportSchema:
    """Update a report state then return it."""
    report = get_report_by_id(report_id)
    if report is None:
        return None
    report.state = state
    return report

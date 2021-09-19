import os, json
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


def get_reports():
    """Get all reports from the simulated database."""
    return reports

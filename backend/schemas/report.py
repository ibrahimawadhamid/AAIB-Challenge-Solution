import datetime
from pydantic import BaseModel


class Report(BaseModel):
    """The base schema class for a single report"""
    id: str
    type: str
    state: str
    message: str
    created: datetime.datetime


class ResolveReport(BaseModel):
    """A schema for resolving a report."""
    ticketState: str

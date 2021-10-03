import datetime
from enum import Enum
from pydantic import BaseModel, Field


class TicketState(str, Enum):
    open = 'OPEN'
    closed = 'CLOSED'
    blocked = 'BLOCKED'


class Report(BaseModel):
    """The base schema class for a single report"""
    id: str
    type: str
    state: TicketState = Field()
    message: str
    created: datetime.datetime


class UpdatedState(BaseModel):
    """A schema for updating a report state."""
    ticketState: TicketState = Field()

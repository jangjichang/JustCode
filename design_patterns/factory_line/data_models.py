from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Context(BaseModel):
    current_datetime: Optional[datetime]
    broker: Optional[str]
    user_id: Optional[int]
    account_id: Optional[str]
    action: Optional[str]


class Button(BaseModel):
    text: str
    url: Optional[str]
    type: str


class BottomSheet(BaseModel):
    title: str
    message: str
    highlight: list[str]
    image_url: str
    buttons: list[Button]



class Event(BaseModel):
    event_name: str
    participant: list[int]

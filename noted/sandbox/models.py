# Models for practicing DDD
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date, time

from typing import Optional, List
import uuid


class Task:
    def __init__(
        self,
        task_id: float,
        title: str,
        date_added: datetime,
        content: Optional[str] = "",
        is_complete: bool = False,
        is_current: bool = True,
    ):
        self.task_id = id
        self.title = title
        self.content = content
        self.is_complete = is_complete
        self.is_current = is_current
        self.date_added = date_added

    def mark_complete(self):
        self.is_complete = True

    def on_queue(self):
        self.is_current = False
        return self.is_current


# Can workday serve as a aggregate for task?
class Workday:
    def __init__(
        self,
        work_day_id: str,
        current_date: date,
        hours: List[time],
        tasks: List[Task] = None,
    ):
        self.work_day_id = work_day_id
        self.current_date = current_date
        self.hours = hours
        self.tasks = tasks
    
    

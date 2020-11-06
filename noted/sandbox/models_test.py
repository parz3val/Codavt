from models import Task
from datetime import datetime


def test_task_complete():
    task = Task(task_id=1.0, title="Test note", date_added=datetime.now, content="")
    assert str(task.mark_complete())

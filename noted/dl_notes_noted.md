# Notes for the Noted app

These are some notes to discover and write the domain model of the noted app.

Desc: Record standup tasks, working hours taken to complete the tasks

Notes:
Working days are from Monday to Friday, so the application only checks for events on working days.

Working day consists of total hours(9) here from 7 to 4. It can also be set custom by the user. start_time and end_time represent the times.

Working day is identified with working_day_id and the datetime object.

Task is a smallest unit of work that needs to completed and is fully recursible. Task is identified by unique task_id and contains at least one working day, title, and timestamp, and boolean status (is_complete).

Current references whether the task is being worked on or not.

Tasks can automatically start recording the period once the current of the task is set to True.

Time taken is the difference between the timestamp of is_complete and current start date.

If the task isn't complete in a day, they move to next working day automatically.

## Wrting a models

To do

Notes

import calendar
from abc import ABC, abstractmethod
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class Repeat(BaseModel, ABC):
    @abstractmethod
    def shouldBeShown(self, task_date: date) -> bool:
        pass
    
class NoRepeat(Repeat):
    def shouldBeShown(self, task_date: date) -> bool:
        return True

class Daily(Repeat):
    def shouldBeShown(self, task_date: date) -> bool:
        curr_date = date.today()
        return curr_date >= task_date

class Weekly(Repeat):
    def shouldBeShown(self, task_date: date) -> bool:
        curr_date = date.today()
        if curr_date >= task_date:
            return curr_date.weekday() == task_date.weekday()
        return False

class Monthly(Repeat):
    def shouldBeShown(self, task_date: date) -> bool:
        curr_date = date.today()
        if curr_date >= task_date:
            _, last_day = calendar.monthrange(curr_date.year, curr_date.month) 
            clamped_day = min(task_date.day, last_day)
            return curr_date.day == clamped_day
        return False

class Custom(Repeat):
    weekdays: list[int] = Field(...,
        min_length=1, 
        description="List of weekdays (0=Monday, 6=Sunday) for recurrence"
    )

    def shouldBeShown(self, task_date: date) -> bool:
        curr_date = date.today()
        if curr_date >= task_date:
            return curr_date.weekday() in self.weekdays
        return False
        

class Task(BaseModel):
    description: str
    repeat: Repeat = NoRepeat()
    task_date: date = date.today()

tasks: list[Task] = []

# @tool
def create_task(task: Task) -> bool:
    """ Allows to create a task """
    tasks.append(task) 
    return True


create_task(Task(description = "Hacer Ejercicio", repeat = Custom(weekdays = [1, 3, 5])))
create_task(Task(description = "Sacar pasaportes", task_date=date(2026, 1, 15)))
create_task(Task(description = "Ir por Alessa", repeat = Daily()))
create_task(Task(description = "Diego Play Therapy", repeat = Weekly()))
create_task(Task(description = "Pastilla del perro anti pulgas", repeat = Monthly()))


print(tasks)

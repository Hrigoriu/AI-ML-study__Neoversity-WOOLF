from abc import ABC, abstractmethod

from src.tasks import Task

id_counter = 0


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...


class AddTaskCommand(Command):
    def __init__(self, task_list: list[Task], task_description: str):
        super().__init__()
        self.task_list = task_list
        self.task_description = task_description

    def execute(self):
        global id_counter
        id_counter += 1
        new_task = Task(id_counter, self.task_description)
        self.task_list.append(new_task)


class AllTasksCommand(Command):
    def __init__(self, task_list: list[Task]):
        super().__init__()
        self.task_list = task_list

    def execute(self):
        print(self.task_list)

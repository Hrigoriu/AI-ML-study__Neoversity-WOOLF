import pickle
import os.path

from abc import ABC, abstractmethod
from src.tasks import Task


class TaskPersistenceStrategy(ABC):
    @abstractmethod
    def persist(self, task_list: list[Task]) -> None: ...

    @abstractmethod
    def load(self) -> list[Task]: ...


class PickleTaskPersistenceStrategy(TaskPersistenceStrategy):
    FILE_PATH = 'tasks.pkl'

    def persist(self, task_list: list[Task]) -> None:
        with open(self.FILE_PATH, 'wb') as file:
            pickle.dump(task_list, file)

    def load(self) -> list[Task]:
        if os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, 'rb') as file:
                return pickle.load(file)
        else:
            return []

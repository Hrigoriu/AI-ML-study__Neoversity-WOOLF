from src.logger import Logger
from src.commands import Command


class TaskInvoker:
    def __init__(self):
        self.logger = Logger()

    def run_command(self, command: Command):
        self.logger.info(f"Running command: {command.__class__.__name__}")
        command.execute()

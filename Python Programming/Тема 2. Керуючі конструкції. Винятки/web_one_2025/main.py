from src.logger import Logger
from src.invoker import TaskInvoker
from src.commands import AddTaskCommand, AllTasksCommand
from src.strategies import PickleTaskPersistenceStrategy

import colorama

colorama.init(autoreset=True)


def main():
    logger = Logger()
    task_invoker = TaskInvoker()
    persistence_strategy = PickleTaskPersistenceStrategy()

    task_list = persistence_strategy.load()

    available_actions = {
        "add": lambda: task_invoker.run_command(
            AddTaskCommand(task_list, input("Enter task description: "))
        ),
        "all": lambda: task_invoker.run_command(AllTasksCommand(task_list)),
        "exit": lambda: exit(0),
    }

    while True:
        user_input = input("Please select action: add|all|exit: ").strip().lower()

        logger.info(f"User has entered {colorama.Fore.BLUE}'{user_input}'")

        if user_input in available_actions:
            action = available_actions[user_input]
            persistence_strategy.persist(task_list)
            action()
        else:
            print(f"{colorama.Fore.RED}Unknown action")


if __name__ == "__main__":
    main()

from src.models import FileSource, ConsoleSource, APISource, TasksGiver


def give_engine():
    sources = [FileSource(), ConsoleSource(), APISource()]
    for source in sources:
        tasks = source
        if isinstance(source, TasksGiver):
            for task in tasks.get_tasks():
                print(tasks.printf_task(task))

if __name__ == "__main__":
    give_engine()

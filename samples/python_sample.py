from dataclasses import dataclass


@dataclass
class Task:
    title: str
    completed: bool = False


def summarize(tasks: list[Task]) -> str:
    """Return a short summary of completed and pending tasks."""
    completed = sum(task.completed for task in tasks)
    return f"{completed}/{len(tasks)} tasks completed"


tasks = [Task("Review theme", True), Task("Check syntax colors")]
print(summarize(tasks))
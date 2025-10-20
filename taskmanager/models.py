import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Literal

TASK_STATUS = Literal["BACKLOG", "TODO", "IN_PROGRESS", "BLOCKED", "DONE"]
TASK_COMPLEXITY = Literal[1, 2, 3, 4, 5]


@dataclass
class Task:
    """
    Represents a single task in our system.
    We use 'field' to provide default values or custom factories.
    'default_factory' runs a function to get the default.
    """

    id: str = field(default_factory=lambda: f"task_{uuid.uuid4()}")
    description: str
    status: TASK_STATUS = "BACKLOG"
    due_date: Optional[datetime] = None
    complexity: int = 1
    dependencies: List[str] = field(default_factory=list)
    time_taken_minutes: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now(tz="utc"))

    def __post_init__(self):
        """
        This is a special dataclass method that runs right after
        the object is created. We can use it for validation.
        """
        if self.complexity < 1:
            self.complexity = 1
        if self.complexity > 5:
            self.complexity = 5

        # A task in the backlog shouldn't have a due date by default,
        # but a task moved to TODO should have one.
        if self.status != "BACKLOG" and self.due_date is None:
            # This is a good place to raise an error to let the developer
            # (us) know we're using the class wrong.
            raise ValueError("Tasks in 'TODO' must have a due_date.")

    def move_to_done(self, time_taken: int):
        """
        A helper method to properly mark a task as done.
        """
        self.status = "DONE"
        self.time_taken_minutes = time_taken
        print(f"Task '{self.id}' moved to DONE. Time taken: {time_taken} minutes.")

    def add_dependency(self, task_id: str):
        """
        A helper method to add a dependency.
        """
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
            print(f"Task '{task_id}' is now a dependency for '{self.id}'.")


# --- Example Usage (You can run this file directly to test it) ---
if __name__ == "__main__":

    # 1. Create a few tasks
    task1 = Task(description="Set up project structure", status="DONE", complexity=2)
    task1.move_to_done(time_taken=60)

    task2 = Task(
        description="Write core prioritization logic",
        status="TODO",
        due_date=datetime.now(),
        complexity=5,
    )

    # 2. Create a sub-task that depends on task2
    task3 = Task(
        description="Write tests for prioritization",
        status="TODO",
        due_date=datetime.now(),
        complexity=3,
        dependencies=[task2.id],  # This task depends on task2
    )

    print("--- Created Tasks ---")
    print(task1)
    print("\n")
    print(task2)
    print("\n")
    print(task3)

    print(f"\nTask 3 depends on: {task3.dependencies}")

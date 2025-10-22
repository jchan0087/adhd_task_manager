import uuid
import copy
from dataclasses import dataclass, field, InitVar
from datetime import datetime, timezone
from typing import List, Optional, Literal, get_args

TASK_STATUS = Literal["BACKLOG", "TODO", "IN_PROGRESS", "BLOCKED", "DONE"]
TASK_COMPLEXITY = Literal[1, 2, 3, 4, 5]


@dataclass
class Task:
    """
    Represents a single task in our system.
    We use 'field' to provide default values or custom factories.
    'default_factory' runs a function to get the default.
    """

    description: str
    id: str = field(default_factory=lambda: f"task_{uuid.uuid4()}")
    due_date: Optional[datetime] = None
    complexity: int = 1
    dependencies: List[str] = field(default_factory=list)
    time_taken_minutes: Optional[int] = None
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    _status: str = field(init=False)
    initial_status: InitVar[str] = "BACKLOG"

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str):
        if (
            new_status != self.initial_status and
            new_status not in get_args(TASK_STATUS)
        ):
            print("status is not initial status")
            self.status = self.initial_status
        else:
            self._status = new_status

    def __post_init__(self, initial_status):
        """
        This is a special dataclass method that runs right after
        the object is created. We can use it for validation.
        """
        if self.complexity < 1:
            self.complexity = 1
        if self.complexity > 5:
            self.complexity = 5

        self.status = initial_status

        # A task in the backlog shouldn't have a due date by default,
        # but a task moved to TODO should have one.
        if self.status != "BACKLOG" and self.due_date is None:
            # This is a good place to raise an error to let the developer
            # (us) know we're using the class wrong.
            raise ValueError(
                f"""Task '{self.id}' has status '{self.status}' but no due_date."""
            )

        self._initial_state = copy.deepcopy(self.__dict__)

    def move_to_done(self, time_taken: int):
        """
        A helper method to properly mark a task as done.
        """
        self.status = "DONE"
        self.time_taken_minutes = time_taken
        print(
            f"""Task '{self.id}' moved to DONE.
            Time taken: {time_taken} minutes."""
        )

    def add_dependency(self, task_id: str):
        """
        A helper method to add a dependency.
        """
        if task_id not in self.dependencies:
            self.dependencies.append(task_id)
            print(f"Task '{task_id}' is now a dependency for '{self.id}'.")


# --- Example Usage (You can run this file directly to test it) ---
if __name__ == "__main__":

    print("--- Creating Tasks ---")

    # 1. Create a few tasks
    # We must provide 'initial_status' and a 'due_date'
    # because the status is not 'BACKLOG'.
    try:
        task1 = Task(
            description="Set up project structure",
            initial_status="DONE",  # <-- Use 'initial_status'
            complexity=2,
            due_date=datetime.now(timezone.utc) # <-- Must provide due_date
        )
        task1.move_to_done(time_taken=60)
        print(task1)

    except ValueError as e:
        print(f"Error creating task1: {e}")

    try:
        task2 = Task(
            description="Write core prioritization logic",
            initial_status="TODO",  # <-- Use 'initial_status'
            due_date=datetime.now(timezone.utc), # <-- Must provide due_date
            complexity=5,
        )
        print("\n")
        print(task2)

    except ValueError as e:
        print(f"Error creating task2: {e}")

    # 2. Create a sub-task that depends on task2
    try:
        task3 = Task(
            description="Write tests for prioritization",
            initial_status="TODO",  # <-- Use 'initial_status'
            due_date=datetime.now(timezone.utc), # <-- Must provide due_date
            complexity=3,
            dependencies=[task2.id],  # This task depends on task2
        )
        print("\n")
        print(task3)
        print(f"\nTask 3 depends on: {task3.dependencies}")

    except (ValueError, NameError) as e:
        print(f"\nError creating task3: {e}")

    # 3. Create a simple backlog task (no due date needed)
    try:
        task4 = Task(
            description="Think about future features",
            initial_status="BACKLOG" # <-- This is fine with no due_date
        )
        print("\n")
        print(task4)

    except ValueError as e:
        print(f"\nError creating task4: {e}")

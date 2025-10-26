# ADHD Task Manager (Working Title)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This is a free, open-source tool to help those with ADHD tackle their daily tasks, both at work and in their personal lives. The project was inspired by my 12-year-old son who, like me, has ADHD. We both find that traditional calendar and task apps are a constant struggle to manage.

My hope is to build a tool that helps him—and others like us—struggle less with planning and focus more on living.

---

## Core Philosophy

Traditional task managers often require you to estimate how long a task will take, which is a common challenge for those with ADHD. This project flips the script:

* **Prioritization First:** Tasks are weighted by urgency, complexity, due date, and dependencies.
* **Clear "Next Step":** The primary goal is for the tool to tell you the *single next task* to focus on.
* **Track, Don't Predict:** You log the time a task took *after* you complete it, providing useful data without the upfront anxiety of estimation.

## Key Features

* **Smart Prioritization Engine:** Automatically sorts your `TODO` list based on a weighted algorithm.
* **Task Statuses:** A workflow inspired by Kanban: `BACKLOG`, `TODO`, `IN_PROGRESS`, `BLOCKED`, and `DONE`.
* **Dependency Management:** A task won't appear as "next" if its prerequisite tasks aren't `DONE`.
* **Persistent Storage:** Your tasks are saved locally to a file, so you never lose your list.
* **Dual Interfaces:** Access your tasks how *you* work best:
    * **CLI:** A fast, keyboard-driven interface for your terminal.
    * **Web UI:** A visual, drag-and-drop Kanban-style board (planned).
    * **Mobile App:** A future goal is to create a native app.

## Project Architecture

This project is built with a clean, decoupled architecture, making it modular and easy to maintain.

1.  **🧠 The Core Library (`taskmanager`)**
    * A pure Python library containing all the "brains."
    * Includes the `Task` model, the `TaskManager` class for managing the list, and the `Prioritizer` logic.
    * This engine is totally independent of any user interface.

2.  **💻 The CLI (Command-Line Interface)**
    * The first "head" for the core library.
    * Uses `typer` (or `argparse`) to provide simple commands like `task next`, `task add`, and `task done`.
    * Imports and calls the Core Library.

3.  **🖥️ The Web Application (API + UI)**
    * The second "head" for the core library.
    * **Backend API:** A lightweight Flask/FastAPI server that wraps the Core Library in web endpoints (e.g., `GET /api/tasks/next`).
    * **Frontend UI:** A simple HTML/CSS/JavaScript single-page application that talks to the API to display a visual Kanban board.

## 🗺️ Project Roadmap

This project is under active development. Here is the high-level plan:

### ✅ Phase 1: The Core Library (The "Brain")
- [x] **Task Model (`models.py`):** Define the `Task` data structure with statuses, dependencies, etc.
- [ ] **Task Manager (`manager.py`):** Create the `TaskManager` class to add, find, update, and hold tasks.
- [ ] **Storage (`storage.py`):** Implement saving/loading all tasks to a persistent JSON file.
- [ ] **Prioritizer (`prioritizer.py`):** Build the core logic to sort tasks by urgency, due date, complexity, and dependencies.

### Phase 2: The Command-Line Interface (CLI)
- [ ] **Command Parser:** Set up `typer` or `argparse` to handle user input.
- [ ] **Core Commands:** Implement essential commands:
    - [ ] `task next`
    - [ ] `task list`
    - [ ] `task add`
    - [ ] `task start <id>`
    - [ ] `task done <id> --time <minutes>`
    - [ ] `task move <id> <status>`
    - [ ] `task show backlog`

### Phase 3: The Web Application (API + UI)
- [ ] **Web API (Backend):**
    - [ ] Set up Flask/FastAPI server.
    - [ ] Create API endpoints for all core `TaskManager` functions.
- [ ] **Web UI (Frontend):**
    - [ ] Design basic HTML/CSS for a Kanban view.
    - [ ] Write JavaScript to `fetch` data from the API and build the UI.
    - [ ] Implement drag-and-drop functionality to change task status.

### Phase 4: Packaging & Distribution
- [ ] **`pyproject.toml`:** Create the project configuration and dependency file.
- [ ] **CLI Entry Point:** Configure the file to make the `task` command available on `pip install`.
- [ ] **Documentation:** Write final setup and usage instructions.
- [ ] **Publish:** (Optional) Publish the package to PyPI.

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. This means it will always remain free and open-source. You are welcome to use, modify, and distribute it, but any derivative works must also be shared under the same license.

## Contributing

(Placeholder) We welcome contributions! Please see `CONTRIBUTING.md` for details on how to get started, submit pull requests, and report bugs.
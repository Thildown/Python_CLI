# Advanced CLI Task Manager

A command-line task management tool with advanced features including subcommands, logging, environment variables, and unit testing.

## Features

- **Task Management**: Add, list, and delete tasks
- **Persistent Storage**: Tasks stored in a JSON file
- **Subcommands**: Intuitive interface using CLI subcommands
- **Logging**: Comprehensive logging of all operations
- **Environment Variables**: Configurable via environment variables
- **Testing**: Thorough unit test coverage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/advanced_cli_task_manager.git
cd advanced_cli_task_manager

## Interactive Testing with Jupyter Notebook

A Jupyter notebook (`task_manager_test.ipynb`) is included in the repository that contains pre-executed tests and demonstrations of the Task Manager CLI.

### Pre-executed Tests

The notebook includes several test runs that have been performed to demonstrate the functionality:

- Addition of multiple tasks with different priorities
- Listing and sorting tasks in various ways
- Test deletion of tasks
- Edge case handling (e.g., deleting non-existent tasks)
- Complete unit test execution results

You can review these test results to verify that the application functions as expected without needing to run the code yourself.

### Running Additional Tests

You can also execute the notebook cells to run your own tests:

1. Start Jupyter:
```bash
jupyter notebook
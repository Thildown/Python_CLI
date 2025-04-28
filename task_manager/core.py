import json
import os
import uuid
from datetime import datetime

# Import the logger
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file_path

# Setup logger
logger = setup_logger()

# Get tasks file path
TASKS_FILE = get_tasks_file_path()

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASKS_FILE):
        logger.info(f"Tasks file not found. Creating a new one at {TASKS_FILE}")
        return []
    
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            logger.info(f"Loaded {len(tasks)} tasks from {TASKS_FILE}")
            return tasks
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {TASKS_FILE}")
        return []
    except Exception as e:
        logger.error(f"Error loading tasks: {str(e)}")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
            logger.info(f"Saved {len(tasks)} tasks to {TASKS_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving tasks: {str(e)}")
        return False

def add_task(description, priority="medium"):
    """Add a new task with the given description and priority."""
    if not description:
        logger.error("Task description cannot be empty")
        return False
    
    if priority not in ["low", "medium", "high"]:
        logger.warning(f"Invalid priority '{priority}'. Using 'medium' instead.")
        priority = "medium"
    
    tasks = load_tasks()
    
    # Create new task
    new_task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    
    tasks.append(new_task)
    success = save_tasks(tasks)
    
    if success:
        logger.info(f"Added task: {description} with priority {priority}")
        return new_task
    else:
        logger.error(f"Failed to add task: {description}")
        return False

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    logger.info(f"Listed {len(tasks)} tasks")
    return tasks

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    initial_count = len(tasks)
    
    # Filter out the task to delete
    updated_tasks = [task for task in tasks if task.get("id") != task_id]
    
    if len(updated_tasks) == initial_count:
        logger.warning(f"Task with ID {task_id} not found")
        return False
    
    success = save_tasks(updated_tasks)
    
    if success:
        logger.info(f"Deleted task with ID: {task_id}")
        return True
    else:
        logger.error(f"Failed to delete task with ID: {task_id}")
        return False
import argparse
import json
import sys

# Import core functionality
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

# Setup logger
logger = setup_logger()

def main():
    """CLI entry point for the task manager."""
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add Task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("-d", "--description", required=True, help="Task description")
    add_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], 
                           default="medium", help="Task priority")
    
    # List Tasks command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--sort", choices=["priority", "created"], 
                            help="Sort tasks by priority or creation date")
    
    # Delete Task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("-i", "--id", required=True, help="Task ID to delete")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute command
    if args.command == "add":
        task = add_task(args.description, args.priority)
        if task:
            print(f"Task added successfully with ID: {task['id']}")
        else:
            print("Failed to add task")
            sys.exit(1)
    
    elif args.command == "list":
        tasks = list_tasks()
        if tasks:
            # Sort tasks if requested
            if args.sort == "priority":
                priority_order = {"high": 0, "medium": 1, "low": 2}
                tasks.sort(key=lambda x: priority_order.get(x.get("priority", "medium"), 1))
            elif args.sort == "created":
                tasks.sort(key=lambda x: x.get("created_at", ""))
            
            # Print tasks
            print("Tasks:")
            for task in tasks:
                print(f"ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Priority: {task['priority']}")
                print(f"Created: {task['created_at']}")
                print(f"Completed: {task['completed']}")
                print("---")
        else:
            print("No tasks found")
    
    elif args.command == "delete":
        success = delete_task(args.id)
        if success:
            print(f"Task with ID {args.id} deleted successfully")
        else:
            print(f"Failed to delete task with ID {args.id}")
            sys.exit(1)
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
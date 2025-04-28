import os

def get_tasks_file_path():
    """Get task file path from environment variable or use default."""
    return os.getenv("TASKS_FILE_PATH", "tasks.json")
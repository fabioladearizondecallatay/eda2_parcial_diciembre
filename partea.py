import heapq
import json

"""El código implementa un sistema de gestión de tareas con prioridades utilizando un heap 
para manejar tareas de forma eficiente. Permite añadir tareas con prioridad y dependencias, 
listar tareas pendientes, marcar tareas como completadas y obtener la tarea más prioritaria disponible. 
Las dependencias se verifican automáticamente, y las tareas se guardan en un archivo para garantizar 
persistencia entre ejecuciones. Incluye validación de entradas y utiliza la librería heapq para garantizar 
una buena eficiencia en las operaciones"""


class TaskManager:
    def __init__(self, storage_file="tasks.json"):
        self.task_heap = []  # Priority queue
        self.completed_tasks = set()  # Set of completed task names
        self.storage_file = storage_file
        self.load_tasks()

    def add_task(self, name, priority, dependencies=None):
        if not name or not isinstance(priority, int):
            raise ValueError("Task name must be non-empty, and priority must be an integer.")
        if dependencies and not isinstance(dependencies, list):
            raise ValueError("Dependencies must be a list of task names.")
        dependencies = dependencies or []
        task = {
            "name": name,
            "priority": priority,
            "dependencies": dependencies
        }
        heapq.heappush(self.task_heap, (priority, name, task))
        self.save_tasks()

    def show_tasks(self):
        print("Pending tasks (ordered by priority):")
        for priority, name, task in sorted(self.task_heap):
            print(f"- {task['name']} (Priority: {task['priority']}, Dependencies: {task['dependencies']})")

    def complete_task(self, task_name):
        self.task_heap = [(p, n, t) for p, n, t in self.task_heap if t["name"] != task_name]
        heapq.heapify(self.task_heap)
        self.completed_tasks.add(task_name)
        self.save_tasks()

    def get_next_task(self):
        while self.task_heap:
            priority, name, task = self.task_heap[0]
            if self._can_execute(task):
                print(f"Next task: {task['name']} (Priority: {task['priority']})")
                return task
            else:
                print(f"Skipping task '{task['name']}' due to unmet dependencies.")
                heapq.heappop(self.task_heap)
        print("No executable tasks available.")
        return None

#bonus
    def _can_execute(self, task):
        return all(dep in self.completed_tasks for dep in task["dependencies"])

    def save_tasks(self):
        data = {
            "tasks": self.task_heap,
            "completed": list(self.completed_tasks)
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.task_heap = [(p, n, t) for p, n, t in data["tasks"]]
                self.completed_tasks = set(data["completed"])
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_heap = []
            self.completed_tasks = set()

# Example Usage
def main():
    tm = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Get Next Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Task name: ")
            priority = int(input("Priority (integer): "))
            dependencies = input("Dependencies (comma-separated, leave blank if none): ")
            dependencies = dependencies.split(",") if dependencies else []
            tm.add_task(name, priority, dependencies)
        elif choice == "2":
            tm.show_tasks()
        elif choice == "3":
            task_name = input("Task name to complete: ")
            tm.complete_task(task_name)
        elif choice == "4":
            tm.get_next_task()
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

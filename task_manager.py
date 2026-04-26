import json


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "❌"
        return f"{status} {self.title}"

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["completed"])


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Removed: {removed.title}")
        else:
            print("Invalid index")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid index")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []




def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                manager.mark_completed(index)
            except:
                print("Invalid input")

        elif choice == "4":
            manager.list_tasks()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                manager.remove_task(index)
            except:
                print("Invalid input")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()
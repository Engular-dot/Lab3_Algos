from typing import List
from dataclasses import dataclass

@dataclass
class Task:
    id_number: int
    description: str
    priority: str

    def __str__(self):
        return f"\n{self.id_number}: {self.description}, приоритет: {self.priority}"

class Queue:

    def __init__(self):

        self.tasks:List[Task] = []

    def enqueue(self,description,priority):
        
        id_number = len(self.tasks)+1
        new_task = Task(id_number, description, priority)
        self.tasks.append(new_task)
        print(f"Задача {id_number} добавлена в очередь")

    def dequeue(self):

        if self.isEmpty():
            print("Список пуст")
            return None
        return self.tasks.pop(0)
        

    def front(self):

        if self.isEmpty():
            print("Список пуст")
            return None
        return self.tasks[0]

    def isEmpty(self):

        return len(self.tasks) == 0

    def display_tasks(self):

        if not self.tasks:
            print("Список пуст")
            return None
        print("\nСПИСОК ЗАДАЧ")
        print("\n|  №  |               Описание задачи               |   Приоритет   |")
        for task in self.tasks:
            print(f"|{task.id_number:^5}|{task.description:^45}|{task.priority:^15}|")
def main():
    queue = Queue()

    queue.enqueue("Доделать проект","Высокий")
    queue.enqueue("Придумать название для приложения","Низкий")
    queue.enqueue("Подумать о вечном","Очень низкий")

    queue.display_tasks()
    print("\nПервая в очереди:")
    print(queue.front())
    print("\nСделана первой(вышла первой):")
    print(queue.dequeue())
    queue.display_tasks()

if __name__ == '__main__':
    main()



class ToDoList(object):
    """Класс для внесения и сопровождения задач"""

    def __init__(self):
        self.task_list = {}

    def add_task(self, task: str):
        """Добавить задачу в лист исполнения"""
        if task not in self.task_list.keys():
            self.task_list[task] = '\u267B'
            print(f'Задача "{task}" внесена в лист исполнения\n')
        else:
            print(f'Задача "{task}" уже существует\n')

    def complete_task(self, task: str):
        """Отметить задачу как выполненную"""
        if task in self.task_list.keys():
            self.task_list[task] = '\u2705 '
            print(f'Задача "{task}" отмечена как выполненная\n')
        else:
            print(f'Задача "{task}" не существует\n')

    def remove_task(self, task: str):
        """Удалить задачу из листа исполнения"""
        if task in self.task_list.keys():
            del (self.task_list[task])
            print(f'Задача "{task}" удалена из списка\n')
        else:
            print(f'Задача "{task}" не существует\n')

    def get_list_tasks(self):
        """Вывести список всех задач"""
        print('Список всех задач:\n')
        for task, status in self.task_list.items():
            print(f'{status}\t"{task}"\n')


task_list = ToDoList()

task_list.add_task('Task1')
task_list.add_task('Task2')
task_list.add_task('Task3')
task_list.add_task('Task1')
input()

task_list.get_list_tasks()
input()

task_list.complete_task('Task1')
task_list.complete_task('Task2')
input()

task_list.remove_task('Task2')
task_list.remove_task('Task2')
input()

task_list.get_list_tasks()

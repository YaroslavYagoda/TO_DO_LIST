import query_action as q
from shell_def import ShellDef
import json


class TaskManager(ShellDef):
    """Класс управления задачами"""

    def __init__(self):
        self.__tasks_list = []
        self.func_list = [self.get_tasks_list,
                          self.add_task,
                          self.complete_task,
                          self.remove_task,
                          self.load_from_json,
                          self.save_to_json,
                          self.exit_program]
        self.hello_string = q.terminal_hello_string
        self.query = q.start_terminal_query
        self.action = q.start_terminal_action

    json_file_name = 'task.json'

    @staticmethod
    def input_task_name(description=None):
        """Ввод наименования задачи"""
        if not description:
            description = ''
            while not (''.join(description.split()).isalnum()):
                description = input('Введите название задачи:\n')
        return description

    @staticmethod
    def input_task_index(index=None):
        """Ввод индекса задачи"""
        if not index:
            index = ''
            while not index.isdigit():
                index = input('Введите номер задачи из списка:\n')
        return int(index)

    def get_tasks_list(self):
        """Вывести список всех задач"""
        self.clear_screen()
        print('Список всех задач:\n')
        for i in range(len(self.__tasks_list)):
            print(f'{self.__tasks_list[i]["icon"]} '  # Иконка статуса выполнения
                  f'{i + 1}. '  # Номер по порядку (для удаления по индексу)
                  f'{self.__tasks_list[i]["description"]}:\n'  # Задача
                  f'\tСтатус выполнения - {"выполнена" if self.__tasks_list[i]["completed"] else "выполняется"}\n')
        print(f'Всего задач в списке: {len(self.__tasks_list)}\n')
        self.input_continue()

    def add_task(self, description=None):
        """Добавить задачу в лист исполнения"""
        self.clear_screen()
        print('Добавление новой задачи\n')
        description = self.input_task_name(description)
        self.__tasks_list.append({"description": description,
                                  "completed": False,
                                  "icon": '\u267B'})
        print('\nЗадача  внесена в лист исполнения\n')
        self.input_continue()

    def complete_task(self, index=None):
        """Отметить задачу как выполненную"""
        self.clear_screen()
        print('Снятие задачи с контроля(отметка о выполнении)\n')
        index = self.input_task_index(index)
        if 0 < index <= len(self.__tasks_list):
            self.__tasks_list[index - 1] = {"description": self.__tasks_list[index - 1]["description"],
                                            "completed": True,
                                            "icon": '\u2705'}
            print('\nЗадача отмечена как выполненная\n')
            self.input_continue()
        else:
            print(f'\nЗадачи с номером "{index}" не существует\n')
            self.input_continue()

    def remove_task(self, index=None):
        """Удалить задачу из листа исполнения"""
        self.clear_screen()
        print('Удаление задачи из списка\n')
        index = self.input_task_index(index)
        if 0 < index < len(self.__tasks_list) + 1:
            self.__tasks_list.pop(index - 1)
            print('\nЗадача удалена\n')
            self.input_continue()
        else:
            print(f'\nЗадачи с индексом "{index}" не существует\n')
            self.input_continue()

    def load_from_json(self):
        self.clear_screen()
        print('Импорт задач из файла (добавление в текущий список)\n')
        with open(self.json_file_name, 'r') as json_file:
            data = json.load(json_file)
        for task in data:
            self.__tasks_list.append(task)
        print(f'Импортировано задач: {len(data)}\n')
        self.input_continue()

    def save_to_json(self):
        self.clear_screen()
        print('Экспорт задач (файл будет перезаписан)\n')
        with open(self.json_file_name, 'w') as json_file:
            json.dump(self.__tasks_list, json_file, indent=4)
        print(f'Экспортировано задач: {len(self.__tasks_list)}\n')
        self.input_continue()

    def get_private_attr(self):
        return self.__tasks_list

    @staticmethod
    def input_continue():
        input('Для продолжения работы нажмите ввод (enter)')


if __name__ == '__main__':
    ext = ''
    tasks_list = TaskManager()
    try:
        while ext != 'exit':
            ext = tasks_list.choice_management()
    except Exception as err:
        print(f'Возникла ошибка "{err}"\n\nСвяжитесь с администратором!\n')
        tasks_list.input_continue()

import json
import os
from task_manager import TaskManager
from contextlib import redirect_stdout
import io


class TestProgram(TaskManager):
    test_task_name = 'Test_Task'
    test_task = {
        "description": test_task_name,
        "completed": False,
        "icon": '\u267B'
    }
    json_file_name = 'test_task.json'
    performed = False

    def isfile(self):
        assert os.path.exists(super().json_file_name), f'Файл {super().json_file_name} для импорта/экспорта не найден'

    def is_json_data_in_file(self):
        try:
            with open(super().json_file_name, 'r') as json_file:
                json.load(json_file)
        except json.JSONDecodeError as err:
            raise err

    def check_add_and_complete_task(self):
        len_old = len(self.get_private_attr())
        self.add_task(self.test_task_name)
        assert len_old + 1 == len(self.get_private_attr()), \
            'При добавлении задачи в список количество задач в списке не изменилось!'
        assert self.test_task in self.get_private_attr(), \
            'Количество задач в списке увеличилось но задача не добавлена!'
        self.complete_task(1)
        assert self.get_private_attr()[0]["completed"] == True and self.get_private_attr()[0]["icon"] == '\u2705', \
            'Задача не присвоен статус "выполнена" или не заменена иконка статуса на \u2705'

    def check_remove_task(self):
        len_old = len(self.get_private_attr())
        self.remove_task(1)
        assert len_old - 1 == len(self.get_private_attr()), \
            'При удалении задачи из списка количество задач в списке не изменилось!'
        assert self.test_task not in self.get_private_attr(), \
            'Количество задач в списке уменьшилось но задача осталась!'

    def check_save_and_load_from_json(self):
        self.add_task(self.test_task_name)
        list_old = self.get_private_attr().copy()
        self.save_to_json()
        self.remove_task(1)
        self.load_from_json()
        assert list_old == self.get_private_attr(), \
            'Ошибка последовательности экспорт --> импорт, сведения о задаче изменены'

    def conduct_tests(self):
        f = io.StringIO()
        with redirect_stdout(f):
            self.isfile()
            self.is_json_data_in_file()
            self.check_add_and_complete_task()
            self.check_remove_task()
            self.check_save_and_load_from_json()

    @staticmethod
    def input_continue(performed=False):
        if performed:
            input('Для продолжения работы нажмите ввод (enter)')


if __name__ == '__main__':
    test = TestProgram()
    test.conduct_tests()

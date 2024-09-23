from task_manager import TaskManager
from test_task_manager import TestProgram

if __name__ == '__main__':
    test = TestProgram()
    test.conduct_tests()
    ext = ''
    tasks_list = TaskManager()
    try:
        while ext != 'exit':
            ext = tasks_list.choice_management()
    except Exception as err:
        print(f'Возникла ошибка "{err}"\n\nСвяжитесь с администратором!\n')
        tasks_list.input_continue()

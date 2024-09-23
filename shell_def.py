from os import system


class ShellDef:
    def __init__(self):
        self.func_list = [self.exit_program]
        self.hello_string = 'Класс оболочки для выбора'
        self.query = 'Выберите действие:\n'
        self.action = ['1. Завершение работы']

    @staticmethod
    def clear_screen():
        system('cls||clear')

    @staticmethod
    def choice_of_answer(query, list_of_action):
        choice = ''
        list_of_answer = [str(i + 1) for i in range(len(list_of_action))]
        while choice not in list_of_answer:
            print(query)
            for action in list_of_action:
                print(action)
            choice = input()
        return choice

    @staticmethod
    def exit_program():
        print('\nРабота завершена!\nДо свидания!')
        return 'exit'

    @staticmethod
    def input_continue():
        input('Для продолжения работы нажмите ввод (enter)')

    def choice_management(self):
        self.clear_screen()
        print(self.hello_string + '\n')
        choice = int(self.choice_of_answer(self.query, self.action))
        call_func = self.func_list[choice - 1]
        return call_func()


if __name__ == '__main__':
    shelldef_cls = ShellDef()
    shelldef_cls.choice_management()

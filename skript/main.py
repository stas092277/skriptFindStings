import re

upiRe = '(.*) = UserPortIn'
upoRe = '(.*) = UserPortOut'


class ParamsManager:
    def __init__(self, path="default_simple_python_block.py"):
        self.path = path
        self.dependencies = {}
        self.all_inputs = set()
        self.using_params = set()

    def find_dependencies(self):
        with open(self.path, 'r') as file:
            text = file.read()

        text = text.replace('\n', '')
        classes = text.split('class')
        classes.pop(0)

        for tmp in classes:
            ins = re.findall(r'(\w+) = UserPortIn', tmp)
            out = re.findall(r'(\w+) = UserPortOut', tmp)
            self.dependencies[out[0]] = ins
            for tmp in ins:
                self.all_inputs.add(tmp)

    def add_new_using_param(self, name_input_param):
        if name_input_param in self.all_inputs:
            self.using_params.add(name_input_param)
            print(f'Параметр "{name_input_param}" добавлен в используемые.')
        else:
            raise ValueError("Нет такого параметра")

    def get_missing_input_params_for_out(self, name_out_param: str):
        return [param for param in self.dependencies[name_out_param] if param not in self.using_params]

    def get_all_output_params_for_input(self, name_input_param: str):
        ans = []
        for key in self.dependencies.keys():
            if name_input_param in self.dependencies[key]:
                ans.append(key)
        return ans

    def get_info_about_inputs_params(self):
        outputs_for_all_using = set()
        for name_int_param in self.using_params:
            out_puts = self.get_all_output_params_for_input(name_int_param)
            for out_put in out_puts:
                outputs_for_all_using.add(out_put)

        for out_put in outputs_for_all_using:
            needed_input = self.get_missing_input_params_for_out(out_put)
            if len(needed_input) == 0:
                print(f'-{out_put}.')
            else:
                print(f'-{out_put}. Не хватает: {needed_input}')

    def get_info_about_output_param(self, name_out_param: str):
        if name_out_param in self.dependencies:
            print(f'-{name_out_param}. Для рассчета нужны: {self.dependencies[name_out_param]}')
        else:
            raise ValueError("Нет такого параметра")


def writing_file(nameFile, lines):
    with open(nameFile, "w") as file:
        for line in lines:
            file.write(line + '\n')


def find_names():
    with open('default_simple_python_block.py', 'r') as file:
        lines = file.readlines()

    upi_set = set()
    upo_set = set()
    both_set = set()
    for line in lines:
        if line[0] == '#':
            continue
        if re.match(upiRe, line) is not None:
            upi_set.add(str(re.findall(r'(\w+) = UserPortIn', line)[0]))
        if re.match(upoRe, line) is not None:
            upo_set.add(str(re.findall(r'(\w+) = UserPortOut', line)[0]))

    both_set.update(upi_set, upo_set)

    upi_set = sorted(upi_set)
    upo_set = sorted(upo_set)
    both_set = sorted(both_set)

    writing_file("UserPortIn.txt", upi_set)
    writing_file("UserPortOut.txt", upo_set)
    writing_file("UserPortInAndOut.txt", both_set)


if __name__ == '__main__':
    # find_names()
    manager = ParamsManager()
    manager.find_dependencies()
    print("Введите число чтобы вызвать команду:\n" +
          "1 - Список всех входных параметров\n" +
          "2 - Список всех выходных параметров\n" +
          "3 - Добавить в используемые новый входной параметр\n" +
          "4 - Список всех используемых параметров\n" +
          "5 - Узнать что можно вычислить с используемых параметров и каких еще не хватает\n" +
          "6 - Узнать какие параметры нужны для рассчета выбранного выходного параметра\n"
          )
    while True:
        command = int(input("Введите номер команды: \n"))
        if command == 1:
            print("Все входные параметры:")
            print(manager.all_inputs)
        if command == 2:
            print("Все выходные параметры:")
            print(list(manager.dependencies.keys()))
        if command == 3:
            param = input("Введите входной параметр чтобы добавить его в используемые: \n")
            manager.add_new_using_param(param)
        if command == 4:
            print("Все используемые параметры:")
            print(manager.using_params)
        if command == 5:
            manager.get_info_about_inputs_params()
        if command == 6:
            param = input("Введите выходной параметр чтобы узнать что нужно для его расчета: \n")
            manager.get_info_about_output_param(param)


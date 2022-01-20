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

    def get_all_input_params_for_out(self, name_out_param: str):
        return [param for param in self.dependencies[name_out_param] if param not in self.using_params]

    def get_all_output_params_for_input(self, name_int_param: str):
        ans = []
        for key in self.dependencies.keys():
            if name_int_param in self.dependencies[key]:
                ans.append(key)
        return ans

    def get_info_about_input_param(self, name_int_param: str):
        if name_int_param in self.all_inputs:

            out_puts = self.get_all_output_params_for_input(name_int_param)
            for out_put in out_puts:
                needed_input = self.get_all_input_params_for_out(out_put)
                if len(needed_input) == 0:
                    print(f'-{out_put}.')
                else:
                    print(f'-{out_put}. Не хватает: {self.get_all_input_params_for_out(out_put)}')
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
    print("Все входные параметры")
    print(manager.all_inputs)

    while True:
        param = input("Введите входной параметр чтобы узнать что можно посчитать: \n")
        manager.using_params.add(param)
        manager.get_info_about_input_param(param)

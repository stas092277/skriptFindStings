import re

upiRe = '(.*) = UserPortIn'
upoRe = '(.*) = UserPortOut'

dependencies = {}
all_inputs = set()
using_params = set()


def writingFile(nameFile, lines):
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

    writingFile("UserPortIn.txt", upi_set)
    writingFile("UserPortOut.txt", upo_set)
    writingFile("UserPortInAndOut.txt", both_set)


def find_dependensis():
    with open('default_simple_python_block.py', 'r') as file:
        text = file.read()

    text = text.replace('\n', '')
    classes = text.split('class')
    classes.pop(0)

    for tmp in classes:
        ins = re.findall(r'(\w+) = UserPortIn', tmp)
        out = re.findall(r'(\w+) = UserPortOut', tmp)
        dependencies[out[0]] = ins
        for tmp in ins:
            all_inputs.add(tmp)


def get_all_input_params_for_out(name_out_param: str):
    return [param for param in dependencies[name_out_param] if param not in using_params]


def get_all_output_params_for_input(name_int_param: str):
    ans = []
    for key in dependencies.keys():
        if name_int_param in dependencies[key]:
            ans.append(key)
    return (ans)


def get_info_about_input_param(name_int_param: str):
    if name_int_param in all_inputs:

        out_puts = get_all_output_params_for_input(name_int_param)
        for out_put in out_puts:
            needed_input = get_all_input_params_for_out(out_put)
            if len(needed_input) == 0:
                print(f'-{out_put}.')
            else:
                print(f'-{out_put}. Не хватает: {get_all_input_params_for_out(out_put)}')
    else:
        raise ValueError("Нет такого параметра")


if __name__ == '__main__':
    #find_names()
    find_dependensis()
    print("Все входные параметры")
    print(all_inputs)

    # print(get_all_input_params_for_out('дальность_обнаружения'))
    # print(get_all_output_params_for_input('КУ_антенны'))
    while True:
        param = input("Введите входной параметр чтобы узнать что можно посчитать: \n")
        using_params.add(param)
        get_info_about_input_param(param)

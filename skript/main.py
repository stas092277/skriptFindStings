import re

upiRe = '(.*) = UserPortIn'
upoRe = '(.*) = UserPortOut'


def writingFile(nameFile, lines):
    with open(nameFile, "w") as file:
        for line in lines:
            file.write(line + '\n')


def find():
    file = open('default_simple_python_block.py', mode='r', encoding='utf-8-sig')
    lines = file.readlines()
    file.close()

    upi_set = set()
    upo_set = set()
    both_set = set()
    for line in lines:
        if re.match(upiRe, line) is not None:
            line = line.replace('#', "").replace(" ", "").removesuffix("=UserPortIn()\n")
            upi_set.add(line)
        if re.match(upoRe, line) is not None:
            line = line.replace("type=np.ndarray", "").replace('#', "").replace(" ", "").removesuffix("=UserPortOut()\n")
            upo_set.add(line)

    both_set.update(upi_set, upo_set)

    writingFile("UserPortIn.txt", upi_set)
    writingFile("UserPortOut.txt", upo_set)
    writingFile("UserPortInAndOut.txt", both_set)


if __name__ == '__main__':
    find()

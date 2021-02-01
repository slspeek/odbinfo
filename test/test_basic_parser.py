" parser tests "
from odbinfo.parser.basic import parse


CODE = """
dim number1, number2 as integer
dim answer as integer

Myfunction("go for it")
console.writeline("enter first number")
number1=int(console.readline())
console.writeline("enter second number")
number2=int(console.readline())
total=number1+number2
console.writeline("the answer is "& answer)

"""


def test_parse():
    " call parse "
    parse("")


def test_parse_select():
    " call parse select"
    tree = parse(CODE)
    print(tree.toStringTree())

def test_parse_error():
    " call parse select"
    tree = parse('const a = 6')
    print(tree.toStringTree())

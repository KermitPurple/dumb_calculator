#!/usr/bin/env python3

OUT_FILENAME = 'dumb_calc.py'
MIN_NUMBER = 0
MAX_NUMBER = 100
OPERATIONS = ['+', '-', '*', '/']
OPERATION_FNS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
TAB = ' ' * 4

def write_calc():
    '''
    write a caluclator program the worst way possible
    '''
    with open(OUT_FILENAME, 'w') as file:
        file.write(
            'import sys\n\n'
            'print(\'Welcome to the worst calculator there is!\')\n'
            'num1 = int(input(\'Enter the first number> \'))\n'
            'op = input(\'Enter the operation> \')\n'
            'num2 = int(input(\'Enter the second number> \'))\n\n'
        )
        if_stmt = 'if'
        for op in OPERATIONS:
            op_fn = OPERATION_FNS[op]
            for num1 in range(MIN_NUMBER, MAX_NUMBER):
                for num2 in range(MIN_NUMBER, MAX_NUMBER):
                    try:
                        result = op_fn(num1, num2)
                    except ZeroDivisionError:
                        result = 'Undefined'
                    file.write(f'{if_stmt} num1 == {num1} and op == {op!r} and num2 == {num2}:\n{TAB}print(\'{num1} {op} {num2} = {result}\')\n')
                    if if_stmt == 'if':
                        if_stmt = 'elif'
        file.write(f'else:\n{TAB}print(\'Invalid arguments\')\n{TAB}sys.exit(1)')

def main():
    '''Driver Code'''
    write_calc()

if __name__ == '__main__':
    main()

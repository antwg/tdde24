from calc import *


def exec_program(code):
    if is_program(code):
        statements = program_statements(code)
        if is_statements(statements):
            for statement in statements:
                check_type(statement)

def check_type(statement):
    # if is_assignment(statement):
    #     print(statement[-1], '[-1]')
    #     x = 'res'
    #     y = statement[-1]
    #     exec("%s = %d" % (x,1))
    #     print(res)

    # if is_repetition(statement):
    #     print('repetition')
    #     if is_true(repetition_condition(statement)):
    #         print('true')
    #         for element in statement[2:]:
    #             print(element)
    #             check_type(element[2])
    #         is_repetition(element)

    if is_selection(statement):
        if condition(selection_condition(statement)):
            check_type(statement[2])
            exec_program(['calc'] + statement[3:])
        else:
            exec_program(['calc'] + statement[3:])

    elif is_output(statement):
        if is_binaryexpr(output_expression(statement)):
            print(binary_expression(statement[-1]))
        else:
            print(statement)

    # elif is_input(statement):
    #     statement[0] = input()

    # elif is_binaryexpr(statement):
    #     print(statement)
    #     return binary_expression(statement)
    else:
        print('else')

def condition(value):
    if value[1] == '>':
        return (value[0] > value[-1])
    elif value[1] == '<':
        return (value[0] < value[-1])
    else:
        return (value[0] == value[-1])

def binary_expression(expression):
    if expression[1] == '+':
        return expression[0] + expression[2]
    elif expression[1] == '-':
        return expression[0] - expression[2]
    elif expression[1] == '*':
        return expression[0] * expression[2]
    elif expression[1] == '/':
        return expression[0] / expression[2]

#            first_statement(statements)
# calc1 = ['calc', ['print', 2], ['print', 4]]
# exec_program(calc1)
#
# calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
# exec_program(calc2)

calc4 = ['calc', ['print', [5, '+', 4]]]
exec_program(calc4)

"""
COMMA = ',' ;

PROGRAM = '[', "'calc'", COMMA, STATEMENTS, ']' ;

STATEMENTS = STATEMENT | STATEMENT, COMMA, STATEMENTS ;

STATEMENT = SELECTION | OUTPUT ;

SELECTION = '[', "'if'", COMMA, CONDITION, COMMA, STATEMENT, [COMMA, STATEMENT], ']'

OUTPUT = '[', "'print'", COMMA, EXPRESSION, ']' ;

EXPRESSION = CONSTANT | BINARYEXPR ;

BINARYEXPR = '[', EXPRESSION, COMMA, BINARYOPER, COMMA, EXPRESSION, ']' ;

CONDITION = '[', EXPRESSION, COMMA, CONDOPER, COMMA, EXPRESSION, ']' ;

BINARYOPER = "'+'" | "'-'" | "'*'" | "'/'" ;

CONDOPER = "'<'" | "'>'" | "'='" ;

CONSTANT = ? a Python number ? ;
"""

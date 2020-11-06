from calc import *


def exec_program(code):
    if is_program(code):
        statements = program_statements(code)
        if is_statements(statements):
            for statement in statements:
                check_type(statement)
        else:
            print('else')
            raise SyntaxError("A statement couldn't be interpreted.")
    else:
        raise SyntaxError("Can't interpret as a calc program.")

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
            if len(statement) == 3:
                check_type(statement[2])
            else:
                check_type(statement[2])
                exec_program(['calc'] + statement[3:])
        else:
            exec_program(['calc'] + statement[3:])

    elif is_output(statement):
        if is_binaryexpr(output_expression(statement)):
            print(binary_expression(statement[-1]))
        elif isinstance(statement[-1], int) :
            print(statement[-1])
        else:
            raise SyntaxError('Invalid expression')

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
    elif value[1] == '=':
        return (value[0] == value[-1])
    else:
        raise SyntaxError("Not a valid CONDOPER")

def binary_expression(expression):
    if expression[1] == '+':
        return expression[0] + expression[2]
    elif expression[1] == '-':
        return expression[0] - expression[2]
    elif expression[1] == '*':
        return expression[0] * expression[2]
    elif expression[1] == '/':
        return expression[0] / expression[2]

"""The tests"""
# calc1 = ['calc', ['print', 1]]
# """Tests if output works with a constant"""
# exec_program(calc1)
#
# calc2 = ['calc', ['print', 'a']]
# """Make sure if it does not work with a non valid constant"""
# exec_program(calc2)
#
# calc3 = ['calc', ['print', 1], ['print', [5, '+', 4]]]
# """Test if output works with expressions"""
# exec_program(calc3)
#
# calc4 = ['calc', ['print', 1], ['print', [5, '%', 4]]]
# """Test when given a non valid BINARYOPER"""
# exec_program(calc4)
#
# calc5 = ['calc', ['if', [4, '<', 6], ['print', 2], ['print', 4]]]
# """Tests if proram works if statement is True"""
# exec_program(calc5)
#
# calc6 = ['calc', ['if', [4, '!=', 6], ['print', 2]]]
# """Tests if proram works with non valid condoperator"""
# exec_program(calc6)
#
# calc7 = ['calc', ['if', [4, '>', 6], ['print', 2], ['print', 4]]]
# """Tests if proram works if statement is False"""
# exec_program(calc7)
#
# calc8 = ['calc', ['if', [4, '>', 6], ['print', 2], 'print', 4]]
# """Tests if the structure is incorrect"""
# exec_program(calc8)
#
# calc9 = ['calc']
# exec_program(calc9)

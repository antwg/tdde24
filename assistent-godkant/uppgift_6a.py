#Anton Wegeström antwe841
#Christopher Wåtz chrwa634

from calc import *

def exec_program(code, input_table = {}):
    """Runs a program"""
    if is_program(code):
        statements = program_statements(code)
        if is_statements(statements):
            return exec_statements(statements, input_table)

        else:
            raise SyntaxError("A statement couldn't be interpreted.")
    else:

        raise SyntaxError("Can't interpret as a calc program.")


def exec_statements(statements, input_table):
    #calc1 = ['calc', ['print', 5], ['set', 'a', 5], ['print', 'a']]
    statement_first = first_statement(statements)
    statements_rest = rest_statements(statements)

    variabletable = exec_statement(statement_first, input_table)

    if empty_statements(rest_statements(statements)):

        return variabletable

    return exec_statements(rest_statements(statements), variabletable)


def exec_statement(statement, variabletable):
    """Checks the type of a given statement"""
    if is_assignment(statement):
        return exec_assignment(statement, variabletable)

    elif is_repetition(statement):
        return exec_repetion(statement, variabletable)

    elif is_selection(statement):
        return exec_condition(statement, variabletable)

    elif is_output(statement):
        return exec_output(statement, variabletable)

    elif is_input(statement):
        return exec_input(statement, variabletable)
    else:
        raise SyntaxError('A statement could no be interpreted.')


def exec_expression(expression, variabletable):
    """Calculates and/or returns expression as integer/float."""

    if is_binaryexpr(expression):
        return binary_expression(expression, variabletable)

    elif isinstance(expression, (int, float)):
        return expression

    elif is_variable(expression):
        return variabletable[expression]

    else:
        raise SyntaxError(str(expression) + """: The given expression was not
        a valid expression""")


def exec_input(statement, variabletable):
    """Assigns a value to a variable given by user input"""

    variabletable_c = variabletable.copy()

    variabletable_c[input_variable(statement)] = int(input('Enter value for '
        + input_variable(statement) + ': '))

    return variabletable_c


def exec_assignment(statement, variabletable):
    """Assigns a value to a variable given by the program"""

    variabletable_c = variabletable.copy()

    expression = exec_expression(assignment_expression(statement), variabletable)
    variable = assignment_variable(statement)

    variabletable_c[variable] = expression


    return variabletable_c


def exec_output(statement, variabletable):
    """Prints a given expression"""
    expression = exec_expression(output_expression(statement), variabletable)
    if is_variable(output_expression(statement)):
        print(output_expression(statement), '=', expression)
        return variabletable
    else:
        print(expression)
        return variabletable


def exec_condition(statement, variabletable):
    """Checks if condition is met"""

    condition_value = condition(selection_condition(statement), variabletable)

    if condition_value:
        return exec_statement(statement[2], variabletable)

    elif not condition_value and len(statement) >= 4:
        return exec_statement(statement[3], variabletable)

    elif not condition_value:
        return variabletable

    else:
        raise SyntaxError("In exec condition: invalid condition")


def condition(value, variabletable):
    """Compares 2 expressions"""
    left = exec_expression(value[0], variabletable)
    right = exec_expression(value[2], variabletable)

    if value[1] == '>':
        return left > right
    elif value[1] == '<':
        return left < right
    elif value[1] == '=':
        return left == right
    else:
        raise SyntaxError("Not a valid CONDOPER.")


def binary_expression(expression, variabletable):
    """Performs a chosen binary expression on 2 expresssions"""
    left = exec_expression(binaryexpr_left(expression), variabletable)
    right = exec_expression(binaryexpr_right(expression), variabletable)

    if expression[1] == '+':
        return left + right
    elif expression[1] == '-':
        return left - right
    elif expression[1] == '*':
        return left * right
    elif expression[1] == '/':
        return left / right
    else:
        raise SyntaxError('Not binary expression')


def exec_repetion(statement, variabletable):
    """Performs statement while condition is true"""
    variabletable_c = variabletable.copy()

    condition_rep = repetition_condition(statement)
    statement_rep = repetition_statements(statement)

    if condition(condition_rep, variabletable_c):

        variabletable_c = exec_statements(statement_rep, variabletable_c)

        return exec_statement(statement, variabletable_c)

    return variabletable_c

"""The tests"""
# calc1 = ['calc', 'print', 1]
# """Tests with invalid statement"""
# exec_program(calc1)
#
# calc2 = ['print', 1]
# """Tests with invalid structure"""
# exec_program(calc2)
#
# calc3 = ['calc']
# """Tests with 0 statements"""
# exec_program(calc3)
#
# calc4 = ['calc', ['if', [4, '!=', 6], ['print', 2]]]
# """"Tests an invalid condoperator"""
# exec_program(calc4)

# calc5 = ['calc', ['if', [[5, '%', 4], '<', 6], ['print', 2]]]
# """Tests an invalid binary operator"""
# exec_program(calc5)
#
# calc6 = ['calc',[ 'set', 'x', 'a']]
# """Tries to assign non numeric value to variable"""
# exec_program(calc6)

from calc import *

#returnar inte nått värde
def exec_program(code, input_table = {}):
    if is_program(code):
        statements = program_statements(code)
        if is_statements(statements):
            #creates a copy of the input table so the function is not destructive
            variabletable = input_table.copy()
            variabletable = exec_statement(first_statement(statements), variabletable)

            exec_program(['calc'] + rest_statements(statements), variabletable)


            #if changes were made in the variable table return the new table
            if input_table != variabletable:
                return variabletable

            else:
                return input_table

        else:
            raise SyntaxError("A statement couldn't be interpreted.")

    else:
        raise SyntaxError("Can't interpret as a calc program.")


def exec_statement(statement, variabletable):
    """Checks the type of a given statement"""
    if is_assignment(statement):
        exec_assignment(statement, variabletable)

    elif is_repetition(statement):
        exec_repetion(statement, variabletable)

    elif is_selection(statement):
        exec_condition(statement, variabletable)

    elif is_output(statement):
        return exec_output(statement, variabletable)

    elif is_input(statement):
        return exec_input(statement, variabletable)


def exec_expression(expression, variabeltable):
    """Calculates and/or returns expression as integer/float."""
    if is_binaryexpr(expression):
        return binary_expression(expression, variabletable)

    elif isinstance(expression, (int, float)):
        return (expression, variabletable)

    elif expression in variabletable:
        return (variabletable[expression], variabletable)


def exec_input(statement, variabletable):
    """Assigns a value to a variable given by user input"""

    variabletable[input_variable(statement)] = int(input('Enter value for '
        + input_variable(statement) + ': '))

    return variabletable


def exec_assignment(statement, variabletable):
    """Assigns a value to a variable given by the program"""
    expression = exec_expression(assignment_expression(statement), variabletable)
    variable = assignment_variable(statement)

    variabletable[variable] = expression

    return variabletable


def exec_output(statement, variabletable):
    """Prints a given expression"""
    expression = exec_expression(output_expression(statement), variabletable)

    print(expression)


def exec_condition(statement, variabletable):
    """Checks if condition is met"""
    condition_value = condition(selection_condition(statement), variabletable)

    if condition_value:
        exec_program(statement[2], variabletable)

    elif not condition_value and len(statement) >= 4:
        exec_program(statement[3], variabletable)

    elif not condition_value:
        pass

    else:
        raise SyntaxError("In exec condition: invalid condition")


def condition(value, variabletable):
    """Compares 2 expressions"""
    left = exec_expression(statement[0], variabletable)
    right = exec_expression(statement[2], variabletable)

    if statement[1] == '>':
        return left > right
    elif statement[1] == '<':
        return left < right
    elif statement[1] == '=':
        return left == right
    else:
        raise SyntaxError("Not a valid CONDOPER.")


def binary_expression(expression, variabletable):
    """Performs a chosen binary expression on 2 expresssions"""
    # statement = expression.copy()
    # if not isinstance(statement[0], (int, float)):
    #     if isinstance(statement[0], list):
    #         statement[0] = binary_expression(statement[0], variabletable)
    #     elif statement[0] in variabletable:
    #         statement[0] = variabletable[statement[0]]
    #     else:
    #         raise SyntaxError("In binary expression: The expression could not \
    #         be interpreted")
    #
    # if not isinstance(statement[2], (int, float)):
    #     if isinstance(statement[2], list):
    #         statement[2] = binary_expression(statement[2])
    #     elif statement[2] in variabletable:
    #         statement[2] = variabletable[statement[2]]
    #     else:
    #         raise SyntaxError("In binary expression: The expression could not \
    #         be interpreted")

    left = exec_expression(binaryexpr_left, variabletable)
    right = exec_expression(binaryexpr_right, variabletable)

    if statement[1] == '+':
        return left + right
    elif statement[1] == '-':
        return left - right
    elif statement[1] == '*':
        return left * right
    elif statement[1] == '/':
        return left / right
    else:
        raise SyntaxError('Not binary expression')


def exec_repetion(statement, variabletable):
    """Performs statement while condition is true"""
    condition_rep = repetition_condition(statement)
    statement_rep = repetition_statements(statement)

    if condition(condition_rep, variabletable):

        for i in range(len(statement_rep)):

            exec_statement(statement_rep[i], variabletable)

        exec_statement(statement, variabletable)

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
#
# calc5 = ['calc', ['if', [[5, '%', 4], '<', 6], ['print', 2]]]
# """Tests an invalid binary operator"""
# exec_program(calc5)
# calc6 = ['calc',[ 'set', 'x', 'a']]
# """Tries to assign non numeric value to variable"""
# exec_program(calc6)

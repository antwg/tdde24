from calc import *

#returnar inte nått värde
def exec_program(code, input_table = {}):
    if is_program(code):
        statements = program_statements(code)
        if is_statements(statements):
            variabletable = input_table.copy()
            for statement in statements:
                check = check_type(statement, variabletable)
                if isinstance(check, dict):
                    variabletable = (check)
                else:
                    check
            return variabletable

        else:
            raise SyntaxError("A statement couldn't be interpreted.")
    else:
        raise SyntaxError("Can't interpret as a calc program.")

def check_type(statement, variabletable):
    if is_assignment(statement):
        eval_assignment(statement, variabletable)

    elif is_repetition(statement):
        condition_rep = repetition_condition(statement)
        statement_rep = repetition_statements(statement)
        if condition(condition_rep, variabletable):
            for i in range(len(statement_rep)):
                if is_input(statement_rep[i]):
                    variabletable = exec_input(statement_rep[i], variabletable)
                elif is_assignment(statement_rep[i]):
                    variabeltable = eval_assignment(statement_rep[i], variabletable)
                elif is_selection(statement_rep[i]):
                    pass
                elif is_output(statement_rep[i]):
                    check_type(statement_rep[i], variabeltable)
                else:
                    raise SyntaxError('in repetion')
            check_type(statement, variabletable)

    elif is_selection(statement):
        eval_condition(statement, variabletable)

    elif is_output(statement):
        return exec_output(statement, variabletable)

    elif is_input(statement):
        return exec_input(statement, variabletable)


def exec_input(statement, variabletable):
    variabletable[input_variable(statement)] = int(input('Enter a value for '
        + input_variable(statement) + ': '))
    return variabletable


def eval_assignment(statement, variabletable):

    expression = assignment_expression(statement)
    variabel = assignment_variable(statement)

    if is_binaryexpr(expression):
        expression = binary_expression(expression, variabletable)
        variabletable[variabel] = expression
        return variabletable
    elif isinstance(expression, (int, float)):
        variabletable[variabel] = expression
        return variabletable
    elif expression in variabletable:
        variabletable[variabel] = variabletable[expression]
        return variabletable
    else:
        raise SyntaxError('Invalid assignment.')

def exec_output(statement, variabletable):

    expression = output_expression(statement)
    if is_binaryexpr(expression):
        print(binary_expression(expression))
    elif isinstance(expression, (int, float)):
        print(expression)
    elif expression in variabletable:
        print(expression, ' = ', variabletable[expression])
        return(expression, ' = ', variabletable[expression])
        """Radbryt"""
    else:
        raise SyntaxError('Invalid expression.')


def eval_condition(statement, variabletable):
    if condition(selection_condition(statement), variabletable):
        if len(statement) == 3:
            check_type(statement[2], variabletable)
        else:
            check_type(statement[2], variabletable)
            exec_program(['calc'] + statement[3:], variabletable)
    else:
        exec_program(['calc'] + statement[3:], variabletable)

def condition(value, variabletable):
    statement = value.copy()
    if not isinstance(statement[0], (int, float)):
        if isinstance(statement[0], list):
            statement[0] = binary_expression(statement[0])
        elif statement[0] in variabletable:
            statement[0] = variabletable[statement[0]]
        else:
            raise SyntaxError("In condition.")

    if not isinstance(statement[2], (int, float)):
        if isinstance(statement[2], list):
            statement[2] = binary_expression(statement[2])
        elif statement[2] in variabletable:
            statement[2] = variabletable[statement[2]]
        else:
            raise SyntaxError("In condition.")

    if statement[1] == '>':
        return (statement[0] > statement[-1])
    elif statement[1] == '<':
        return (statement[0] < statement[-1])
    elif statement[1] == '=':
        return (statement[0] == statement[-1])
    else:
        raise SyntaxError("Not a valid CONDOPER.")

def binary_expression(expression, variabletable):
    statement = expression.copy()
    if not isinstance(statement[0], (int, float)):
        if isinstance(statement[0], list):
            statement[0] = binary_expression(statement[0], variabletable)
        elif statement[0] in variabletable:
            statement[0] = variabletable[statement[0]]
        else:
            raise SyntaxError("In binary expression.")

    if not isinstance(statement[2], (int, float)):
        if isinstance(statement[2], list):
            statement[2] = binary_expression(statement[2])
        elif statement[2] in variabletable:
            statement[2] = variabletable[statement[2]]
        else:
            raise SyntaxError("In binary expression.")

    if statement[1] == '+':
        return statement[0] + statement[2]
    elif statement[1] == '-':
        return statement[0] - statement[2]
    elif statement[1] == '*':
        return statement[0] * statement[2]
    elif statement[1] == '/':
        return statement[0] / statement[2]

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
#
# calc10 = ['calc', ['if', [[8, '+', 2], '<', 6], ['print', 2], ['print', 4]]]
# """Tests if proram works if statement is True"""
# exec_program(calc10)
#
# calc11 = ['calc', ['if', [[3, '+', 2], '<', 'a'], ['print', 2], ['print', 4]]]
# """Tests if proram works if statement is True"""
# exec_program(calc11, {'a': 5})
# calc12 = ['calc', ['set', 'x', 7],['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'z']]
# print(exec_program(calc12))


# calc3 = ['calc', ['read', 'p1'], ['print', 'p1']]
# exec_program(calc3, {'p0': 3})

calc2 = calc4 = ['calc', ['read', 'n'],['set', 'sum', 0], ['while', ['n', '>', 0], ['set', 'sum', ['sum', '+', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']]
exec_program(calc2)

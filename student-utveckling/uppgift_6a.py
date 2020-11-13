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

            if input_table != variabletable:
                return variabletable
            else:
                return input_table

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
    variabletable[input_variable(statement)] = int(input('Enter value for '
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
    print(expression)
    if is_binaryexpr(expression):
        print(binary_expression(expression), end='\n')
    elif isinstance(expression, (int, float)):
        print(expression, end='\n')
    elif expression in variabletable:
        print(expression, '=', variabletable[expression], end='\n')


    else:
        raise SyntaxError('Invalid expression.')

def eval_condition(statement, variabletable):
    if condition(selection_condition(statement), variabletable):
        check_type(statement[2], variabletable)
        # else:
        #     check_type(statement[2], variabletable)
        #     exec_program(['calc'] + statement[3:], variabletable)
    elif not condition(selection_condition(statement), variabletable)\
    and len(statement) >= 4:
        check_type(statement[3], variabletable)

    elif not condition(selection_condition(statement), variabletable):
        pass

    else:
        raise SyntaxError(statement)

def condition(value, variabletable):
    statement = value.copy()
    if not isinstance(statement[0], (int, float)):
        if isinstance(statement[0], list):
            statement[0] = binary_expression(statement[0],variabletable)
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
    else:
        raise SyntaxError('Not binary expression')

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

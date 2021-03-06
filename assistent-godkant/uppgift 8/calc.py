# ----------------------------------------------------------------------------
#  Primitive functions for the ConstCalc and Calc language constructs
# ----------------------------------------------------------------------------


# ----- PROGRAM -----


def is_program(p):
    return isinstance(p, list) and len(p) > 1 and p[0] == 'calc'


def program_statements(p):
    # The first item is 'calc', the rest are the statements
    return p[1:]


# ----- STATEMENTS -----


def is_statements(p):
    # A non-empty list of statements
    return isinstance(p, list) and p and all(is_statement(s) for s in p)


def first_statement(p):
    return p[0]


def rest_statements(p):
    return p[1:]


def empty_statements(p):
    return not p


# ----- STATEMENT -----


def is_statement(s):
    return (
        is_assignment(s)
        or is_repetition(s)
        or is_selection(s)
        or is_output(s)
        or is_input(s)
    )


# ----- ASSIGNMENT -----


def is_assignment(p):
    return isinstance(p, list) and len(p) == 3 and p[0] == 'set'


def assignment_variable(p):
    return p[1]


def assignment_expression(p):
    return p[2]


# ----- REPETITION -----


def is_repetition(p):
    return isinstance(p, list) and len(p) > 2 and p[0] == 'while'


def repetition_condition(p):
    return p[1]


def repetition_statements(p):
    return p[2:]


# ----- SELECTION -----


def is_selection(p):
    return isinstance(p, list) and (3 <= len(p) <= 4) and p[0] == 'if'


def selection_condition(p):
    return p[1]


def selection_true_branch(p):
    return p[2]


def selection_has_false_branch(p):
    return len(p) == 4


def selection_false_branch(p):
    return p[3]


# ----- INPUT -----


def is_input(p):
    return isinstance(p, list) and len(p) == 2 and p[0] == 'read'


def input_variable(p):
    return p[1]


# ----- OUTPUT -----


def is_output(p):
    return isinstance(p, list) and len(p) == 2 and p[0] == 'print'


def output_expression(p):
    return p[1]


# ----- EXPRESSION -----

# No functions for expressions in general. Instead, see the differenct
# types of expressions: constants, variables and binary expressions.


# ----- BINARYEXPR -----


def is_binaryexpr(p):
    return isinstance(p, list) and len(p) == 3 and is_binaryoper(p[1])


def binaryexpr_operator(p):
    return p[1]


def binaryexpr_left(p):
    return p[0]


def binaryexpr_right(p):
    return p[2]


# ----- CONDITION -----


def is_condition(p):
    return isinstance(p, list) and len(p) == 3 and is_condoper(p[1])


def condition_operator(p):
    return p[1]


def condition_left(p):
    return p[0]


def condition_right(p):
    return p[2]


# ----- BINARYOPER -----


def is_binaryoper(p):
    return p in ['+', '-', '*', '/']


# ----- CONDOPER -----


def is_condoper(p):
    return p in ['<', '>', '=']


# ----- VARIABLE -----


def is_variable(p):
    return isinstance(p, str) and p != ""

# ----- CONSTANT -----


def is_constant(p):
    return isinstance(p, int) or isinstance(p, float)


# ----------------------------------------------------------------------------
#  Grammar for the *complete* Calc language
# ----------------------------------------------------------------------------

"""

    (* F??r att vi inte sj??lva ska r??ka l??sa fel och blanda ihop EBNF-komma
    och det ',' som ing??r i v??rt spr??k skapar vi en icke-terminal f??r detta... *)
    COMMA = ',' ;

    (* Ett program best??r av en f??ljd av satser.  Eftersom ordet calc ska st?? inom 
    apostrofer beh??ver vi l??gga detta inom citattecken i grammatiken. J??mf??r med att 
    hakparenteserna ska vara utan apostrofer i v??rt spr??k, men *har* en niv?? av 
    apostrofer i grammatiken. *)
    PROGRAM = '[', "'calc'", COMMA, STATEMENTS, ']' ;

    (* STATEMENTS ??r ett ensamt STATEMENT, eller ett STATEMENT f??ljt av komma 
           och STATEMENTS (som i sin tur ??r 1 STATEMENT som m??jligen f??ljs av flera,
        och s?? vidare).  *)
    STATEMENTS = 
        STATEMENT
      | STATEMENT, COMMA, STATEMENTS ;
    
    (* En sats kan vara en tilldelning, en upprepning, ett val,
       en inmatning eller en utmatning. *)
    STATEMENT =
        ASSIGNMENT
      | REPETITION
      | SELECTION
      | INPUT
      | OUTPUT ;

    (* En tilldelning best??r av en variabel och ett uttryck vars v??rde ska ber??knas
       f??r att sedan kopplas till det givna variabelnamnet. *)
    ASSIGNMENT = '[', "'set'", COMMA, VARIABLE, COMMA, EXPRESSION, ']' ;

    (* En upprepning best??r av ett villkorsuttryck och en f??ljd av satser,
       vilka upprepas s?? l??nge villkorsuttrycket ??r sant.  *)
    REPETITION = '[', "'while'", COMMA, CONDITION, COMMA, STATEMENTS, ']' ;

    (* Ett val best??r av ett villkorsuttryck f??ljt av en eller tv?? satser.
       Den f??rsta satsen utf??rs om villkorsuttrycket ??r sant,
       den andra (om den finns) om villkorsuttrycket ??r falskt.
       Notera att [ ... ] betyder att det som st??r inom hakparenteserna
       f??r utel??mnas ("optional").  *)
    SELECTION = '[', "'if'", COMMA, CONDITION, COMMA, STATEMENT, [COMMA, STATEMENT], ']'

    (* En inmatningssats anger namnet p?? en variabel som ska f?? ett
       numeriskt v??rde av anv??ndaren. *)
    INPUT = '[', "'read'", COMMA, VARIABLE, ']' ;

    (* En utmatningssats anger ett uttryck vars v??rde ska skrivas ut. *)
    OUTPUT = '[', "'print'", COMMA, EXPRESSION, ']' ;

    (* Ett matematiskt uttryck kan vara en konstant, en variabel eller
       ett bin??rt uttryck. *)
    EXPRESSION =
        CONSTANT
      | VARIABLE
      | BINARYEXPR ;

    (* Ett bin??rt uttryck best??r av tv?? uttryck med en matematisk operator i mitten. *)
    BINARYEXPR = '[', EXPRESSION, COMMA, BINARYOPER, COMMA, EXPRESSION, ']' ;

    (* Ett villkor best??r av tv?? uttryck med en villkorsoperator i mitten. *)
    CONDITION = '[', EXPRESSION, COMMA, CONDOPER, COMMA, EXPRESSION, ']' ;

    (* En bin??roperator symboliserar ett av de fyra grundl??ggande r??knes??tten.
       Eftersom man i spr??ket m??ste skriva detta med citattecken som i
           [10, "+", 20]
       m??ste vi h??r ha med *dubbla* citattecken.  Om vi bara skrev '+'
       skulle uttrycket vara
           [10, +, 20]
       vilket inte kan tolkas i Python.
    *)
    BINARYOPER = "'+'" | "'-'" | "'*'" | "'/'" ;

    (* En villkorsoperator ??r st??rre ??n, mindre ??n eller lika med. *)
    CONDOPER = "'<'" | "'>'" | "'='" ;

    (* En variabel ??r en str??ng definierad som i Python -- str??ngen anger
       namnet p?? variabeln.  Text mellan tv?? fr??getecken anger att n??got
       ??r definierat utanf??r EBNF -- vi g??r allts?? inte s?? l??ngt som att
       vi definierar exakt hur en str??ng ser ut. *)
    VARIABLE = ? a Python string ? ;

    (* En konstant ??r ett tal i Python. *)
    CONSTANT = ? a Python number ? ;
"""

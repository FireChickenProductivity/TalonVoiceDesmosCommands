from talon import actions, Module, settings

module = Module()

button_delay_setting_name = 'desmos_matrix_button_delay'
button_delay = 'user.' + button_delay_setting_name
module.setting(
    button_delay_setting_name,
    type = str,
    default = 400,
    desc = 'How long to wait between button presses in the matrix calculator in milliseconds',
)

matrix_creation_key_delay_setting_name = 'desmos_matrix_creation_key_delay'
matrix_creation_key_delay = 'user.' + matrix_creation_key_delay_setting_name
module.setting(
    matrix_creation_key_delay_setting_name,
    type = str,
    default = 3,
    desc = 'How long to wait between key presses in milliseconds when creating a new matrix.'
)

@module.capture(rule = 'one|two|three|four|five|six')
def desmos_matrix_dimension(m) -> int:
    symbol = m[0]
    if symbol == 'one':
        return 1
    elif symbol == 'two':
        return 2
    elif symbol == 'three':
        return 3
    elif symbol == 'four':
        return 4
    elif symbol == 'five':
        return 5
    elif symbol == 'six':
        return 6


@module.action_class
class Actions:
    def desmos_new_matrix(rows: int, columns: int):
        '''Creates new matrix with the specified dimensions'''
        start_new_matrix()
        wait_button_delay()
        give_matrix_dimensions(rows, columns)
def start_new_matrix():
    #Enter is pressed before tabbing over to the matrix so that if the current calculation has a 
    # decimal result the first tab will not toggle fraction verses decimal display
    actions.key('enter')
    actions.key('tab enter')

def wait_button_delay():
    actions.sleep(f'{settings.get(button_delay)}ms')
def wait_matrix_key_delay():
    actions.sleep(f'{settings.get(matrix_creation_key_delay)}ms')

#Default Dimensions of a Matrix When Created in the Calculator
DEFAULT_ROWS = 2
DEFAULT_COLUMNS = 2

#The maximum number of rows that the calculator can handle
MAX_ROWS = 6

# These constants indicate the number of tabs needed to reach a button from the starting position after creating a matrix
FEWER_ROWS_POSITION = 4
MORE_ROWS_POSITION = 5
FEWER_COLUMNS_POSITION = 6
MORE_COLUMNS_POSITION = 7

#This code was taken from my dragon Desmos set up and could use some serious cleaning
def give_matrix_dimensions(rows: int, columns: int):
    position = 0 #The amount of tabs it takes to reach the currently selected position
    fewerRowsNotClickable = False # if the number of rows is one, you cannot click the button to reduce the number of rows
    # which causes the program to skip that button when trying to return to the matrix from the buttons
    # this variable is used to take that into account when returning to the matrix
    moreRowsNotClickable = False #this variable keeps track of when the number of rows cannot be increased in the calculator
    fewerColumnsNotClickable = False
    if rows < DEFAULT_ROWS:
        press_key_amount('tab', FEWER_ROWS_POSITION)
        position = FEWER_ROWS_POSITION
        press_key_amount('enter', DEFAULT_ROWS - rows)
        if rows == 1:
            fewerRowsNotClickable = True
    elif rows > DEFAULT_ROWS:
            press_key_amount('tab', MORE_ROWS_POSITION)
            position = MORE_ROWS_POSITION
            press_key_amount('enter', rows - DEFAULT_ROWS)
    
    if rows == MAX_ROWS:
        moreRowsNotClickable = True
    
    wait_button_delay()

    if columns < DEFAULT_COLUMNS:
        press_key_amount('tab', FEWER_COLUMNS_POSITION - position)
        position = FEWER_COLUMNS_POSITION
        press_key_amount('enter', DEFAULT_COLUMNS - columns)
        if columns == 1:
            fewerColumnsNotClickable = True
    elif columns > DEFAULT_COLUMNS:
        press_key_amount('tab', MORE_COLUMNS_POSITION - position)
        position = MORE_COLUMNS_POSITION
        press_key_amount('enter', columns - DEFAULT_COLUMNS)
    
    wait_button_delay()

    if (fewerRowsNotClickable and position > FEWER_COLUMNS_POSITION) or \
        (moreRowsNotClickable and position > MORE_ROWS_POSITION):
        position -= 1
    if fewerColumnsNotClickable and fewerRowsNotClickable:
        position -= 1
    
    if position > 0:
        press_key_amount('shift-tab', position - FEWER_ROWS_POSITION + rows*columns)

        
def press_key_amount(key, amount):
    for i in range(amount):
        actions.key(f'{key}')
        wait_matrix_key_delay()




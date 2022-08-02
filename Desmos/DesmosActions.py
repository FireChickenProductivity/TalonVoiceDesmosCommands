from talon import actions, Module

module = Module()

@module.action_class
class SimpleActions:
    def desmos_insert_small_number(number: int):
        '''Inserts the small number. Used in overwriting a standard repeating command.'''
        number_text = str(number)
        actions.insert(number_text)
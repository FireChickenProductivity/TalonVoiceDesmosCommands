#This contains code for graphing calculator trig functions

from talon import actions, Module, Context

module = Module()
module.list('desmos_basic_trig_functions', desc = 'basic trig functions')

context = Context()
context.lists['user.desmos_basic_trig_functions'] = {
    'sine' : 'sin',
    'cosine' : 'cos',
    'tan' : 'tan',
    'tangent' : 'tan',
    'cosecant' : 'csc',
    'secant' : 'sec',
    'cotan' : 'cot',
    'cotangent' : 'cot',
}

@module.capture(rule = 'hyper|hype|hyperbolic')
def desmos_hyperbolic(m) -> str:
    return 'hyperbolic'

@module.capture(rule = '[arc|<user.desmos_hyperbolic>] {user.desmos_basic_trig_functions}')
def desmos_trig_function(m) -> str:
    if len(m) == 1:
        return get_trig_function_call(m[0])
    else:
        return get_modified_trig_function_call(m[0], m[1])


def get_trig_function_call(name):
    return f'{name}('

def get_modified_trig_function_call(modifier, name):
    result = name
    if modifier == 'arc':
        result = 'arc' + result
    elif modifier == 'hyperbolic':
        result += 'h'
    return get_trig_function_call(result)

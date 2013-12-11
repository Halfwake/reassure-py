import sys
import traceback
import random

OLD_DOC = sys.excepthook.__doc__

def doc_check(handler):
    "Will give the handler the __doc__ value of the original sys.excepthook, if it has a false value for its current __doc__ value. (e.g. \"\", None, False)"
    if not handler.__doc__:
        handler.__doc__ = OLD_DOC
    return handler

def set_hook(handler, do_doc_check = True):
    "Sets the excepthook to a new value while possibly adding a new __doc__ value."
    if do_doc_check:
        handler = doc_check(handler)
    sys.excepthook = handler

def print_err(message):
    print >>sys.stderr, message

def print_tb(tb):
    print_err('Traceback (most recent call last):')
    traceback.print_tb(tb)

HOOKS = {}

def default_hook_test(exc, value, tb):
    "Returns the same result as the default sys.excepthook would."
    print_tb(tb)
    print_err("%s: %s" % (exc.__name__, value))
    
HOOKS['test1'] = default_hook_test

def _lambda(exc, value, tb):
    gasp = random.choice([
        'Oh no! ;~;',
        'Uh oh...',
        'This doesn\'t look good!',
    ])
    closer = random.choice([
        'Better luck next time?',
        'Victory is getting up one more time than you fall!',
        'Up and at\'em!',
    ])
    closer = '~~' + closer + '~~'
    print_err(gasp)
    default_hook_test(exc, value, tb)
    print_err(closer)
HOOKS['chipper'] = _lambda

def set_hook_by_key(key):
    'Sets the new excepthook to the corresponding HOOKS value.'
    set_hook(HOOKS[key])

    

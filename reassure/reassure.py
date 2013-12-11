import sys
import traceback
import random
import webbrowser

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

def print_err(msg):
  sys.stderr.write(msg + '\n')

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

def _lambda(exc, value, tb):
  print_err('''\
I've tried so hard
  And got so far
    But in the end
      It doesn't even matter
      I had to fall
    To lose it all
  But in the end
It doesn't even matter
''')
  default_hook_test(exc, value, tb)
  greenday_video = 'http://www.youtube.com/watch?v=ZP-bAlOJzWc'
  webbrowser.open(greenday_video)
HOOKS['greenday'] = _lambda
  


def set_hook_by_key(key):
    'Sets the new excepthook to the corresponding HOOKS value.'
    set_hook(HOOKS[key])

    

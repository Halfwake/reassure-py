import sys
import traceback
import random
import webbrowser

OLD_DOC = sys.excepthook.__doc__

class Hooks(object):
  def __init__(self, hooks):
    self.hooks = dict([(hook.__name__, hook) for hook in hooks])
  def set_hook(self, key):
    'Sets the new excepthook to the corresponding value.'
    Hooks._set_hook(self.hooks[key])
  @staticmethod
  def _set_hook(handler, do_doc_check = True):
    "Sets the excepthook to a new value while possibly adding a new __doc__ value."
    if do_doc_check:
        handler = Hooks._doc_check(handler)
    sys.excepthook = handler
  @staticmethod
  def _doc_check(handler):
    "Will give the handler the __doc__ value of the original sys.excepthook, if it has a false value for its current __doc__ value. (e.g. \"\", None, False)"
    if not handler.__doc__:
        handler.__doc__ = OLD_DOC
    return handler
  @staticmethod
  def base_hook(exc, value, tb):
    "Returns the same result as the default sys.excepthook would."
    Hooks.print_tb(tb)
    Hooks.print_err("%s: %s" % (exc.__name__, value))
  @staticmethod
  def print_err(msg):
    sys.stderr.write(msg + '\n')
  @staticmethod
  def print_tb(tb):
      Hooks.print_err('Traceback (most recent call last):')
      traceback.print_tb(tb)

    


def chipper(exc, value, tb):
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
    Hooks.print_err(gasp)
    Hooks.base_hook(exc, value, tb)
    Hooks.print_err(closer)

def greenday(exc, value, tb):
  Hooks.print_err('''\
I've tried so hard
  And got so far
    But in the end
      It doesn't even matter
      I had to fall
    To lose it all
  But in the end
It doesn't even matter
''')
  Hooks.base_hook(exc, value, tb)
  greenday_video = 'http://www.youtube.com/watch?v=ZP-bAlOJzWc'
  webbrowser.open(greenday_video)

hooks = Hooks([chipper, greenday])
  



    

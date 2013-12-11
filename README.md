reassure-py
=================

Alleviate the pain of debugging with motivational error messages!

Bad Error Message
```
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>>
```

Good Error Message
```
>>> import reassure
>>> reassure.set_hook_by_key('chipper')
>>> 3 / 0
Oh no! ;~;
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
~~Up and at'em!~~
>>>
```


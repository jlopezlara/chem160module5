Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import exp
>>> def f(x):
	return x*exp(-x)

>>> # Numerically Integrate f(x) from 0 to 50
>>> intgrl+0.0
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    intgrl+0.0
NameError: name 'intgrl' is not defined
>>> x=0
>>> xmax=50
>>> dx=0.1
>>> while x<xmax:
	intgrl+=dx*f(x)
	x+=dx
print ("Integral=",intgrl,"error=",abs(1-intgrl))
SyntaxError: invalid syntax
>>> print ("Integral=",intgrl,"error=",abs(1-intgrl))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print ("Integral=",intgrl,"error=",abs(1-intgrl))
NameError: name 'intgrl' is not defined
>>> 

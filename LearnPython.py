Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> 9 - 8
1
>>> 4 * 6
24
>>> 8 / 4
2.0
>>> 5 /2
2.5
>>> 5 // 2
2
>>> 8 +  9 - 10
7
>>> 8 + 2 * 3
14
>>> (8 + 2) * 3
30
>>> 2 * 2 * 2
8
>>> 2 ** 3
8
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 'chung'
'chung'
>>> print('chung')
chung
>>> print ('chung's laptop)
SyntaxError: invalid syntax
>>> print("chung's laptop")
chung's laptop
>>> print('chung "laptop"')
chung "laptop"
>>> print('chung\'s "laptop"')
chung's "laptop"
>>> 'chung' + 'chung'
'chungchung'
>>> 10 * 'chung'
'chungchungchungchungchungchungchungchungchungchung'
>>> print('c:\docs\nchung')
c:\docs
chung
>>> print(r'c:\docs\nchung')
c:\docs\nchung
>>> 2 + 3
5
>>> x = 2
>>> x + 3
5
>>> y =3
>>> w + y
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    w + y
NameError: name 'w' is not defined
>>> y = 3
>>> x + y
5
>>> x = 9
>>> x + y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x + 10
19
>>> _ + y
22
>>> name = (chung)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    name = (chung)
NameError: name 'chung' is not defined
>>> name = 'chung'
>>> name + 'van'
'chungvan'
>>> name[0]
'c'
>>> name[3]
'n'
>>> name[-1]
'g'
>>> name[-4]
'h'
>>> name[0:3]
'chu'
>>> name[1:3]
'hu'
>>> name[1:]
'hung'
>>> name[:4]
'chun'
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> 'my' + name[3:]
'myng'
>>> myname = 'maivanchung'
>>> len(myname)
11
>>> nums = [25,12,36,95,,14]
SyntaxError: invalid syntax
>>> nums = [25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> num [0]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    num [0]
NameError: name 'num' is not defined
>>> nums [0]
25
>>> nums [4]
14
>>> nums[2]
36
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names = ['chung','mai','van']
>>> names
['chung', 'mai', 'van']
>>> values = [9.5,'chung', 25]
>>> mil = [nums, names]
>>> mil
[[25, 12, 36, 95, 14], ['chung', 'mai', 'van']]
>>> nums.append(45)
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend(29,12,14,36)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    nums.extend(29,12,14,36)
TypeError: extend() takes exactly one argument (4 given)
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min (nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
>>> s =  {22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s = {25,,14,98,63,75,98}
SyntaxError: invalid syntax
>>> s = {25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> help ()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> list

help> LIST
No Python documentation found for 'LIST'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> LISTS

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> num = 5
>>> id(num)
140729045639952
>>> name = 'chung'
>>> id(name)
2032479203992
>>> a =10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
140729045640112
>>> id(b)
140729045640112
>>> id(10)
140729045640112
>>> k = 10
>>> id (k)
140729045640112
>>> a = 9
>>> id(a)
140729045640080
>>> id (b)
140729045640112
>>> k = a
>>> id (k)
140729045640080
>>> b =8
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> type(PI)
<class 'float'>
>>> PI
3.15
>>> 

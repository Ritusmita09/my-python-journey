# object types [Data types]

- Number : 123456, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10)) #start from index 0
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yumm'}, dict(hours=10) #does not start from index 0
- Set : set('abc'), {'a','b','c'}
- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')
- Boolean : True , False
- None : None
- Functions, modules, classes

- Advance : Decorators, Generators, Iterators, MetaProgramming


- Practice in terminal
>>> 12+12
24
>>> 2.5 * 6.90
17.25
>>> 2**100
1267650600228229401496703205376
>>> 2^20
22
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random() 
0.27309259778925343
>>> random.choices([1, 2, 3, 4, 5])
[2]
>>> random.choices([1, 2, 3, 4, 5])
[3]
>>> username = "chaiaurcode"
>>> len(username)
11
>>> username[0]
'c'
>>> username[-3]
'o'
>>> username[1:3]
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> mylist = [123 , 'milk', 3.14]
>>> len
<built-in function len>
>>> (mylist)
[123, 'milk', 3.14]
>>> len(mylist)
3
>>> 
>>> mylist[0]
123
>>> mylist[-1]
3.14
>>> myD = {'one': 'lemon', 'two': 'ginger', 'superman':'spiderman'} 
>>> myD
{'one': 'lemon', 'two': 'ginger', 'superman': 'spiderman'}
>>> myD['two']
'ginger'
>>> myTup = (1, 2, 4, 6, 8)
>>> myTup[0]
1
>>> len(myTup)
5
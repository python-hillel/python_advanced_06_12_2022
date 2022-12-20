a = 'Testing ' \
    'the ' \
    'long ' \
    'string ' \
    'in ' \
    'Python'

b = '''Testing 
the 
    long 
        string 
    in 
Python


'''

c = """SELECT *
  FROM table
 WHERE field1 = 'Python';"""

print('"' + a + '"')
print('"' + b + '"')
print(c)

print('Testing '
      'the '
      'long '
      'string '
      'in '
      'Python')

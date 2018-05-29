

def whom_do_we_know():
  """lets create a few list comprehensions"""

  with_spaces = [
    'my value',
    'has spaces',
    'i want to',
    'change that to',
    'not be', ]

  add_stuff = [i.replace(' ','\t') for i in with_spaces]
  return '\t'.join(add_stuff)

   

def print_me(arg1):
  print(arg1)


print_me(whom_do_we_know())


# working with dicts

def a_dict_function():
  """lets play with some dicts"""
  a_dict = {
    'key1': 'value set',
    'key2': ['yeah',1,'or','more','values'],
    'key3': 3,
    'key4': {3,4,6,7},
    'key5': (3,),
    'key6': print_me(whom_do_we_know()),
    'key7': print_me,
    'key8': whom_do_we_know,
  }

  print_me(a_dict)
  print_me(a_dict['key1'])
  print_me(a_dict['key2'])
  print_me(a_dict['key3'])
  print_me(a_dict['key4'])
  print_me(a_dict['key5'])
  a_dict['key6']            # should be none
  a_dict['key7'](a_dict['key8']())  # this works

a_dict_function()
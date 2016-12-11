import random

class Stack:
  def __init__(self):
    self.arr = []
  
  def push(self, value):
    self.arr.append(value)
    
  def pop(self):
    if not self.arr:
      raise("Empty Stack")
    return self.arr.pop()
  
  def top(self):
    if not self.arr:
      raise("Empty Stack")
    return self.arr[-1]
  
  def is_empty(self):
    return not bool(self.arr)
    

def par_is_valid(inp):
  valid = True
  st = Stack()
  if not inp:
    return valid
  for par in inp:
    if par == '(':
      st.push(par)
    else:
      if st.is_empty():
        valid =  False
        break
      else:
        st.pop()
        
  return valid and st.is_empty() 

sequance1 = '()()(())'
sequance2 = ')())('

def test(test_count):
  for _ in range(test_count):
    length = random.randint(5, 20)
    test_str = ''.join([random.choice(['(', ')']) for _ in range(length)])
    opened_count = test_str.count('(')
    closed_count = test_str.count(')')
    is_equal=True if opened_count == closed_count else False
    
    print(test_str)
    print(opened_count, closed_count)
    assert not (par_is_valid(test_str) and not is_equal) 
    if par_is_valid(test_str):
      print(test_str)
  print("Test Passed!")
    
test(150)



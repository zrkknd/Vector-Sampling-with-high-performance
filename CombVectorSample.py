from scipy.special import comb
"""
use function CombVectorSample.GetCombVector(n,m,x) to get a combination vector
"""

class CombVectorCalc():
  """
  A Class to calculate a combination vector by it's positon on complete combination set
  """
  def __init__(self):
    self.vector = None
    
  def GetCombVector(self,n,m,x):
    """  
    make a combination vector  
    parameters:    
    n, complete number    
    m, combination number    
    x, vector position in vector complete set  
    return:    
    a vector as list.
    Example: 
        >>> cv_calc=CombVectorCalc()  
        >>> cv_calc.GetCombVector(6,3,14)
        [1,3,4] 
    """ 
    if isinstance(n,int) and isinstance(m,int) and isinstance(x,int):
      if n <= 0 or m <= 0 or m > n or x <= 0 or x > comb(n,m):
        raise ValueError
      self.vector = []
      self._number_selection_recursion(n,m,x)
      return [y-1 for y in self.vector]
    raise TypeError
  
def _make_combination_number_list(self,n,m):
  """
  make a list fill by combination numbers like comb(n-1,m-1),comb(n-2,m-1),...,comb(m-1,m-1)
  parameters:
    n, complete number  
    m, combination number
  return:
    a list fill by combination numbers
  """
  ls = [0]
  start = 0
  for i in range(n-1,m-2,-1):
    start += int(comb(i,m-1))
    ls.append(start)
   return ls

def _number_selection_recursion(self,n,m,x):
  """
  calculate the number selection of dimension by using recursion algorithm
  parameters:
    n, complete number
    m, combination number
    x, vector position on the complete set
  return:
    ls, store dimension by a list
  """
  if m == 1:
    s = x
    if len(self.vector) > 0:
      s = self.vector[-1] + x
      self.vector.append(s)
      return self.vector
  comb_ls = self._make_combination_number_list(n,m)
  for i in range(len(comb_ls)):
    if x == comb_ls[i]:
      s = 0
      if len(self.vector) > 0:
        s = self.vector[-1]
        self.vector.append(s + i)
        m -= 1
      for j in range(m,0,-1):
        self.vector.append(n-j+1+s)
        return self.vector
    elif x < comb_ls[i]:
      s = i
      if len(self.vector) > 0:
        s = self.vector[-1] + i
        self.vector.append(s)
        break
  self._number_selection_recursion(n-i,m-1,x-comb_ls[i-1])
  return self.vector

class CombVectorSample():
  def __init__(self):
    

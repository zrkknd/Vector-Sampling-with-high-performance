import random as rd
from scipy.special import comb

def GetComb(n,m,x):
  """
  make a combination vector
  parameter:
  n, complete number
  m, combination number
  x, vector position in vector complete set
  return:
  a vector as list.
  """
  ls = Position_recursion(n,m,x,[]) 
  return [y-1 for y in ls]

import random as rd
from scipy.special import comb
"""
use function GetCombVector(n,m,x) to get a combination vector
"""
def make_combination_number_list(n,m):
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

def number_selection_recursion(n,m,x,ls):
  """
  calculate the number selection of dimension by using recursion algorithm
  parameters:
    n, complete number
    m, combination number
    x, vector position on the complete set
    ls, store dimension by a list
  return:
    ls, store dimension by a list
  """
  if m == 1:
    s = x
    if len(ls) > 0:
      s = ls[-1] + x
      ls.append(s)
      return ls
  elif m == 0 or m > n or x > comb(n,m):
    raise ValueError
  comb_ls = make_combination_number_list(n,m)
  for i in range(len(comb_ls)):
    if x == comb_ls[i]:
      s = 0
      if len(ls) > 0:
        s = ls[-1]
        ls.append(s + i)
        m -= 1
      for j in range(m,0,-1):
        ls.append(n-j+1+s)
        return ls
    elif x < comb_ls[i]:
      s = i
      if len(ls) > 0:
        s = ls[-1] + i
        ls.append(s)
        break
  ls = number_selection_recursion(n-i,m-1,x-comb_ls[i-1],ls)
  return ls
  
def GetCombVector(n,m,x):
  """
  make a combination vector
  parameters:
    n, complete number
    m, combination number
    x, vector position in vector complete set
  return:
    a vector as list.
  """
  ls = number_selection_recursion(n,m,x,[]) 
  return [y-1 for y in ls]

import random as rd
from scipy.special import comb
"""
use CombVectorSample.Sample_comb_vectors() to sample a group of vectors from combination vector complete set
use CombVectorCalc.Get_comb_vector() to calc a combination vector by using combination range number, combination selection number 
and vector's position on vector complete set
"""
	
class CombVectorCalc():
	"""
  	A Class to calculate a combination vector by it's positon on complete combination set
  	"""
  	def __init__(self):
    	self._vector = None
    
  	def Get_comb_vector(self,n,m,x):
    	"""  
    	make a combination vector  
    	parameters:    
			n, combination range number    
   	   		m, combination selection number    
      		x, vector position in vector complete set  
    	return:    
			a vector as list.
    	Example: 
        	>>> cv_calc=CombVectorCalc()  
        	>>> cv_calc.Get_comb_vector(6,3,14)
        	(1,3,4)
    	""" 
    	if isinstance(n,int) and isinstance(m,int) and isinstance(x,int):
      		if n <= 0 or m < 0 or m > n or x <= 0 or x > comb(n,m):
        		raise ValueError('input parameter error')
      		if m == 0:
        		return ()
      		self._vector = []
      		self._number_selection_recursion(n,m,x)
      		return tuple(y-1 for y in self._vector)
    	raise TypeError('input parameter error %s, %s, %s' % (type(n),type(m),type(x)))

	def _make_combination_number_list(self,n,m):
  		"""
  		make a list fill by combination numbers like comb(n-1,m-1),comb(n-2,m-1),...,comb(m-1,m-1)
  		parameters:
    		n, combination range number
    		m, combination selection number 
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
			n, combination range number
			m, combination selection number 
			x, vector position on the complete set
		return:
			self._vectors, store dimension by a list
		"""
		if m == 1:
			s = x
			if len(self._vector) > 0:
		  		s = self._vector[-1] + x
			self._vector.append(s)
			return self._vector
		comb_ls = self._make_combination_number_list(n,m)
		for i in range(len(comb_ls)):
			if x == comb_ls[i]:
		  		s = 0
		  		if len(self._vector) > 0:
					s = self._vector[-1]
		  		self._vector.append(s + i)
		  		m -= 1
		  		for j in range(m,0,-1):
					self._vector.append(n-j+1+s)
		  		return self._vector
			elif x < comb_ls[i]:
		  		s = i
		  		if len(self._vector) > 0:
					s = self._vector[-1] + i
		  		self._vector.append(s)
		  		break
		self._number_selection_recursion(n-i,m-1,x-comb_ls[i-1])
		return self._vector

class CombVectorSample():
	"""
	A class to sample a group combination vectors from complete combination vector set
	"""
	def __init__(self):
		self._naturals = None
		self._vectors = None

	def Sample_comb_vectors(self,n,m=1,count=1):
		"""
		A function to sample a group combination vectors
		parameters:
		  	n, combination range number
		  	m, combination selection number
		  	count, vector sampling count
		retrun:
		  	a group combination vectors by list
		"""
		if isinstance(n,int) and isinstance(m,int) and isinstance(count,int):
		  	if n <= 0 or m <= 0 or m > n or count <= 0 or count > comb(n,m):
				raise ValueError('input parameter error')
		  	self._sample_natural_from_combination_range(low=comb(n,m),size=count)
		  	cv_calc = CombVectorCalc()
		  	self._vectors = []
		  	for pos in self._naturals:
				self._vectors.append(cv_calc.Get_comb_vector(n,m,pos))
		  	return self._vectors
		raise TypeError('input parameter error %s, %s, %s' % (type(n),type(m),type(count)))

	def _sample_natural_from_combination_range(self,low,high=None,size=1):
		"""
		A function to sample natural number from given range 
		parameters:
		  	low, low bound of range. If parameter high equal to None, is is high bound of range.
		  	high, high bound of range, defoult is None
		  	size, number sampling count
		return:
			None.
		"""
		if high is None:
		  	a = 1
		  	b = low
		elif low < high:
		  	a = low
		  	b = high
		else:
		  	raise ValueError('input parameter error')  
		self.naturals = []
		while size > 0:
		  	t = rd.randint(a,b)
		  	if t not in self._naturals:
				self._naturals.append(t)
				size -= 1
			

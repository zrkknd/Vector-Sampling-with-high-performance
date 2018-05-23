# Vector-Sampling-with-high-performance
A different way to sample combination vectors. Fast and less memory using

As all Know, itertools.combinations() function is a Generator. It use to generate combination vector. 

Sometimes if you want use this function to sample some vectors from all combination complete set, you have to put the itertools.combinations() to list() function to make a complete set of all combination vectors. And then use random.sample() function to get the sample of vectors. 

But this way waste lots of times and huge memory space. Hence I find a different way to sample combination vectors. Sample vector position on complete set randomly, and use vector postion to calculate the number selection of every dimension of the vector. 

This way need using Combination Recursive Algorithm to calculate the number selection. It is shown below:

          Combination Recursive Algorithm: comb(m,n) = comb(m-1,n-1) + comb(m-2,n-1) + ... + comb(m-k,n-1) + ... + comb(n-1,n-1)
          
Step1, calculate the combination number Y using scipy.special.comb(m,n) function.

Step2, sample natural numbers from 1 to Y, get the sample number as the postion of combination vector of complete set.

Step3, using Combination Recursive Algorithm to calculate number selection(range from 0 to m) of every dimension of the vector(n dimensions).

Every recursive running can make sure number selection of 1 dimension. Hence we can sample a n dimension vector just run recursive n times, by using the postiion of this vector on complete set. 

It is fast and less memory using.

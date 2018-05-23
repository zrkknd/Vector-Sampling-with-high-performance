# Vector-Sampling-with-high-performance
A different way to sample combination vectors. Fast and less memory using

As all Know, itertools.combinations() function is a Generator. It use to generate combination vector. 

Sometimes if you want use this function to sample some vectors from all combination complete set, you have to put the itertools.combinations() to list() function to make a complete set of all combination vectors. And then use random.sample() function to get the sample of vectors. 

But this way waste lots of times and huge memory space. For solve this problem, I find a different way to sample combination vectors. The itertools.combinations() function generate vectors with orders. Hence we can use the position of vector on complete combination vector set to calculate the number selection of each dimention of vector. So we just need sample vector position on complete combination vector set randomly. It is fast and less memory need. 

This way need using Combination Recursive Algorithm to calculate the number selection. It is shown below:

          Combination Recursive Algorithm: comb(n,m) = comb(n-1,m-1) + comb(n-2,m-1) + ... + comb(n-k,m-1) + ... + comb(m-1,m-1)
          
Step1, calculate the combination number range using scipy.special.comb(n,m) function.

Step2, sample natural numbers from the range, get the sample number as the postion of combination vector on complete vector set.

Step3, using Combination Recursive Algorithm to calculate number selection(range from 0 to n-1) of every dimension of the vector(m dimensions).

Every recursive running can make sure number selection of 1 dimension. Hence we can sample a m dimension vector just run recursive m times. 

It is fast and less memory using.

### 11
Our proposed approach is based on the simple idea of embedding a low dimensional space into the high dimensional space. Instead of optimizing on the high dimensional space, we optimize over the lower dimensional space.

### 12
This idea leads to our algorithm which is very similar to BO.
The differences are:
First instead of optimizing over a high dimensional space X we, optimize over Y
which has to be sed.
We draw a random Gaussian matrix A which gives us the random embedding.
When evaluating the objective function, we do f(Ay) instead of f(x)
We update our prior based on <y, f(Ay)>

### 13
Let me illustrate the algorithm with a picture. 

Here the high dimensional space X is the square. instead of optimizing over it directly, we optimize over Y which is the red line. Y is mapped to AY which is the blue line. 

As we can see optimizing Y is the same as optimizing over the blue line AY.

And if 

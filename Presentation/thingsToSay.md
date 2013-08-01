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

Howevee, since the embedding is random, we have to  make sure that the optimizer is included in AY?

### 14
First, this result shows that if you are willing to make Y very big (As in choose Y as a really big box), with probability 1 we have the opimimum contained in Y. 
Of course, this is under the assumption that the effective dimensionality is low.

But this still does tell us how to set Y.

### 15
What the next thm tells us is that if the effective dimensionality is d_e, then optimizer in y guaranteed by thm 1 also has a reasonable norm with high probability.

Therefore to set Y we have have to ensure that the bounds contain vectors of reasonable norms.

Thus this gives us guidelines in how to set Y.

### 16


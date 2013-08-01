### 11
Our proposed approach is based on the simple idea of embedding a low dimensional space into the high dimensional space. Instead of optimizing on the high dimensional space, we optimize over the lower dimensional space.

### 12
This idea leads to a very simple algorithm which is very similar to BO.
The differences are:

First choose a compact set Y in a lower dimensional space.
Draw a random matrix A which gives us the random embedding.

We then do BO in Y while the objective function is changed from f(x) to g_A(y) = f(Ay).


### 13
Let me illustrate the algorithm with a picture. 

Here the high dimensional space X is the square. instead of optimizing over it directly, we optimize over Y which is the red line. Y is mapped to AY which is the blue line. 


Optimizing over Y is the same as optimizing over the blue line over X.

So if one of the 2 dimensions in the original space does not matter, then we can still locate the optimum with the blue line. 
Howevee, since the embedding is random, we have to  make sure that the optimizer is included in AY.
As we can see later we can ensure this with high probability by setting Y to be large enough.
This brings us to two theoretical results.
### 14
First, this result essentially shows that if you are willing to make Y very big (As in choose Y as a really big box), with probability 1 we have will the opimimum contained in Y. 
Of course, this is under the assumption that the effective dimensionality is low.

But this still does tell us how to set Y.

### 15
What the next thm tells us is that if the effective dimensionality is low, then optimizer in y guaranteed by thm 1 also has a reasonable norm with high probability.

Therefore to set Y we have have to ensure that the bounds contain vectors of reasonable norms.

Thus this gives us guidelines on how to set Y.

### 16




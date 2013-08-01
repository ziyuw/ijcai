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









## Comments
Talk about failing more.
The theorem is probablistic
You can choose another random embedding.

Gab & Frank: Theorems maybe too long. Try to find a different way of saying theorem 2.
Get rid of the assumptions.


- BO use black box (picture).
- Application slide. Big overview and the problem it solves.
- LPsolve has 50000 downloads in a year.
- Many of them discrete. It's common for problems to have free parameters. 
- tutorials from 2 days before mention those.
- BO picture slide. Bring in sequence. what is the objective function.
- Many acquisition function and well studied area.
- Theoretical results available.


- Thoeretical result for REMBO.
- Thoroughly.
- get rid of the curse slide (BO ususally work well in 5-10 dimensions and that's enough for a lot
of applications)
- Add axis names to slide 9.
- Move hypotheis testing to experiments.
- Cut the caption on random search.
- Contrast REMBO and BO.
- Minute longer on slide 14 and walk through.

- add probably 25D.
- If knew the dimension, we can do well. 
- All methods have the same function evalutions.
- Guess wrong can still lead of OK performance.
- Same number of function evaluations.
- provably show that 
- Getting rid of d=4 first and plot it twice.
- Add branin picture. 2d of branin (often used)
- lpsolve has 46 dimensions to be optimized.
- Get rid of references.
- Conclusion.		
- Bayesian optimization is up and coming
- But no high-dim
- Contribution.
- Add link to code and advertise it.






[Slide 16:]
First we evaluate our approach on Bayesian Neural Networks.
And we use cross-validation to construct the reward signal.
We divide the data into 8 sets, and train 8 BNNs each on 7 sets and test them on
the remaining set as in cross-validation.

The table presents results of this model on the robot arm dataset.
Many researcher has tried this problem before.
Specifically Radford Neal used BNNs and HMC on it.
We use the same code but adapted the sampled and were able to achieve better results.

This is my supervisor here and I manage to beat him by a bit.

[Slide 17:]
And again we use the same model on a different dataset.
This is one of the dataset from 
the NIPS 2003 feature selection challenge which is 6097 dimensional.
and again we achieved better performance by adapting the sampler.
And also by doing majority voting, we were able to beat another method
which uses a more complicated model.

[Slide 18:]
Also we compare our sampler on some other models. 
Here we adopt a more traditional MCMC diagnostics.

Here we compare our adapted HMC against NUTS and adapted RMHMC 
expert-tuned RMHMC.

NUTS is an modified HMC sampler that automatically sets L 
such that the trajectory in each proposal does not takes a u-turn.

[Slide 19:]
On the left we see that we have consistently better minimum ESS/L compared to NUTS across the datasets we tried.
On the right we see that for most of the dataset we match or outputperform the expert-tuned sampler.

[Slide 20:]
Next, we evaluate the different approaches on the Log Gaussian Cox Point process. 
This problem here is 4096 dimensional.
On the left we see that AHMC has higher ESS/L compared to NUTS.
And we have the same story on the right.

[Slide 21:]
Finally, we compare our models on the stochastic volitality model.
Again AHMC outperforms NUTS on Min Median and Max ESS/L measures.






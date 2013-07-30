---------- End of Review from Reviewer 1 ----------

------------- Review from Reviewer 2 -------------
Relevance                                     : 9
Originality                                   : 9
Significance                                  : 9
Technical quality                             : 9
Readability and organization                  : 10
Overall recommendation                        : 9
Confidence                                    : 8
Recommend for oral presentation               : 10
{CRITERIONNAME_09}: {CRITERIONVALUE_09}
{CRITERIONNAME_10}: {CRITERIONVALUE_10}

-- Comments to the author(s):
* SUMMARY:

  The paper suggests a technique for efficient Bayesian Optimization

  in very high dimensions (with low intrinsic dimensionality)

  utilizing a random embeddings technique.



* RELEVANCE:



  Bayesian Optimization is highly relevant and a current and

  interesting topic, fully appropriate to IJCAI.



* ORIGINALITY:

  The paper suggests an interesting novel idea for high-dimensional

  optimization. A simple, but effective idea, very interesting and

  original.



* SIGNIFICANCE:

  The work is very interesting and significant since it allows one to

  progress to optimization of extremely high-dimensional functions if

  there is some hidden intrinsic dimension. The nice property of the

  method is that it does not require an explicit reconstruction of

  these dimensions and so the problem remains tractable.



* TECHNICAL QUALITY:



  Very good study, including error bounds, and comparison with other

  relevant existing methods. Well developed, and stringently argued.



* READABILITY AND ORGANIZATION:



  The paper was a pleasure to read. Clear and transparently presented

  and well developed. Most of my comments are of minor nature.



  - Abstract:



    'integer linear' -> 'integer-linear' or 'integer/linear'



  - page 1:



    "number of evaluations ... increases exponentially" - with

    dimensionality?



    "sequential likelihood ratio tests, with a couple of tuning

    parameters, " - both commas can/should go.



  - page 3:



    "zero set of a polynomial" - you probably want to say of a

    "nontrivial polynomial"



    "Theorem 2 says that given any..." - here I have a question: how

    important is the condition of the mapping? Can we safely assume

    that the matrices Phi are well-conditioned and thus the existence

    of y is a well-posed problem?



    Furthermore, how important is it for your idea of the random

    embedding that it be used for Bayesian Optimization? Could it be

    combined with other methods?



    In the proof for Theorem 3, you talk about x_perp twice, once in

    line 2, and once in line 6 of the proof. Are these the same?



    You mention proposition 1 which does not exist.



  - page 4:



    "In all our experiments we set Y to be [-sqrt d,+sqrt d]^d".

    Where did epsilon disappear to?



    "low dimensional" -> "low-dimensional"



  - page 5:



    In Table 1, is a high value good or bad? Say it.



    "using k=4 interleaved runs is only 0.26^4 ~ 0.005" - where can we

    find this in the figures?



    "looses" -> "loses". At some point, probably this misspelling of 

    "lose" will officially be accepted to be considered correct, but

    until that happens, I will continue to ask for the

    orthographically correct version.


-- Summary:
Very enjoyable read - interesting idea, simple and elegant, and very well explained and developed. Impressive results (10^9-dimensional space!). Makes one want to go and implement it right away.
---------- End of Review from Reviewer 2 ----------

------------- Review from Reviewer 3 -------------
Relevance                                     : 8
Originality                                   : 9
Significance                                  : 9
Technical quality                             : 7
Readability and organization                  : 9
Overall recommendation                        : 8
Confidence                                    : 8
Recommend for oral presentation               : 1
{CRITERIONNAME_09}: {CRITERIONVALUE_09}
{CRITERIONNAME_10}: {CRITERIONVALUE_10}

-- Comments to the author(s):
SUMMARY:

This paper presents a new idea to apply random embedding through to the problem of Bayesian optimization in high dimensional spaces where the "actual" problem is known to be low dimensional. It is the second paper in the field to achieve Bayesian optimization in high dimensional spaces. However, the kind of problems where it can be applied are different.



RELEVANCE:

This paper provides a novel contribution to the intersection of Bayesian optimization and dimensionality reduction, both in the theoretical and applied point of view. Thus, the contribution is clear.



ORIGINALITY:

This paper combines the random embedding from [Bergstran and Bengio 2012] with a classical Bayesian optimization setup. However, this combination provides new opportunities for Bayesian optimization in high dimensions. There is only a recent paper [Chen 2012] that addressed this problem. However, the setup is completely different. For instance, as far as I know, [Chen 2012] is able to automatically determine the number of effective dimensions in a single run. However, as pointed out in this paper, it requires those dimensions to be aligned with the ARD kernel. Furthermore, ARD kernels are able to find dimension which are uncorrelated (noise), not only those that are constant. In contrast, REMBO can find any embedding in the high dimensional space. However, the number of effective dimension must be known in advance (or a close upper bound) and it might require several runs for the embedding to include the optimal value.



SIGNIFICANCE:

As stated before, the idea of Bayesian optimization in high dimensional spaces is new. This paper provides interesting insights in the area. However, it should consider including [Chen 2012] in the experimental comparisons.



TECHNICAL QUALITY:

The paper provides both theoretical and experimental results to support the quality of the work. Nevertheless, there are a couple of important issues that are not fully explained:



-One of the critical issues in Bayesian optimization is the exploration-exploitation trade-off. This has been more or less solved by selecting criteria such as the Expected Improvement or UCB, and it is what makes an algorithm excel over the rest. However, REMBO has 2 parameters that need to be explored, that is, the effective number of dimensions and the number of runs. From the present work, it is not clear how, at a certain point, is better to span a new run or to keep exploiting the current one. Also, if the number of effective dimensions is completely unknown, it is not clear how to select "d" and when it should be increased or reduced.



-In any Bayesian optimization, there is the assumption of smoothness (up to a certain level, depending on the kernel) of the underlying function. However, is it still preserved when using the projection operator?



-Are the results in Figure 4 statistically significant? Considering that the plots only capture 1/4*std it seems that some of the algorithms (including REMBO) can do surprisingly good and surprisingly bad.



READABILITY AND ORGANIZATION:

The paper is in general clearly written with enough references to the state of the art. As an opinion, since the selection of the kernel is related to each of the experiment, it could clarify the reading if it is moved to section 4.



Figure 4 is labeled in the text as Figure 4.2
-- Summary:
This paper provides a novel and interesting contribution in the field of Bayesian optimization. However, there are some technical details that are not completely clarified and it is unclear the significance of some of the results.
---------- End of Review from Reviewer 3 ----------

////////////////////////////////////////////////////
Powered by ConfMaster.net
///////////////////////////////////////////////////

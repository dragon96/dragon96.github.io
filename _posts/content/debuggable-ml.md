

This post serves as a review of some of the papers selected for the [Debugging Machine Learning Models](https://debug-ml-iclr2019.github.io/)
workshop at ICML 2019, in addition to some of my own thoughts. My goal is to better understand some of the questions that researchers
ask and how they tackle them, and to highlight some of the more interesting questions that have come out of this.

*TODO*: read the last 6 papers and include them in here.


#### Poisoning attacks

I thought this was one of the more interesting ideas to come out of reading. 

#### Can we detect dataset distributional shifts?

The premise of 

#### How does pruning affect interpretability?

 - Bau


#### What features of a given input contribute to a classifier’s decision?

There were two papers that explored this question. 

Consider two adjacent layers $K \to L$ of a trained neural network. Given that some subset $L^\prime \subseteq L$ of neurons activitated with some value,
can we trace that back to a subset $K^\prime \subseteq K$ responsible for that activation? For example, this question is relevant when $L$ is the
final layer of a neural network responsible for binary classification, as $L$ has two neurons and answers "What parts of the input are responsible for
this classification decision?" We could treat this as a gadget; if we could conceive of $K^\prime$, we could re-iterate on the ancestor layer of $K$,
until we reach the input layer.

I particularly like this approach because (1) it is a composable and well-contained problem (2) it meshes with the model of a trained neural network
as a distributed representation of its training data. 

MAGIX proposes another approach to this 

What are some broader ways we can think about attributing features of an input to a model’s decision? Both local sensitivity analysis and MAGIX
implicitly assume that the ambient input space offers For example, local sensitivity analysis assigns a real number to each pixel of the input image
as an indication of the weight that each pixel contributes in the model’s decision. While this is a fine way to gather intuition about *where* the neural network
"looks", it fails to capture some of the structure of the image that informs this decision. In the shark image, the classification is likely not
based on each independent pixel’s value, but the edge formed by the pixels collectively. Thus, the layers that are most explanatory of this decision are
in the hidden layers. Can we quantify at what layer a decision is most explanatory? Can we retrain models to better capture the innate structure of our data?

The MAGIX paper uses recidivism data to support its analysis. Here, an interpretation is defined on decision values, and some subset of input feature values.
For example, MAGIX generates the rule $\text{race=white and alcoholic=no}$ to explain why a person is considered $\text{low-risk}$. For an inexplicable reason,
this generated condition doesn’t explain much to me; we would have discovered the same dominant rule about the training data used to train the model by
training a decision tree directly. Or rather, idk, this captures 90% of how the model makes decisions, but it doesnˇt explain how it makes the decision.

Leads me to think that for more interpretable models to exist, models will need to be trained in a more inherently interpretable manner. A convolution is
a good example of such gadget; it captures the "locality" of our image data.

#### What images can’t a generator generate?

Consider a generator $G: \mathcal{Z} \to \mathcal{X}$ (in the GAN sense), where $\mathcal{X}$ and $\mathcal{Z}$ are input and latent sizes respectively.
We want to understand the range of $G$ (i.e. the possible images it can and cannot generate).
The primary claim is that if we can train an inverter $E: \mathcal{X} \to \mathcal{Z}$
to satisfy $E(G(z))=z$, then we know that $G(E(x)) = x$ only if $x$ is in the support of $G$.

Inverting an entire neural network is often an intractable problem, so we can consider a more tractable version of the problem training
another inverter $E_F$ only on the final layers $G_F$ of $G$. Then $G(E(x)) = x$ only if $G_F(E_F(x)) = x$, so we can identify some images that
are not in the range of $G$.

This is an interesting line of inquiry, but I don’t know if the claim that $E(G(z)) = z$ implies $G(E(x)) = x$ is reasonable. 
For example, this is false if $\mathcal{X} = \mathbb{R}^n$ and $\mathcal{Z} = \mathbb{R}^m$ with $n > m$.
However, this false equivalence may not end up mattering in practice.

#### Understanding the inner workings of a classifier

Given 
 - Visualizing with slices
 - Local sensitivity 



# Open questions and concluding thoughts

- Unrelated ideas
 * Consideration of what a "real" input is.
 * Not a big fan of fairness approaches.


#### Markdown Tips

Quick tips: 
links:    [link_text](url)
eqn:      $x$ for inline, $$x$$ for centered
red:      <div class="red">text</div>

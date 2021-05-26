<!--
Quick tips: 
images:   ![alt_text](/assets/image_name.png){:.center-image}
links:    [link_text](url)
eqn:      $x$ for inline, $$x$$ for centered
red:      <div class="red">text</div>
-->


## Readings

* [(Maclean 2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4728354/). I found this paper frustratingly poorly written, even though it contained some good ideas. The premise considers possible dynamical models of how different populations of cells can inhibit or promote the growth of other cells -- in particular, stem, progenitor, and differentiated cells. For example, it considers four schematics below.

![](/assets/maclean_2015.jpg){:.center-image}

One insight is that there is a way to define a probability for each stable fixed point; see [(Kirk 2015)](https://arxiv.org/pdf/1505.02920.pdf). The paper fails to define precisely what an inhibition arrow represents, and what the different experimental conditions (true, independent, and iid conditions) mean. Their motivation for considering these four examples is also unclear.

Nevertheless, this brings up some interesting questions to think about further:
   * The authors come from a population biology angle, which I know very little about.Their introduction contains some interesting references.
   * Is there a way to reason about dynamical differences of the four schematics proposed above?
   * Authors explore fixed point probability as a function on distribution of initial conditions. Is there a "maximum entropy" intitial distribution that makes sense?
   * The authors entertain a question of whether model complexity yields higher or lower stability. [(May 1972)](https://sci-hub.tw/https://doi.org/10.1038/238413a0) Is this the right question?
   * The proposed model does not take cell locality into account; I don’t know to what extent cells only signal to their neighboring cells, although I think spatial effects could be an interesting extension.

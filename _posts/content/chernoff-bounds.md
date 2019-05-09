Markov’s inequality states that for a nonnegative-valued random variable $X$, we have $Pr(X\ge a) \le \frac{\mathbb{E}[X]}{a}$ for all $a$. This is a pretty dumb inequality if $a < \mathbb{E}[X]$, but otherwise it tells a story about how the tail (when $(X > a)$) cannot be too heavy or else its expected value would need to be shifted higher.

The Chernoff bound exponentiates everything. For all $t$:

$$ Pr(X \ge a) = Pr ( e^{Xt} \ge e^{at} ) \le \frac{\mathbb{E}[e^{Xt}]}{e^{at}}$$

And when $X = \sum X_i$, where $X_i$ are mutually independent random variables, we can split the right-hand side further:

$$ Pr(X \ge a) \le e^{-at} \mathbb{E}\left[\prod e^{tX_i}\right] = e^{-at}\prod \mathbb{E}[e^{tX_i}] $$

In general, the product of random variables cannot be moved outside an expected value like this; this is only valid when the variables are independent. For some intuition about how the expected value of a product differs from the product of the expected value of random variables, let’s look at the case with two random variables $A$ and $B$. 

The quantity $\mathbb{E}[AB]-\mathbb{E}[A]\mathbb{E}[B]$ is the covariance of $A$ and $B$. Let $D$ be a discrete random variable that is $+1$ or $-1$ with $1/2$ probability each. When $A$ and $B$ both take the value of $D$ (perfectly correlated), then $\text{cov}(A,B) = \text{var}(D) = 1$. When $A$ takes the value of $D$ and $B$ takes the value of $-D$, then $\text{cov}(A,B) = -1$. And when $A$ and $B$ take on independently drawn events from $D$’s distribution, then we have $\text{cov}(A,B) = 0$.

So if the Chernoff bound is just a Markov bound, what makes it so much stronger? Suppose that $X_i$ is a real number uniformly and independently drawn from $[0,1]$ for each $i=1, \cdots, n$, and $X = \sum X_i$. Then from Markov’s inequality, 

$$ Pr(X \ge kn) \le \frac{\boxed{n}\cdot\tfrac12}{k\boxed{n}} = \frac12\cdot \frac1{k}.$$

And from the Chernoff bound using $\mathbb{E}[e^{tX_i}] = \int_0^1 e^{tx} dx = e^t-1$, we have:

$$Pr(X \ge kn) \le e^{-tkn}\left(\mathbb{E}[e^{tX_i}]\right)^n= \left(\frac{e^t-1}{e^{tk}}\right)^{\boxed{n}} $$

When we track what happens to the $n$, exponentiating actually enables us to amplify a probability instead of having it cancel out in Markov’s inequality. There isn’t anything special about the exponential. As long as we pick any nonnegative increasing function, we can actually do the same trick. For example, we could choose $x^2$:

$$Pr(X>kn) \le \frac{\mathbb{E}[X^2]}{(kn)^2} = \frac{n\cdot (1/3)}{k^2n^2} = \frac13\cdot \frac1{k^2n}$$

Or generalizing to an arbitrary polynomial $x^d$:

$$Pr(X>kn) \le \frac{\mathbb{E}[X^d]}{(kn)^d} = \frac1{d+1}\cdot \frac1{k^dn^{d-1}}$$

As $d$ increases, this bound asymptotically tightens as a function of $n$. The reason we don’t have names for these inequalities is that the Chernoff bound will always be asymptotically tighter than any of these polynomial transformations to Markov’s inequality.

**Exercise**: The Chernoff bound will always give a stronger bound *asymptotically*, but not necessarily numerically. Using the same example, can the Chernoff bound ever be weaker than the Markov bound? (If $t=1$, any $\frac12 < k < \ln(e-1) \approx 0.54$ will mean that the Markov bound is stronger, but what about when $t$ is chosen optimally?)

You might wonder what happens if we choose a function that is concave on $[0,1]$. Naturally, I would try $\ln(x)$, but you have to be careful:

$$Pr(X>kn) \le \frac{\mathbb{E}[\ln(X)]}{\ln(kn)} = -\infty$$

This is invalid because $\ln(X)$ is not nonnegative on its domain, violating the Markov inequality assumption. If we instead choose $\sqrt{x}$, we get:

$$Pr(X>kn) \le \frac23\cdot \frac{\sqrt n}{\sqrt k}$$

So we do get a bound for concave functions too, but it’s just not useful. For large $n$, the RHS will grow with $n$, while the RHS of vanilla Markov’s inequality $1/2k$ is constant, so in essence, we’ve just *weakened* our inequality.

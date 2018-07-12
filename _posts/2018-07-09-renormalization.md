---
layout: post
title: Renormalization Group in Iterated Maps
date: 2018-07-09
categories: raw
---

 * Primarily followed these notes: [Introduction to universality and renormalization
group techniques](https://arxiv.org/pdf/1210.2262.pdf).
 * Secondarily: [Universality in transitions to
chaos](http://www.cns.gatech.edu/PHYS-4267/UFO.pdf), for understanding universality a little better.
 * Third: [The Topology of Chaos: Alice in Stretch and Squeezeland (Chapter 2)](http://csc.ucdavis.edu/~chaos/courses/ncaso/Readings/ch2.pdf)

## Summary

 * Definition of a Lyapunov exponent. 
   * "For one dimensional maps, it can be shown that Lyapunov exponents are independent of the initial condition $x_0$, except perhaps for a set of measure zero."
 * Period doubling behavior of logistic map $\mu x(1-x)$. Qualitative behavior depends on $\mu$. Convergent behavior for $x<3$, chaotic behavior for $x \approx 3.7$ or higher.
 * Notion of a superstable cycle, although significance is not clear.
 * The universal equation: $g(x) = \alpha g(g(-x/\alpha))$, with $g(0) = 1$ WLOG and $g(1) = -1/\alpha$.
 * Broad intuition about what the renormalization group is.
 * Chaos is defined as satisfying: for any $J\subset I$, there exists an $N$ such that for all $n>N$, $f^n(J) = I$. This implies the following properties:
   * Sensitivity to initial conditions. More precisely, there exists a $\delta$ for which for all $x$, $J\ni x$, $y\in J$, there is an $N$ such that $\mid f^N(x)-f^N(y)\mid>\delta$.
   * Existence of dense orbits: In English, this means, that iterated application of $f$ on $x$ can become arbitrarily close to any $y$. Or: For any $A,B\subset I$, there is an $N$ such that $f^N(A) \cap B \neq \varnothing$.
   * Has a set of unstable periodic points that is dense in its domain.
 * The third set of notes elegantly answers exercise 2.6 in the first set of notes, showing that tent maps yield chaotic behavior, by using binary coding!

## Questions

 * Given an iterated map $f^{2^n}(x)$, how do we know that the $2^n$ fixed points necessarily follow a single cycle? In other words, disprove: There exists an $x$ such that $f^{2^k}(x) = x$ for some $k <  n$.
 * What are the shaded parts in this diagram after $\mu_{\infty}$:

 ![Bifurcations of Logistic Map](/assets/renorm_bifurc.png){:.center-image}

 * What does "universality" mean in the context of a real life system? The notes cite that $\delta \approx 4.6692$ is "universal" in this mathematical context, but how does this apply to a fluid system?

 * Let $f_\mu$ be a function with fixed points $r_1, \cdots, r_{n}$. Let $g_\mu = f_\mu(f_\mu(x))$ have stable points $r_1,\cdots, r_{2n}$. Prove or disprove: if $\left(\frac12 (f_\mu^\prime)^2\right)_ {\mu} > 0$, then $\left(\frac12(g_\mu^\prime)^2\right)_ \mu > 0$ for $x=r_i$, where $i=1,2,\cdots, 2n$. (This will formally show that the function has period doubling bifurcations forever, and that the fixed points of $f$ will become unstable fixed points of $g$.)

 * I have still yet to understand the precise conditions in which period doubling occurs. The notes claim that $f$ as a differentiable, unimodal function with a quadratic tip is sufficient, but this doesn't seem necessary.

 * For the chaos generated from iterated application of the tent map, it is shown that the number of fixed points $N(p) \approx N_f(p)/p = 2^p/p$, where $N_f(p)$ is the total number of fixed points of $f^p$. (Note: Use $\sum_{q|p} q N(q) = N_f(p)$ to compute values for primes and powers of $2$.) The growth rate $h_P\lim_{p\to\infty} \frac1p \ln N(p) = \ln2$, which happens to be the Lyapunov exponent. Is this a coincidence? $h_P$ is also asserted to be the topological entropy. What is that?

## Extra Links

 * [How I found these notes](https://calculatedcontent.com/2015/04/01/why-deep-learning-works-ii-the-renormalization-group/)
 * [Some exercises to help with Lyapunov exponents and superstability](https://www.math.ucdavis.edu/~romik/teaching-pages/mat119b/119b-hw7-solutions.pdf)
 * [Same as above](https://www.math.ubc.ca/~andrewr/620341/assignments/assignment2_solutions.pdf)
 * [Understanding the tent-map exercise](http://oldwww.ma.man.ac.uk/~pag/dynsyst/2-itineraries.pdf) Show that iterated application of the tent map does not lead to period doubling behavior, and that it transitions directly into chaos.
 * [Connecting period-doubling cascades to chaos](https://arxiv.org/pdf/1002.3363.pdf) Paper by Yorke to possibly answer the second question above.

<!-- 
 Raw Notes:

 (Page 12): The last two paragraphs on the page confuse me. Also why is mu < 4 (Answer: To make sure that f: [0,1] -> [0,1]
If there are four fixed points of f^4(x), how do we know that they appear in a 4 cycle? Is it just topologically impossible to be two 2-cycles?
Also, why is this 4-cycle attractive? Why not repulsive?
What's all of the shady stuff on the bifurcation diagram after ~3.55ish?
(Remember, the y-axis shows the values of the fixed points)
What are all of the pseudo-lines in the >3.6 area?
Still need to understand what the Lyapunov exponent actually is. I think I'm misunderstanding it. (Do the exercises)
Verify Figure 6.
Exercise 2.1 answers my question about why there's only "one" Lyapunov exponent for the most part. If two functions are pieced together unnaturally, then of course not, but because the Lyapunov exponent ends up being the sum of log(f'(x_n)), and x_n -> stable points. What if there are two stable points naturally, like -x(x-1)(x+2)? (Only holds for the same neighborhood)
Wait how is a Lyapunov exponent defined for a cycle/periodic behavior?

Not clear why superstable orbits ~ when Figure 6 goes to -infty. Namely, show that gamma(mu) = -infty iff (F^n)'(x)=0

Universality
-------------

Would really like to understand the story of how universality of delta applies to turbulence or something real

[Meta: I like the writing style of this. It shows the cool parts, and then talks about the assumptions made ("we are not going to talk about how regular it needs to be"). Math textbooks often present in the other order.]

2.5: Why don't we have maps with 2^n periodic points decompose into two separate cycles? (Probably some kind of topological/algebraic argument)
2.6: Found this: http://csc.ucdavis.edu/~chaos/courses/ncaso/Readings/ch2.pdf

RG Introduction
------------------
When are the conditions 3.4 true? What are the assumptions being made?
	What if the function isn't even?
	Unpack the quadratic tip assumption
	Why is a<b needed?
Why is function space U an infinite dimensional space?
Shouldn't it be mapping 2^{n-1} to 2^{n} periods?
	No: Consider the fixed points x1 ... x_{2^n}. Then f(f(x_i)) = x_{i+2}, so the period is 2^{n-1}
Exercise: try mapping the logistic map and plotting it to see what happens
Still lacking a bit of intuition about superstable maps: Why do we care about these specifically?

May be worth looking at Feigenbaum's original work. [18] was recommended. -->




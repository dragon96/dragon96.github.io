---
layout: post
title: Notes on Random Generation and Counting
date: 2019-04-18
---

## Outline

Examples:
	Generating a random partition
	Generating a random tree with a certain degree distribution
	DNF circuits

Definitions:
	Uniform generator

Caveats:

What kind of computation machine do we have? Either a probabilitistic TM or a OCM.
	What if you have a denominator that's not a power of 2?
	How do the powers of these two machines differ?
		Sufficient condition: If there is a polynomial time function N(x) that integrates all answers. 



### Oracle Coin Machines

Consider the two probabilistic computation paradigms:
 * A **probabilistic Turing machine** (PTM) is a Turing machine equipped with a fair coin; each decision can be made on a random bit generator.
 * An **oracle coin machine** (OCM) is a Turing machine that on each decision, can flip a coin with any rational probability $p/q$. Implementation-wise, such machine would have a separate tape, where $p$ and $q$ are written.

You might ask, how would a PTM simulate a 3-sided coin, or how would an OCM simulate an event with probability $1/\sqrt2$. Wouldn't both machines never terminate? We can allow both machines to fail with bounded probability, upon which it terminates with output $\mathbf{?}$. We also need to allow the output distribution to deviate from our desired distribution by some specified amount called the *tolerance*. 

**Exercise**: It's clear that anything a PTM can compute, the OCM can do with comparable complexity, but are there problems that an OCM can compute in polynomial-time that a PTM cannot?

**Lemma**: Suppose we have a polynomial-time bounded OCM $M: \mathcal{X} \to \mathcal{Y}$. If there exists a polynomial-time computable function $N: \mathcal{X}\to\mathcal{Y}$ such that $P(M(x)=y)\cdot N(x)\in \mathbb{Z}$ for all input-output pairs $(x,y)$ with $y\neq \mathbf{?}$, then there exists a PTM $M^\prime$ that *efficiently simulates* $M$, meaning that:

 * ("Efficiently") The runtime of $M^\prime$ is at most some polynomial $p_1(x)$ times of the runtime of $M$.
 * ("Simulates") For all input-output pairs $(x,y)$ with $y\neq \mathbf{?}$, there is some polynomial $p_2(x)$ such that $Pr(M(x)=y) \le p_2(x)\cdot Pr(M^\prime(x)=y)$.

*Comment*: I'm not fan of the author's "Simulates" part of the definition. First, using a polynomial $p_2$ to bound the acceptance probability is very weak. Second, I find that the one-sided criterion is a bit unintuitive to think about. The important part of this awkward definition is that $p_2(\cdot)$ is only a function on the input string, not the output string.

(Why a polynomial time bound is weak?) 



## References

Sinclair
	Atrocious notation

## Maybe?

Generating the factorization of a random number.
	Maybe this should be a separate post.
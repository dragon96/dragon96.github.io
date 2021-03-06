---
layout: post
title: "Concentration Inequalities"
date: 2018-12-02
is_draft: True
---

Concentration inequalities are primarily used to answer the question: "Given a random variable $X$, how often are we allowed to see tail behavior?" Tail behavior refers to samples of $X$ that violate its statistics. For example, if your commute has a mean travel time of 50 minutes and standard deviation of 10 minutes, you might occasionally have commute times of 80 minutes. But you should be suspicious if you observed these travel times too frequently. We'll formalize this intuition that rare events can't occur too frequently.

#### Markov's Inequality

We'll frame this as a challenge-response game on a real-valued random variable $X$ between Adam and his mischievous younger sister Eve. Adam chooses some restrictions on $X$. A real value $a$ is then announced, and Eve gets to pick a distribution for $X$, scoring $P(X>a)$ points. Adam is a benevolent older brother and doesn't want to set too many rules, but he also wants to upper bound the frequency of Eve's mischief, $P(X>a)$, beyond his tolerance threshold $a$. 

<div class="red">
	Could be funny: an image of Calvin's mom, trying to "tame" Calvin.
</div>

Let's try constructing inequalities, starting with as few assumptions about $X$ as possible. 

**Scenario 1**: If Adam doesn't restrict $X$'s behavior, what can he say about Eve's behavior?

Nothing! $X$ can be any distribution, so this means that for any $a$, Eve can assign probability mass only to values of $x>a$. 

**Scenario 2**: Adam enforces that $\mathbb{E}[X] = \mu$. What can he say about Eve's behavior?

Almost nothing! Just because Adam fixes the center of the distribution doesn't prevent Eve from forcing $X$ to be arbitrarily far from $\mu$. For example, if $\mu=0$, for any $x>a$, Eve can assign $P(X = x) = P(X = -x)$, causing $P(X>a) = 0.5$. The trick here is that Eve can balance out arbitrarily large values of $x$ with arbitrarily small values $-x$ to satisfy Adam's expectation constraint. 

To thwart this, Adam only needs to restrict Eve's ability to assign probability to arbitrarily small values.

**Exercise**: Eve can score $0.5$ points, independent of $a$, but she can do better. How can she score $1-\epsilon$ points, for any $\epsilon > 0$? Can Eve score $1$ point?

**Scenario 3**: Adam requires $\mathbb{E}[X] = \mu$ and $X \ge 0$. How does Eve maximize $P(X>a)$?

<div class="red">
	Poorly written below. WTF is a spending budget? Diagram desperately needed.
</div>

Like in the previous scenario, whenever mass is assigned to some $x > \mu$, Eve must balance it by assigning mass to some $x^\prime < \mu$ in order to satisfy the expectation condition. Intuitively, this can be visualized as balancing a unit mass of oranges on a see-saw, with its fulcrum at $X=\mu$. On the left side ($x^\prime < \mu$), Eve puts as many oranges as far from the fulcrum as possible, to maximize how much she can place on the right side. On the right side ($x > \mu$), Eve places oranges just right of the $X=a$ marker, so that she can maximize the *number* of oranges with $X\ge a$.

<div class="red">
	Diagram of seesaw intuition; rewrite the below 
</div>

If she assigns $1-p$ proportion of her total mass to values of $x^\prime$, her budget $B \le (1-p)\cdot (\mu-0)$. Given this budget $B$ and $p$ leftover mass, she maximizes $P(X>a)$ by assigning all $x = a+\epsilon$. Thus, her total expenses over $\mu$ are $E > p\cdot (a-\mu)$. Thus, we must have:

$$ p(a-\mu) < E \le B \le (1-p)\mu \Rightarrow p < \mu/a $$

**Theorem** (Markov's Inequality): Let $X$ be a nonnegative random variable and $a > 0$. Then $P(X < a) < \frac{\mathbb{E}[X]}{a}$.

This is great for Adam! The maximum amount of mischief Eve can create varies inversely with $a$. 

<div class="red">
Commentary about a = E[X] and how this is only about tail behavior. If X isn't greater than 0, then shift it. Exercise: What if Eve is going in blind about a, and wants to cause as much mischief given some distribution that a is drawn from?

Thinking about mean as a budget.
</div>


#### Chebyshev's Inequality

In the previous scenarios, a common theme is that Eve can get pretty far just by putting mass at extrema, relative to $\mathbb{E}[X]$. Now we'll consider a regime in which Adam also fixes the spread of $X$.

<!--So far, we've only played with assumptions about $\mathbb{E}[X]$. Now, we will consider a different angle, in which we have information about the spread of $X$. Formally, this means that $\text{Var}(X) = \mathbb{E}[(X-\mathbb{E}[X])^2]$.  
(Note to self: this definition of Variance is what we were looking at for budget in Markov's inequality.)-->

Formally, Adam fixes the mean $\mu$ and variance $\sigma^2$ of $X$. A $k>0$ is announced, and Eve wants to maximize $P\left(\frac{\mid X-\mu\mid}{\sigma} > k\right)$. 

**Exercise**: The purpose of reformulating the game is to capture the more natural question of "How much mass can be more than $k$ standard deviations away from the mean?" rather than "How much mass can be more than an arbitrary fixed value?" Show that the original game, in which Eve tries to maximize $P(X>a)$, can be reduced to new objective of maximizing $P\left(\frac{\mid X-\mu\mid }{\sigma} \ge k\right)$.

**Scenario 4.0**: Adam requires $\mathbb{E}[X] = \mu$ and $\text{Var}(X) = \sigma^2$. How does Eve maximize $P\left(\frac{\mid X-\mu\mid }{\sigma} \ge k\right)$?

This problem is harder because Eve must simultaneously satisfy two statistics. One insight is that the mean requirement is actually a distraction! Consider the alternative game:

**Scenario 4.1**: Adam requires $\text{Var}(X) = \sigma^2$. How does Eve maximize $P\left(\frac{\mid X-\mu\mid }{\sigma} \ge k\right)$?

Consider any probability distribution with variance $\sigma^2$. Eve redistributes probability masses in a way that keeps the variance fixed. You can visualize this as moving only two probability masses at a time. Unfortunately, $\mu$ can shift while she does this, making the target $P\left(\frac{\mid X-\mu\mid }{\sigma} \ge k\right)$ hard to track. Thus, it's convenient for Eve to fix $\mathbb{E}[X]$ (let's say, at $0$), and separately figure out how to satisfy the variance condition.

<div class="red">
	May be helpful to make diagram illustrating the technique of moving two masses at a time.
</div>

As in Scenario 2, Eve wants probability masses as far from $\mu$ as possible. Unfortunately, a probability distribution with $\mid x\mid  > k\sigma$ whenever $P(X=x) > 0$ would yield $\text{Var}(X) \ge k^2 \sigma^2$ (Why?). Thus, Eve needs to distribute $1-p$ total mass at values $\mid x\mid  < k\sigma$ and the remaining $p$ mass at $\mid x\mid  \ge k\sigma$ values. Eve wants to maximize $p$, so she should locally minimize variance where possible to marginally increase $p$.

For the "inner" masses with $\mid x\mid  < k\sigma$, their exact $x$-value doesn't affect how many points Eve scores, so she should minimize whatever variance comes from inner masses.

**Exercise**: Prove that inner masses should all have $x=0$ to minimize variance.

For the "outer" masses with $\mid x\mid  \ge k\sigma$, their exact values won't affect Eve's score, which is fixed at $p$. Thus, for the sake of minimizing variance while fixing the mean, she should have $P(X=-k) = P(X=k) = \frac p2$.

**Exercise**: Prove that outer masses should satisfy $P(X=-k\sigma) = P(X=k\sigma) = \frac p2$.

Thus, the total variance is $$\sigma^2 = (1-p)\mathbb{E}[(X_{\text{inner}}-\mu)^2] + p\cdot\mathbb{E}[(X_{\text{outer}} - \mu)^2] \ge p\cdot k^2\sigma^2,$$ or $P(\mid X\mid  \ge k\sigma) \le \frac1{k^2}$.

<div class="red">
	diagram
</div>

**Theorem (Chebyshev's Inequality)**: Let $X$ be a random variable with $\text{Var}(X) = \sigma^2$. Then $P\left(\frac{\mid X-\mathbb{E}[X]\mid }{\sigma} \ge k\right) \le \frac1{k^2}$.

You may notice that the way we built Eve's strategy for Chebyshev's inequality is similar to what we did for Markov's inequality. We have some "point" oranges (the "outer" masses) that actually help her maximize her objective, but need some "budget" oranges (the "inner" masses) to balance out the high variance from her "point" oranges. The textbook proof of Chebyshev's is actually a direct application of Markov's inequality.










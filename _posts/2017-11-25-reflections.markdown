---
layout: post
date: 2017-11-25
title: "Reflections 11/25/17"
categories: daily reflections
---

# What did I learn today?

In Strogatz Chapter 4, we modeled oscillatory behavior by considering systems that are $2\pi$-periodic. Instead of plotting behavior on a plane, we considered behavior on a circle. The way to motivate simple behavior on a circle is to first consider two systems: $\dot\theta = k$ and $\dot\theta = A\sin\omega$. The first system is a jogger with uniform speed, and the second models a pendulum.

We can start to model a more complex system with bifurcating properties by combining these two: $\dot\theta = k - A\sin\omega$. When $A < k$, then the right hand side is always positive, so there are no fixed points. But when $A > k$, we have symmetric fixed points about a certain axis. This was paired nicely with a firefly synchronization example. The naive firefly tries to match other blinking stimuli, but has a fixed blinking frequency that cannot actually change. Instead, the firefly can offset its usual blinking frequency by manually adding an offset based on the other stimulus. If the other blinking stimulus is too fast though ($A < k$), then the firefly enters phase drift and never synchronizes with the stimulus.

I finally decided to finish up Abbott Chapter 5 also, after several weeks (months?) of not touching the analysis book. To recap the differentiation chapter, Darboux's theorem states that derivatives must satisfy the intermediate value property: If $f$ is a function that is differentiable on an interval $[a,b]$ and if $f'(a) < \alpha < f'(b)$, then there's an $x\in (a,b)$ such that $f'(x) = \alpha$. This was surprisingly not equivalent to the statement that all derivatives are continuous. For example, consider $f(x) = x^2\sin\left(\frac1x\right)$.

There was also a lot of detail about how the Mean Value Theorem is the basis of many results about differentiability. It states that if $f$ is differentiable on an interval $(a,b)$, then there must be some $x\in(a,b)$ such that $f'(x) = \frac{f(b)-f(a)}{b-a}$. I don't remember a lot of the results that were proved with this (Rolle's, L'Hopital), but I should do the exercises to get a deeper understanding.

Lastly, the entire chapter builds up to a self-guided exercise that we can even get continuous functions that are differentiable nowhere. We considered the function $$g(x) = \sum_{n=0}^\inf \frac{1}{2^n}h(2^nx),$$ where $h(x)$ is the sawtooth function with period 2 formed by repeating $\mid x \mid$ on $[-1,1]$. I liked the author's choice to consider summations of absolute value functions instead of sinusoids, but it seems good to remember that this is not because absolute values have "corners", as sinusoids are smooth.

# Other reflections?

Yesterday, I got very little done, and set my goal for today to just "try again". I usually don't make this kind of goal because it makes me scared that I'll fall into an infinite loop of always trying again, but I'm glad I set it as my sole focus for today: to read my textbooks and do this kind of end-of-day synthesis. 

Likewise, I rarely make goals to "repeat today" because it feels complacent or that I'm not pushing myself, but I think this is a perfectly reasonable goal for tomorrow. True learning comes from an accumulation of effort, not a scattered walk.

Today I got very little done in the early afternoon, and only started working around 6 pm. Normally, I would inadvertently give up for the day, but I am proved wrong once again. It's never too late to start.

I stopped eating Chipotle for lunch recently because I tend to food coma in the afternoon. I also learned that certain foods leave a certain aftertaste that make me feel less energetic. Not sure what this is about.

I should follow the allure of great weather and Frisbee.


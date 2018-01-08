---
date: 2017-12-10
categories: strogatz
layout: post
title: "Strogatz 6: Phase Plane"
---

This chapter begins to work with nonlinear systems and the kind of qualitative behaviors we can deduce about a nonlinear system.

A pretty fundamental question that's pretty easily to overlook is:

#### **Does a general nonlinear system even have a unique solution?**

Fortunately, by the **existence and uniqueness theorem**, given a general system $\mathbf{\dot{x}} = f(\mathbf{x})$ and an initial value, as long as $f$ is continuous and all of its partial derivatives are also continuous on an open connected set, then there is a unique solution on a time interval $(-\tau, \tau)$ centered around $t=0$.

I took this definition straight from the book, and didn't look too far into the details. I have some vague intuition about why all of these conditions have to be true, but don't care too much to explore it further until I'm working on a domain that isn't open + connected someday. 

Two mystifying pieces of this are the parts about continuous partial derivatives. Suppose $f(\mathbf{x}) = \mid\mathbf{x}\,\mid$ and $\mathbf{x}(0) = 0$. Then there is an entire family of solutions: 

$$\mathbf{x} = \begin{cases}
  0 \qquad \text{ for } t<\tau \\      
  Ce^{t} \quad\, \text{ for } t \ge \tau
\end{cases}$$

It might be interesting to think about why: (1) we don't require any information about continuous second partial derivatives and (2) this result also guarantees a trajectory on a negative time interval.

#### **What kind of local information can we gather about nonlinear systems?**

We revisit the oldest trick in the book: approximate complex systems by more well-behaved systems that we know how to model well. In other words, we linearize the system. For a system $\mathbf{\dot{x}} = f(\mathbf{x})$, we can consider a Taylor series expansion of $f$. (Remember that $\mathbf{x}$ is $n$-dimensional.) We can drop higher order terms in our approximation, with the understanding that the model will only account for local behavior.

A rough sketch of how to use this technique given a system: (1) Identify the fixed points in the system, by setting $f(\mathbf{x}) = \mathbf{0}$. (2) For each fixed point $(x^\star, y^\star)$ in the system, approximate the local behavior by the Jacobian matrix of $f$ at $(x^\star, y^\star)$. This system is linear, so we can classify the stability and local trajectories with known techniques. 

![Linearization](/assets/strogatz6_local.png){:.center-image}

...Or can we?

#### **What are the limitations to linearization?**

It's not immediately clear that a fixed point in a nonlinear system has the same stability as its linearized counterpart. It turns out that if the linearized fixed point is not one of the borderline cases (saddle, node, spiral), then they really do share the same properties. On the other hand, if we find a fixed point to be a center, then it's really easy for higher-order nonlinear terms to turn the center into a spiral, and can mean the difference between stability and instability.

![Edge cases](/assets/strogatz6_unstable.png){:.center-image}

We can see that in [Figure 5.2.8]({% post_url 2017-11-30-strogatz5 %}) that centers are on the edge between two types of saddles. Similarly, for linearized stars and degenerate nodes, we might see higher order nonlinear terms change the behavior of trajectories between nodes and spirals, but we won't see the stability of the fixed point change.

#### **How do we think about global properties in a nonlinear system?**

In electromagnetics, we can deduce the amount of charge inside an arbitrarily chosen Gaussian surface by examining the electric field on the surface. In a similar manner, we can discover properties about a nonlinear system, such as the existence of limit cycles [[Ch. 7]] and fixed points in the surface.

For some phase portrait on a plane, choose an orientable curve $\mathcal{C}$. From looking at the vector field at each point $x$ on $\mathcal{C}$, we can intuitively define the **index** of $\mathcal{C}$ to be the number of times this vector rotates when traversing the curve. For example, the index in the below example is $I_{\mathcal{C}} = -1$.

![Index](/assets/strogatz6_index.png){:.center-image}

Phase portraits must satisfy some very nice properties:

1. If you can continuously deform $\mathcal{C}$ to get another curve $\mathcal{C}^\prime$ without passing through any fixed points, then $I_{\mathcal{C}} = I_{\mathcal{C}^\prime}$.
2. If $\mathcal{C}$ encloses exactly one attracting or repelling node, then the index is $+1$. Notice that the index cannot make stability distinctions.
3. If $\mathcal{C}$ encloses exactly one saddle node, the index is $-1$. This is shown in the example above.
4. If $\mathcal{C}$ does not contain any fixed points, then $I_{\mathcal{C}} = 0$. 

	*Proof*: Use (1) until you enclose an infinitesimally small region. The vectors should all point the same way.
5. If $\mathcal{C}$ is a trajectory for the system, then $I_{\mathcal{C}} = +1$. 

	*Proof*: Pretend you are an ant walking on the curve.

6. If $\mathcal{C}$ contains fixed points $x_1, x_2,\cdots, x_n$, then $I_{\mathcal{C}} = \sum I_{x_i}$. 

	*Proof*: Sketch; see below.

	![Summative property](/assets/strogatz6_summative.png){:.center-image}

Notice that properties (5) and (6) immediately imply that closed orbits must contain fixed points whose indices sum to $+1$. Furthermore, we can't have saddle nodes only.

<!-- Some additional questions to think about:

 - On what kind of topologies does this work? Is there a generalization to Gaussian surfaces?
 - Reminds me of the coulomb NN paper. -->

#### **Other**

There was an entire section on conservative systems and time-reversible systems, but I paid very little attention to these sections. What I remember: Conservative systems cannot have attracting fixed points.

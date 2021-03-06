
Chapter 5 was about linear systems, which was largely a review from differential equations. My overall take on the big questions of the chapter:

#### **How do we think about linear systems?**

Linear systems have scaling properties. This gives it the nice property that if there’s a point $x$ such that $\dot{x}$ points in the same direction as $x$ (Read: $\dot{x} = c_1x$), then all $y = c_2x$ will forever point in the same direction. So the idea is to hunt for these points (which are the eigenvectors). 

Once this is done, we classify the trajectories surrounding the eigen-lines and the stability of fixed points discovered. There are some edge cases with duplicate eigenvectors (degenerate systems) and complex eigenvalues (periodic behavior). 

![Classification of fixed points](/assets/strogatz5_classifications.png){:.center-image}

#### **How does a general trajectory behave?**

The trajectory zooms toward the slow eigen-line (on a plane). If we think about these points in the eigenbasis (using the eigenvectors as our $x,y$ axes and scaling appropriately), then every point will have a fast and slow eigenvector component. In each time-step, the phase portrait moves more in the fast direction, so it approaches the slow "eigen-axis" faster.

![Fast and slow eigendirections](/assets/strogatz5_fastslow.png){:.center-image}

#### **How to we think about stability in a system?**

There are two notions of stability: attracting points and Lyapunov stable points.

An **attracting** point is an $x$ such that for points sufficiently close to $x^\star$, the phase portrait eventually converges at $x^\star$ as $t\to \infty$. A **Lyapunov stable** point is an $x^\prime$ such that for points near $x^\prime$ stay close to $x^\prime$ for all time.

It’s pretty easy to come up with examples that satisfy both stability conditions or neither stability conditions. A example of a Lyapunov, but not attracting, stable point is the system 

$$\dot{x} = 0, \\\dot{y} = -y.$$

An example of an attracting, but not Lyapunov stable, point is the system

$$\dot{\theta} = -\theta\, \text{ for }\theta\in[0, 2\pi) $$

The point $\theta = 2\pi-\epsilon$ is very close to the attracting point $\theta = 0$. An interesting question is whether an attracting but non-Lyapunov stable point exists in $n$-dimensional space, and if not, what kind of topologies have this?

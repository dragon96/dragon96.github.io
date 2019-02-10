
A limit cycle is an isolated closed trajectory. Isolated means that trajectories near the limit cycle aren't closed. 

It's worth noting that limit cycles are inherently nonlinear phenomena and cannot happen in linear systems. The intuition is that if there exists a limit cycle on a set of points $X$ in a linear system, we expect there to be a limit cycle on the set $X_k = \{k\cdot\mathbf{x} \mid \mathbf{x}\in X\}$ for all scalars $k$. This violates the isolated property.

![Limit Cycles](/assets/strogatz7_limitcycles.png){:.center-image}

Like with attractors and nodes, closed orbits tell us information about the general "shape" or behavior of a system. Although we wouldn't be able to find a closed form solution describing a limit cycle in a system, their existence can give us information about how the system behaves. 

#### **What's the significance of limit cycles?**

By the uniqueness and existence theorem, if there is a closed orbit somewhere, a trajectory can never "cross" the orbit. Thus, the existence of limit cycles allows us to partition our analysis of the phase plane into non-interacting regions.

The **Poincare-Bendixson Theorem** is a cornerstone result concerning properties of systems that contain limit cycles. In particular, if we have a closed orbit $R$ and a trajectory inside of $R$ that is not attracted to any fixed points, then the trajectory must approach a closed orbit. (Note: It doesn't necessarily approach $R$. For example, consider the system $\dot{r} = 0$ and $\dot{\theta} = 1$.) Intuitively, this is reasonable, because by existence and uniqueness, the trajectory cannot cross $R$.

In fact, we can generalize $R$ to any closed, bounded regions. If $R$ doesn't contain any fixed points, then a trajectory inside of $R$ that never escapes $R$ will approach a limit cycle. 

![Poincare-Bendixson](/assets/strogatz7_poincare.png){:.center-image}

This seems to contradict one of the results we gathered from index theory in the last chapter. If the trajectory approaches the closed cycle $C$, then because $C$ has index of $+1$, it must contain a fixed point inside. But there are a couple caveats: (1) The fixed point is not necessarily attracting. (2) We can define $R$ to be a closed, bounded, donut-shaped region that purposely excludes these fixed points.

We can use this theorem to deduce the existence of a limit cycle somewhere in the system, if we find an appropriate **trapping region** $R$ that satisfies the properties above.

It's currently not clear to me how generalizable this theorem is to higher dimensions. Limit cycles have to be orientable, and I'm not sure if there's a topological generalization of this notion in higher dimensional spaces.

#### **Is it possible to prove that closed orbits do not exist in certain systems?**

Yes, but unfortunately, the techniques described only apply in special case systems. For example, **gradient systems**, which are systems that can be written in the form $\dot{\mathbf{x}} = -\nabla V(\mathbf{x})$, cannot contain closed orbits. 

If $C$ is a closed orbit, then the $\Delta V = 0$ after one circuit. On the other hand,

$$ \Delta V = \int_0^T \frac{dV}{dt} dt
 = \int_0^T \frac{dV}{dx} \cdot \frac{dx}{dt} dt 
 = \int_0^T \mid\mid \mathbf{x} \mid\mid^2 dt 
 > 0$$

This result can be generalized to systems $\dot{\mathbf{x}} = f(\mathbf{x})$ for which we can find a **Lyapunov function** $V(\mathbf{x})$ with the following properties: 

1. $V(\mathbf{x}) \ge 0$ for all $\mathbf{x}$, with equality iff $\dot{\mathbf{x}} = 0$. ($V$ is positive definite)
2. $\dot{V}(\mathbf{x}) \le 0$ for all $\mathbf{x}$, with equality iff $\dot{\mathbf{x}} = 0$. (All trajectories flow "downward")

![Lyapunov](/assets/strogatz7_lyapunov.png){:.center-image}

$V$ can be thought of as a generalized energy function, and $\dot{V}$ as a generalized dissipation function.

Unfortunately, these techniques come with two downsides. First, there is no consistent way to construct such energy functions. Second, gradient and Lyapunov functions only describe a small subset of nonlinear systems.

#### **Given that a limit cycle exists, how can we characterize its qualitative properties?**

We can often characterize the period and shape of the closed orbit approximately, although we often can't get exact solutions. 

For shape, looking at the nullclines appears to be a common tactic. The **nullclines** of a system $\dot{\mathbf{x}} = f(\mathbf{x})$ are the solutions to $\dot{x_i} = 0$ for some $i$. In some ways, this kind of inspection is similar to examining the zeros of a polynomial to get a sense of its shape.

For periodicity, big-O analysis seems like a pretty common trick. Suppose a system $\dot{\mathbf{x}} = f(\mathbf{x}, \epsilon)$ contains a parameter $\epsilon$. Often, we can expect some kind of approximate scale for $\epsilon$, since different orders of magnitudes for a parameter can drastically change the behavior of the system. 

When we have scale approximations like $0< \epsilon < < 1$, we can suddenly make more sensible approximations by using a power series to approximate the true solution, dropping the insignificant terms (which in this case are the $O(\epsilon^2)$ terms), and solving for approximate solution. Furthermore, we can characterize the time scales of different qualitative properties of a system (period, amplitude change, frequency shift, etc.) in terms of the complexity of this parameter $\epsilon$. 

For example, the true solution to this system has two time scales: the fast time scale of regular oscillations $O(1)$ and the slow time scale of amplitude decay $O(1/\epsilon)$, where $\epsilon = 0.1$ in this example. Because the approximation was only accounted for the fast time scale, it misses the long-term behavior of the system:

![Two time](/assets/strogatz7_twotime.png){:.center-image}

Because a system can have different time scales for different properties, it sometimes makes sense to use a **two-timing** analysis to account for these different time scales in the approximated system.



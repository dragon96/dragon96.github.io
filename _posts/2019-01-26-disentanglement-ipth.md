---
layout: post
title: "Disentanglement Algorithms"
categories: quantum
date: 2019-01-26 
---

Suppose you have a chain of $N$ spins placed adjacent to one another around a circle, as in Figure 1. Some of these spins may be entangled within $M$ subchains of indefinite length, where $1 \leq M \leq N$. You are provided with the density matrix $\rho$ corresponding to the system.

![Disentanglement Algorithms](/assets/ipth.png){:.center-image}

  (a) Construct an efficient algorithm which will isolate the $M$ subchains of the system. Assume that these subchains will be visible in the form of $\rho$ within a finite number $b$ of bases for your Hilbert space. Include an analysis of the complexity of your algorithm. Do so assuming that you have crafted this spin chain in a laboratory so that entangled subchains will consist only of adjacent spins.

  (b) A competing scientist sees that you are close to a result on your spin chains breakthrough paper and, in a dastardly attempt to jeopardize your grant funding, decides to rearrange the spins in your apparatus. Thankfully, this evildoer does so without disrupting the entanglement of the spins. Modify your algorithm to relax the assumption that subchains consist of adjacent spins. You may now encounter troubling exponential runtimes, so try your best to reduce them.

## Outline

Notation and Background

What is entanglement?

What can I do with the density matrix? What does it represent?

## So what counts as an algorithm? And how is complexity measured?

The restrictions on quantum gates are that the input dimension (the number of qubits) should match the number of output qubits. For example in Boolean logic, the NOT gate takes a single bit and outputs an inverted bit. However, unlike the AND gate, which maps 2 bits to 1 bit, quantum gates must match the input dimension.

How do we represent this mathematically? If a quantum gate has $n$ input lines, then it’s mapping a $2^n$ dimensional state space to a $2^n$ dimensional space, so we represent each gate $G$ as a $2^n\times 2^n$ matrix. What are the restrictions on $G$?. Its output must be a valid quantum state, meaning that for all states $\vert a \rangle$, we must have that $\langle Ga \vert Ga \rangle = 1$, or $G^\dagger G = I$. In other words, $G$ must be unitary. **Exercise**: verify this.

Are all unitary operators valid quantum gates? I don’t know, but I suspect so.

Let’s take a look at an example. The **Hadamard gate** $$H = \frac{1}{\sqrt2} \begin{bmatrix}1 & 1\\ 1 & -1\end{bmatrix}$$ operates on a single qubit. You can verify that $H \vert 0 \rangle = \frac1{\sqrt2}(\vert 0 \rangle + \vert 1 \rangle)$ and $H \vert 1 \rangle = \frac1{\sqrt2}(\vert 0 \rangle - \vert 1 \rangle)$. The intuition here is that a Hadamard can map a qubit into a superimposed version of its two possible "states". (idk what the correct term is.) However, it doesn’t have the power to "escape that space". 

How do you do apply a Hadamard gate to a multi-dimensional state? You can’t. The Hadamard gate can only map one qubit at a time. However, we can apply a gate to each of its bits. For example, applying $H$ to each of the bits of $\vert 001 \rangle $ yields 

$$\begin{eqnarray*} && H(\vert 0\rangle) \otimes H(\vert 0\rangle) \otimes H(\vert 1\rangle) \\
&=& \frac1{2\sqrt2}(\vert 0 \rangle + \vert 1 \rangle)\otimes(\vert 0 \rangle + \vert 1 \rangle)\otimes(\vert 0 \rangle - \vert 1 \rangle) \\
&=& \frac{1}{2\sqrt2}(\vert 000 \rangle - \vert 001\rangle +\vert 010 \rangle - \vert 011\rangle + \vert 100 \rangle - \vert 101\rangle + \vert 110 \rangle - \vert 111\rangle).
\end{eqnarray*}$$

This is an example of how we can start with a "deterministic" (non-superimposed) states and generate some superimposed state. Can all of the valid superimposed states be generated? I think yes, but not with Hadamard gates. **Exercise**.

So clearly, we cannot create entangled bits just by applying lower-dimensional gates and distributing the product. Are there gates that take two inputs and can entangle them? Yes. **Exercise**.

## Computation example: Deutsch’s algorithm

**Problem**: Let’s say we have a black box function $f: \{0, 1\} \to \{0, 1\}$. (as far as I can tell, these black box functions are sometimes called oracles.) I tell you that it’s either constant ($f(0) = f(1)$) or balanced ($f(0) \neq f(1)$), but you don’t know which one. The corresponding quantum gate $F$ maps $\vert a\rangle \vert b \rangle$ to $\vert a \rangle \vert b + f(a) \rangle$, where addition is done $\pmod 2$. How can we do this, and what is the complexity? 

You might be wondering why $F$ is implemented as above. Why map 2 qubits to 2 qubits when we can do this in one dimension? I have no idea why, but I suspect it has to do with ancillary computation. I don’t know what it really means, but my rough guess is that it needs some "temporary space" to store information to do the computation.

((give an outline of what needs to be done. start with a state. Perform some operations of superpositions and entanglements. Measure with interference. And complexity.))

You might also be wondering what complexity means for a quantum algorithm. My understanding is that it’s primarily based on the number of times you need to invoke the oracle. For example, can you find a way to do this with 2 queries? 

**Solution 2:** We can solve plugging in $F(\vert 0\rangle \vert b \rangle)$ and $F(\vert 1\rangle \vert b \rangle)$. If $f$ is constant, then the second qubits should match, and otherwise not. So first, we ignore the first qubit. (Remember that looking at a tensored product of pure states is just like running a few experiments independently. So ignoring is "legal" because we can simply forget that we even had a first qubit. It might be different if the two qubits were entangled though.) To measure, since there is no superposition in the second qubit, we can deterministically measure the bit value, and get our answer. 

Deutsch’s algorithm provides a way to do this with one query. ((how to give a hint about what needs to be improved intuitively?))

**Solution 1:** First start with $\vert 0 \rangle \vert 1 \rangle$. Pass each qubit through a Hadamard gate to get:

$$H(\vert 0\rangle\vert 1\rangle) = \frac12 (\vert 0\rangle + \vert 1\rangle)(\vert 0\rangle - \vert 1\rangle)$$ 

This expands to a superimposed 2D state. We pass this through $F$:

$$F(H(\vert 0\rangle \vert1\rangle)) = \frac12( \vert 0\rangle\vert f(0)\rangle + \vert 1\rangle\vert f(1) \rangle- \vert 0\rangle\vert 1+f(0)\rangle - \vert 1\rangle\vert 1+f(1) \rangle)$$

The idea here is that the signs of the coefficients allows us to distinguish terms. In particular, notice that if $f$ is constant, then the superimposed state is:

$$\pm( \vert 0\rangle\vert 0\rangle + \vert 1\rangle\vert 0\rangle- \vert 0\rangle\vert 1\rangle - \vert 1\rangle\vert 1 \rangle)$$

while if $f$ is balanced, then the superimposed state is:

$$\pm( \vert 0\rangle\vert 0\rangle + \vert 1\rangle\vert 1\rangle- \vert 0\rangle\vert 1\rangle - \vert 1\rangle\vert 0 \rangle)$$

so these two superimposed states are indeed distinguishable, but we need to express it in a form that can be deterministically measured. The trick here is to notice that both of the above expressions can be factored into the tensor product of 1D pure states, except with coefficient differences. So with some toil, we can find that the general factorization is:

$$F(H(\vert 0\rangle \vert1\rangle)) = \frac12( \vert 0\rangle + \color{brown}{(-1)^{f(0)+f(1)}}\vert 1\rangle)\otimes (\vert 0\rangle - \vert 1\rangle) $$

For ease of reading, I highlighted the coefficients in brown, which is easy to mix with the kets if you’re not accustomed to the notation. 

**Exercise**: Why did we choose $\vert 0\rangle \vert 1\rangle$ in the beginning? Why not other two dimensional inputs?

**Exercise**: Notice that after factorizing, the second qubit has not changed! Is there a faster way to notice this factorization? Or is there anything general we can say about the invariance of the last term?

Now applying $H$ to all the bits once more gives us:

$$H(F(H(\vert 0\rangle \vert1\rangle))) = \frac1{2}( \color{brown}{(1+ (-1)^{f(0)+f(1)})} \vert 0\rangle + \color{brown}{(1-(-1)^{f(0)+f(1)})}\vert 1\rangle)\otimes (\text{something}) $$

so that the first qubit is $\vert 0 \rangle$ if $f$ is constant and $\vert 1\rangle$ if it’s balanced. Now we can just measure and find out which one $f$ is!

**Exercise**: Do this for a higher dimension problem? Basically, Deutsch’s algorithm should extend to problems in which balanced means that exactly half of $f(\cdot)$’s are one value, and half the other value. Can we distinguish this in polynomial time? ((copy paste the problem statement for a $n$-dimensional version of Deutsch’s algorithm))

## Putting it all together

Now we’re ready to make sense of the problem. We have $N$ qubits, in which 

## notes to self

Okay, I still don’t exactly understand the formulation. Asking Dom and Michelle

For some reason, classical deterministic functions are used with (x,y) -> (x, y XOR f(x))

A measurement is also a special case of a quantum
gate | the probabilistic projection onto a set of mutually orthogonal subspaces

So the observation operator P (observable) is a Hermitian matrix with eigenvalues, and eigenspaces (vectors?) O_i and V_i. Then P(observing O_i) = Tr(proj(\rho, V_n)), and the new density matrix is:
	$$rho^\prime = P_n \rho P_n / Tr(P_n \rho)$$, where $$P_n$$ is the projection operator.
(Source: https://en.wikipedia.org/wiki/Measurement_in_quantum_mechanics)
			
A quantum gate is a unitary operator from one density matrix to another.

## Sources:

See OneTab group for sources in order of opening. Some especially helpful ones:
 * [Readable intro](https://www.quantiki.org/wiki/basic-concepts-quantum-computation)
 * [StackEx: Simple example of quantum algorithm](https://physics.stackexchange.com/questions/3390/can-anybody-provide-a-simple-example-of-a-quantum-computer-algorithm)
 * [Operations on density matrices](https://cs.uwaterloo.ca/~watrous/LectureNotes/CPSC519.Winter2006/14.pdf)



## Future directions for self

 * Still want to understand this ipth problem
 * Asking KXiang for pset problems. 
 * Is it always the case that the quantum implementation of a classical function $f$ is $\vert x \rangle \vert y\rangle \to \vert x\rangle\vert y \oplus f(x)\rangle$? Even if not, what makes this formulation more viable than others?
 * Understanding how universality of gates. Read some more on the primitive gates, and try to prove universal.
 * Knowing a few more problems + interesting results. Grover’s search algorithm and Shor’s come to mind, but I want to know enough quantum to come up with their formulations. Currently, still have no idea how search could even be formulated as a quantum algorithm.
 * Take a look at a quantum syllabus to know what else is out there.













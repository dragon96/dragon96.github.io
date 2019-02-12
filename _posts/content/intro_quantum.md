An introduction to quantum computing. I recommend thinking through the exercises to get the most out of this post.

## Notation

I won’t go into too much detail on what quantum states really are (mostly because I’ve never taken a quantum class), but here are some of the basics:

 * At its core, quantum states are complex vectors in a $2^n$ dimensional space, where $n$ is some integer. Mathematically, they must satisfy $q^\dagger \cdot q = 1$, where $q$ is a complex $2^n\times 1$ vector and $q^\dagger$ is its conjugate transpose. In other words, the norm of $q$ must be $1$. 
    * For example, in fake quantum notation (which we’ll fix in a second), $p$, $q$, $r$, and $s$ below are valid quantum states with $n=1$: 

	$$ p = \begin{bmatrix}1 \\ 0 \end{bmatrix} \qquad q = \begin{bmatrix}0 \\ 1\end{bmatrix} \qquad r = \begin{bmatrix} 1/\sqrt2 \\ 1/\sqrt2 \end{bmatrix} \qquad  s = \begin{bmatrix} (1+i)/2 \\ (1-i)/2 \end{bmatrix}$$

 * The quantum community uses *bra-ket* notation to rewrite these. A *ket* is used to describe one of the basis vectors (or basis states) in the $2^n$ dimensional space. For example, $p$ and $q$ above would be written as $\vert 0\rangle$ and $\vert 1\rangle$ respectively. The conjugate transposes $p^\dagger$ and $q^\dagger$ are written as $\langle 0 \vert$ and $\langle 1\vert$, which are called *bra*s.
   * The basis states $\vert 0 \rangle$ and $\vert 1\rangle$ are called *qubits*.
   * We also could have named $p = \vert 1\rangle$ and $q = \vert 0 \rangle$. However, by convention, when converting between matrix and bra-ket notation, we represent the $k$-th basis vector to be the state with $k$ written in binary, zero-indexed. Remember that the string inside of the $\vert \cdot \rangle$ is merely a name. We can also name our states $\vert \heartsuit \rangle$ and $\vert \Diamond\rangle$, but this is much harder to parse.
   * For $n=1$, each basis state represents the spin of an electron: up or down.
 * We can also consider linear combinations of these basis states. For example, $r$ above would be written as $\tfrac1{\sqrt2}\vert 0 \rangle + \tfrac1{\sqrt2}\vert 1\rangle$. 
   * Physically, this represents a *superposition* of the two basis states. This is where the story of Schrödinger’s cat comes in. In this superimposed state, the particle is in neither $\vert 0\rangle$ nor $\vert 1\rangle$ state, but upon *measuring*, we’ll find that it is $\vert 0\rangle$ with $(1/\sqrt2)^2 = 1/2$ probability and $\vert 1 \rangle$ with $(1/\sqrt2)^2 = 1/2$ probability. By measuring, we’ve changed the particle’s state permanently.
 * States can be tensored (outer-product-ed) together to form higher-dimensional states. In particular, $\vert 0\rangle\otimes \vert 1\rangle$ and $\vert 01\rangle$ are notationally equivalent. Tensoring is merely a way of considering two properties simultaneously. For example, with playing cards, we have 13 states to represent each unique number and $4$ states to represent each unique suit. $\text{number}\otimes \text{suit}$ represents each unique card. 
   * The outer product of two states with superimposed states can be distributed in the same way we distribute polynomials.

This may take some time to get used to. Just remember that the most important rule is that, in bra-ket notation, $\langle a \vert a \rangle = 1$.

## Quantum Gates

We can think about quantum operations from two different angles: (1) physically, what does a quantum operation represent? (2) mathematically, how do we represent them? 

Unfortunately, I don’t have an answer for (1). Nevertheless, we know that because qubits represent something physical, so we can build a bridge between (1) and (2) by finding mathematical invariants for each of the physical laws they must satisfy. The axioms that we take for granted for now are:

 * If $G$ is a quantum gate, then its input dimension must match its output dimension. Formally, $G: \\{0,1\\}^n \to \\{0,1\\}^n$ for some $n$. <!-- is this true in general? 90% yes because operations are unitary, thus square. -->
 * All quantum gates $G$ correspond to some unitary operation, i.e. $G^\dagger G = I$. Here, $G^\dagger$ means the conjugate transpose of $G$.

Let’s see why the unitary condition must hold. The output of a quantum gate must be a valid quantum state, meaning that for all states $\vert a \rangle$, we must have that $\langle Ga \vert Ga \rangle = 1$, or in matrix notation, $a^\dagger(G^\dagger G)a = 1$ for all column vectors $a$. 

**Exercise**: Show that $a^\dagger(G^\dagger G)a = 1$ implies that $G^\dagger G = 1$.

A couple corollaries worth mentioning:

 * $G$ can have complex entries.
 * $G$ is linear. This is wonderful, because this helps us to define quantum operations on superimposed states just by specifying how it acts on basis states. For example, $G\left(\tfrac1{\sqrt2}\vert 0\rangle + \tfrac1{\sqrt2} \vert 1\rangle\right) = \tfrac1{\sqrt2}G(\vert 0 \rangle) + \tfrac1{\sqrt2}G(\vert 1\rangle)$. 
 * If $G$ acts on $n$-dimensional states, then $G$ is a $2^n \times 2^n$ matrix. For example, if $n=2$, then we could have an operation that reverses the order of the basis qubits:
 
 $$G = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \qquad\Longrightarrow\qquad \begin{array}{l} G(\vert 00 \rangle) = \vert 00 \rangle \\ G(\vert 01 \rangle) = \vert 10 \rangle \\ G(\vert 10 \rangle) = \vert 01 \rangle \\ G(\vert 11 \rangle) = \vert 11 \rangle \end{array}$$ 
 
**Exercise**: Note that in the last example, I am making an implicit assumption that the rows correspond to $\vert 00 \rangle, \vert 01 \rangle, \vert 10\rangle, \vert 11\rangle$ in that order. Show that even if the rows of $G$ correspond to the 4 quantum states in some other order, $G$ would still be a valid unitary operation. 
 
**Question**: You might be wondering if all unitary operators have a corresponding quantum gate. The answer is yes! We’ll take this granted for now, but it could be fun to explore why this is the case.

## The Hadamard Gate 

Let’s take a look at an example. The **Hadamard gate** is given by

$$H = \frac{1}{\sqrt2} \begin{bmatrix}1 & 1\\ 1 & -1\end{bmatrix}$$ 

and operates on a single qubit. You can verify that 

$$H(\vert 0 \rangle)= \frac1{\sqrt2}(\vert 0 \rangle + \vert 1 \rangle) \quad\text{ and }\quad H (\vert 1 \rangle)= \frac1{\sqrt2}(\vert 0 \rangle - \vert 1 \rangle)$$

Note that the Hadamard gate operates on qubits in 1-dimensional space, so it cannot be applied to states of higher dimension. However, we can apply the gate to each of the bits in a higher dimensional state. For example: 

$$\begin{eqnarray*} H(\vert 001\rangle) &=& H(\vert 0\rangle) \otimes H(\vert 0\rangle) \otimes H(\vert 1\rangle) \\
&=& \frac1{2\sqrt2}(\vert 0 \rangle + \vert 1 \rangle)\otimes(\vert 0 \rangle + \vert 1 \rangle)\otimes(\vert 0 \rangle - \vert 1 \rangle) \\
&=& \frac{1}{2\sqrt2}(\vert 000 \rangle - \vert 001\rangle +\vert 010 \rangle - \vert 011\rangle + \vert 100 \rangle - \vert 101\rangle + \vert 110 \rangle - \vert 111\rangle).
\end{eqnarray*}$$

This is an example of how we can start with a "deterministic" state and transformed them into a indeterminate state. 

**Question**: Can all valid linear combinations of states in $\\{0,1\\}^n$ be generated by a sequence of quantum gate operations on a deterministic quantum state? I suspect the answer is yes.

Not all valid quantum states in $\\{0, 1\\}^n$ can be generated with Hadamard gates and tensor products. One such example is $\frac1{\sqrt2}(\vert 00\rangle + \vert 11\rangle)$, which is the canonical example of *entangled bits*. This shows that we cannot entangle bits just by applying lower-dimensional gates and distributing them over a tensor product. 

**Exercise**: Prove or disprove: One cannot create an entangled quantum state from only applications of single-input quantum gates on basis states (e.g. $\vert 0\rangle$ and $\vert 1 \rangle$).

**Exercise**: Find a quantum gate that takes two or more inputs and can create an entangled quantum state. 

## Computation example: Deutsch’s algorithm

We’ll take a look at our first example of a quantum algorithm.

**Problem**: Suppose there is a black box function $f: \\{0, 1\\} \to \\{0, 1\\}$, which is eitherconstant ($f(0) = f(1)$) or balanced ($f(0) \neq f(1)$), but you don’t know which one. Find an algorithm to discern whether $f$ is constant or balanced.

Let’s first unpack what the problem is asking.

First, note that there is a little bit of ambiguity about how $f$, a mathematical function is implemented as a quantum gate. Unintuitively, we’ll consider the quantum gate $F$, also called the *oracle*, which maps $\vert a\rangle \vert b \rangle$ to $\vert a \rangle \vert b \oplus f(a) \rangle$, where $\oplus$ is the XOR operation. This is a fairly general way of implementing a classical function into a quantum gate.

**Exercise**: You might be wondering why $F$ is implemented as a two-input gate with the dummy qubit $b$. Why not have a quantum gate $F^\prime$ with $F^\prime(\vert a\rangle) = \vert f(a) \rangle$? What is the key idea that makes $F$ such a general implementation of a classical function? 

Hint:
<div class="hint">What is the matrix corresponding to $F^\prime$?</div>

You might also be wondering how we measure the efficiency of a quantum algorithm. For example, in classical algorithms, it is common to look at the runtime complexity. In quantum algorithms, we count the number of times the oracle is queried. 

**Exercise**: Propose an algorithm that uses two queries. 

Solution:
<div class="hint"> We can solve by considering $F(\vert 0\rangle \vert b \rangle)$ and $F(\vert 1\rangle \vert b \rangle)$, and ignoring the first qubit of the outputs. If $f$ is constant, then the second qubits of the outputs should match, and otherwise not. <br />

Ignoring the first qubit is "legal" because a product of two lower dimensional quantum states is like having two completely separate experiments. We can directly measure the second qubit since there are no indeterminate states on the second qubit.</div>

Deutsch’s algorithm provides a way to solve this with one query. 

**Solution**: First we start with $\vert 0 \rangle \vert 1 \rangle$. It should make sense why we choose this starting state later. Pass each qubit through a Hadamard gate to get:

$$H(\vert 0\rangle\vert 1\rangle) = \frac12 (\vert 0\rangle + \vert 1\rangle)(\vert 0\rangle - \vert 1\rangle)$$ 

The intuition is that a Hadamard gate "expands" the qubits for us so that we can simultaneously operate on multiple states. We pass this output through $F$:

$$F(H(\vert 0\rangle \vert1\rangle)) = \frac12( \vert 0\rangle\vert f(0)\rangle + \vert 1\rangle\vert f(1) \rangle- \vert 0\rangle\vert 1+f(0)\rangle - \vert 1\rangle\vert 1+f(1) \rangle)$$

The idea here is that the signs of the coefficients allows us to distinguish terms. In particular, notice that if $f$ is constant, then the superimposed state is:

$$\pm\frac12 ( \vert 0\rangle\vert 0\rangle + \vert 1\rangle\vert 0\rangle- \vert 0\rangle\vert 1\rangle - \vert 1\rangle\vert 1 \rangle)$$

If $f$ is balanced, then the superimposed state is:

$$\pm\frac12 ( \vert 0\rangle\vert 0\rangle + \vert 1\rangle\vert 1\rangle- \vert 0\rangle\vert 1\rangle - \vert 1\rangle\vert 0 \rangle)$$

In both of the above expressions, we take the positive sign if and only if $f(\vert 0 \rangle) = 0$.

**Exercise**: Before proceeding to read the remainder of the solution, try to find a general, closed-form expression for $F(H(\vert 0 \rangle\vert 1\rangle))$.

So these two outputs are indeed distinguishable, but the problem is that these are superimposed states and therefore they cannot be deterministically measured. The trick here is to notice that both of the above expressions can be factored into the tensor product of 1D states:

$$\begin{array}{rl} \text{Constant:} & \pm\frac12(\vert 0 \rangle + \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \\ \text{Balanced:} & \pm\frac12 (\vert 0 \rangle - \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \end{array}$$

Now let’s rewrite this in a closed-form way that doesn’t have the $\pm$ in the expressions:

$$\begin{array}{rl} \text{Constant:} & \frac12\cdot (-1)^{f(0)}\cdot (\vert 0 \rangle + \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \\ \text{Balanced:} & \frac12\cdot (-1)^{f(0)}\cdot (\vert 0 \rangle - \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \end{array}$$

And let’s see if we can take this even further by combining these two expressions:

$$ \begin{eqnarray*} F(H(\vert 0\rangle \vert1\rangle)) &=& \frac12\cdot (-1)^{f(0)}\cdot (\vert 0 \rangle + (-1)^{f(0)+f(1)}\cdot \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \\ &=& \frac12((-1)^{f(0)}\cdot \vert 0 \rangle + (-1)^{f(1)}\cdot \vert 1 \rangle)\otimes (\vert 0 \rangle - \vert 1\rangle) \end{eqnarray*}$$

**Exercise**: Why did we choose $\vert 0\rangle \vert 1\rangle$ in the beginning? Why not start with $\vert 0\rangle \vert 0 \rangle$?

**Exercise**: Notice that after factoring, the second qubit has not changed! Is there a faster way to see this?

Now applying $H$ to all the bits once more gives us:

$$\begin{eqnarray*} H(F(H(\vert 0\rangle \vert 1\rangle))) &=& \frac12\left(H((-1)^{f(0)}\cdot \vert 0 \rangle ) + H((-1)^{f(1)}\cdot \vert 1\rangle)\right)\otimes H(\vert 0 \rangle + \vert 1\rangle ) \\ &=& \frac1{\sqrt2} \left(((-1)^{f(0)} + (-1)^{f(1)})\cdot \vert 0 \rangle + ((-1)^{f(0)} - (-1)^{f(1)})\cdot \vert 1\rangle \right)\otimes \vert 1\rangle \end{eqnarray*} $$

The first qubit comes out to $\pm \vert 0 \rangle$ if $f$ is constant and $\pm \vert 1\rangle$ if it’s balanced. Now we can just measure and find out which one $f$ is!

**Exercise**: The most general form of Deutsch’s algorithm is as follows: Let $f: \\{0, 1\\}^n \to \\{0,1\\}$, where $f$ is either constant or balanced (exactly half of the states $s$ satisfy $f(s) = 0$ and the other half satisfy $f(s) = 1$.) Propose an algorithm distinguish whether $f$ is constant or balanced in $O(1)$ queries. How many queries would it take classically, in terms of $n$? 


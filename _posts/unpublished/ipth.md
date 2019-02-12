Quantum Computation basics

 - Hadamard Gates (and what a gate is) 
   - How is complexity measured?
   - Measurement is a gate!
 - Deutsch‰s algorithm (the 1 bit version)
   - Unitary operations
     - Intuition that the first Hadamard gate
   - Gates that apply a function f
     - Why we use (a,b) -> (a, b XOR f(a))
   - Measurement gates (incomplete understanding)
 - Deutsch‰s algorithm (the n bit version)
   - Leave this as an exercise with hints and hide tags?
 - The f(a) = 1 for only one value of n problem.
   - (incomplete understanding) 
     - What are the -1 gates?
     - The orthogonal observation, and implementing a unitary operation with all states as columns.
     - Non-solutions:
       - Can I split into two parts and measure accordingly?
       - Can I just superimpose two states directly?
       - Is there a "look in the box directly" operation?

 - Some future directions:
   - H is its own inverse. So is F. Why?
   - Grover‰s search algorithm

markdown \{ and \}
vim jump down a physical terminal line
~                                                  




## Problem

Suppose you have a chain of $N$ spins placed adjacent to one another around a circle, as in Figure 1. Some of these spins may be entangled within $M$ subchains of indefinite length, where $1 \leq M \leq N$. You are provided with the density matrix $\rho$ corresponding to the system.

![Disentanglement Algorithms](/assets/ipth.png){:.center-image}

  (a) Construct an efficient algorithm which will isolate the $M$ subchains of the system. Assume that these subchains will be visible in the form of $\rho$ within a finite number $b$ of bases for your Hilbert space. Include an analysis of the complexity of your algorithm. Do so assuming that you have crafted this spin chain in a laboratory so that entangled subchains will consist only of adjacent spins.

  (b) A competing scientist sees that you are close to a result on your spin chains breakthrough paper and, in a dastardly attempt to jeopardize your grant funding, decides to rearrange the spins in your apparatus. Thankfully, this evildoer does so without disrupting the entanglement of the spins. Modify your algorithm to relax the assumption that subchains consist of adjacent spins. You may now encounter troubling exponential runtimes, so try your best to reduce them.



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



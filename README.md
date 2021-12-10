# Busy beaver

This is an implementation of The Busy Beaver Problem in Python, java and C++.

What is a busy beaver?

Consider Turing machines with fixed numbers of states and symbols.
If there are k states and n symbols, then the number of possible next move functions, or possible tables, is (2kn+1)kn.
Thus, there are (2kn+1)kn Turing machines with k states and n symbols.
Each of them can be launched on a blank tape, that is a tape with symbols 0 in all cells.
Then some of them never stop, and the other ones eventually stop.
Those which stop are called **busy beavers**.

Busy beavers compete in two competitions:
- to take the most time to stop,
- to leave the most non-blank symbols on the tape when stopping.

We denote by **s(M)** the time taken by busy beaver M, and by **sigma(M)** the number of non-blank symbols left on the tape by M.
We denote by **S(k,n)** the time taken by the busy beaver with k states and n symbols which takes the most time to stop:

S(k,n) = max {s(M) : M is a busy beaver with k states and n symbols}

We denote by Sigma(k,n) the number of non-blank symbols left on the tape by the busy beaver with k states and n symbols which leaves the most non-blank symbols on the tape when stopping:

Sigma(k,n) = max {sigma(M) : M is a busy beaver with k states and n symbols}

***Currently people have managed to solve it for n=1,2,3,4 (for Turing Machines
with 1, 2, 3 and 4 states) by reasoning about and running all the possible
Turing Machines, but for n = 5 this task has currently been impossible.
While most likely it will be solved for n=5, theorists doubt that it shall
ever be computed for n=6.***

## Run
### Python
Enter the number of states as command-line arguments. 

``` python run.py 3 ```

## Reference

- [Busy Beaver competition, Publications in Logic and Theoretical Computer Science by Pascal MICHEL](https://webusers.imj-prg.fr/~pascal.michel/bbc.html)
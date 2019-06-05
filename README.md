# pymplectic
pymplectic is a python software that can solve hamiltonian problems separables in three parts.
## Getting Started
You can download this software with the next order:
```
git clone https://github.com/cosmogat/pymplectic
```
and you can use the example program:
```
python execucio.py
```
This software uses two classes: Metode for define the symplectic method and Solucionador for solve the problem.
## Solucionador class
This class needs a method (Metode object), a map for evolve the initial conditions, an initializer for read the initial conditions and optionally other atributtes.
## Method class
Methods needs the kind of method and the kind of processed method.

## References
* S. Blanes and F. Casas: A Concise Introduction to Geometric Numerical Integration. CRC Press.
* E. Gerlach, J. Meichsner and C. Skokos. On the symplectic integration of the discrete nonlinear Schrödinger equation with disorder. https://doi.org/10.1140/epjst/e2016-02657-0
* Yang He, Yajuan Sun, Jian Liu, Hong Qin. Volume-preserving algorithms for charged particle dynamics. http://dx.doi.org/10.1016/j.jcp.2014.10.032

## Autors
* **Cosmo Cat**  [cosmogat](https://github.com/cosmogat)
## License
See the [LICENSE](LICENSE)

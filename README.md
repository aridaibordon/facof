# FACOF: FAC on terminal framework
Framework for the computation of atomic data using [Flexible Atomic Code](https://github.com/flexible-atomic-code/fac) python interface (PFAC) directly from the terminal.


## Use and installation
This package requires python >= 3.11 and PFAC >= 1.1.5. Default parameters for the configuration interaction and UTA can be changed directly in `config.py`.

FACOF includes a wizard that allows direct use of all its functionalities directly from the terminal. It can be open by calling this package folder. The available flags are,

- `-l ELEM NELEC`: compute atomic level structure by specifying the element (ELEM) and number of bound electrons (NELEC).
- `-t ELEM NELEC`: compute atomic transitions and level structure by specifying the element (ELEM) and number of bound electrons (NELEC).
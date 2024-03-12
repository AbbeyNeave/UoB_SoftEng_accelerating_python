This cythonized code is built and run with two command line arguments.

Firstly, use the below argument to run the setup script and build a c version of the cythonized pyx file, as well as a 'build' folder:
    "python cython_setup.py build_ext -fi"

Secondly, use the below argument to run the run script, utilising the c version and build folder to produce outputs for the cythonized code:
    "python -m cProfile cython_run.py <ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG>"
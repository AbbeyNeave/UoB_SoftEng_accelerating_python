import sys
from LebwohlLasher_cython import initdat
from LebwohlLasher_cython import plotdat
from LebwohlLasher_cython import savedat
from LebwohlLasher_cython import one_energy
from LebwohlLasher_cython import get_order
from LebwohlLasher_cython import MC_step
from LebwohlLasher_cython import main

# Main part of program, getting command line arguments and calling
# main simulation function.
#
if __name__ == '__main__':
    if int(len(sys.argv)) == 5:
        PROGNAME = sys.argv[0]
        ITERATIONS = int(sys.argv[1])
        SIZE = int(sys.argv[2])
        TEMPERATURE = float(sys.argv[3])
        PLOTFLAG = int(sys.argv[4])
        main(PROGNAME, ITERATIONS, SIZE, TEMPERATURE, PLOTFLAG)
    else:
        print("Usage: python {} <ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG>".format(sys.argv[0]))
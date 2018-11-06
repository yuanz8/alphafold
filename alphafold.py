#!/usr/bin/python
import argparse
from alphafold.partition import *
from tests_alphafold import test_alphafold

if __name__=='__main__':

    parser = argparse.ArgumentParser( description = "Compute nearest neighbor model partitition function for RNA sequence" )
    parser.add_argument( "-s","-seq","--sequences",help="RNA sequences (separate by space)",nargs='*')
    parser.add_argument("-c","-circ","--circle", action='store_true', default=False, help='Sequence is a circle')
    parser.add_argument("-v","--verbose", action='store_true', default=False, help='output dynamic programming matrices')
    parser.add_argument("--simple", action='store_true', default=False, help='Use simple recursions (slow!)')
    parser.add_argument("--calc_deriv", action='store_true', default=False, help='Calculate derivative')
    parser.add_argument("-b","--backtrack", action='store_true', default=False, help='Backtrack to get MFE')
    args     = parser.parse_args()

    if args.sequences != None: # run tests
        (Z, bpp, bps_MFE, dZ) = partition( args.sequences, circle = args.circle, verbose = args.verbose, backtrack = args.backtrack, calc_deriv = args.calc_deriv, use_simple_recursions = args.simple )
    else:
        test_alphafold( verbose = args.verbose, use_simple_recursions = args.simple )

import argparse
import sys
import os
sys.path.append('src/')
import graph
import solver_algorithms
from solver_algorithms import randomized_tree, joined_forest_tree
from input_output import input_graphs_from_file, output_graphs_to_new_file


if __name__ == "__main__":
    # Argument Parse
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--num_rand_runs', type=int, default=100, help="Number of random runs for spanning tree algorithm")
    parser.add_argument('-m', '--mode', type=str, default="rand", choices=['rand','forest'], help="Choose which algorithm to use," +
                                                                                                "\"rand\" represent randomized tree algorithm" +
                                                                                                "\"forest\" represent joined forest tree algorithm")
    parser.add_argument('-n', '--max_num_nodes', type=int, default=100, help="Maximum number of nodes in a graph")
    parser.add_argument('-i', '--input', type=str, default="sample/OURHARD.in", help="Input file path")
    parser.add_argument('-o', '--output', type=str, default="sample/OURHARD.out", help="Output file path")
    args = parser.parse_args()
    # Input
    graphs = input_graphs_from_file(args.input)
    print(f'Receiving input file {os.path.abspath(args.input)}')
    # Set constant
    graph.MAX_NUM_NODES = args.max_num_nodes
    solver_algorithms.NUM_RAND_RUNS = args.num_rand_runs
    # Process
    print(f'Start calculating...')
    out = []
    for i, g in enumerate(graphs):
        print(f'Calculate {i+1}-th graph:    ', end='')
        if args.mode == 'rand':
            soln = randomized_tree(g)
        else:
            soln = joined_forest_tree(g)
        out.append(soln)
        print(f'Finished')
    # Output
    print(f'Finished calculating. Output to {os.path.abspath(args.output)}')
    output_graphs_to_new_file(out, args.output)
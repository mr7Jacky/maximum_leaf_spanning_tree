import os
from graph import Graph, Edge, make_graph
from graph_helper import get_leaves, get_edges
from collections import deque
import numpy as np



"""
This file contains functions for reading graphs from files and writing them to files.
"""
def do_everything():
	dirname=os.path.dirname
	format_instance(os.path.join(dirname(dirname(__file__)), "sample/hard.in"))
# Reads and returns all graphs in the given text file
# NOTE: Graphs must be in format given by instructors
def format_instance(file_name):

	# Read in raw lines
	with open(file_name, 'r') as input_file:
		raw_lines = input_file.readlines()

	with open(file_name, 'r') as input_file:
		raw_lines_1 = input_file.readlines()

	# Strip newline from each line
	for i in range(len(raw_lines)):
		raw_lines[i] = raw_lines[i].strip()

	# Store lines in a queue (using deque) for efficient processing
	lines = deque(raw_lines)

	# Read the number of graphs in file
	if len(lines) > 0:
		number_of_graphs = int(lines.popleft())
	else:
		return []
	with open(file_name, 'w') as ourfile:
		ourfile.writelines(raw_lines)
	index = 0
	# Read lines in nested structure
	for _ in range(number_of_graphs):
		number_of_edges = int(lines.popleft())
		newset=set()
		index = index + 1

		for _ in range(number_of_edges):
			edge_ends = lines.popleft().split()
			newset.add(int(edge_ends[0]))
			newset.add(int(edge_ends[1]))

		number_of_vertices = len(newset)
		raw_lines_1[index]=str(number_of_vertices) + ' ' + str(number_of_edges) + '\n'
		index = index + number_of_edges
	with open(file_name, 'w') as ourfile:
		ourfile.writelines(raw_lines_1)



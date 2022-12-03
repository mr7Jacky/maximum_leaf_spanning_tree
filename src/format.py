import os
from graph import Graph, Edge, make_graph
from graph_helper import get_leaves, get_edges, get_nodes
from collections import deque
import numpy as np



"""
modify format of hard.in
"""
def do_everything():
	dirname=os.path.dirname
	# format_instance(os.path.join(dirname(dirname(__file__)), "sample/OURHARD.in"))
	format_edges(os.path.join(dirname(dirname(__file__)), "sample/OURHARD.in"),os.path.join(dirname(dirname(__file__)), "sample/OURHARD1.in"))
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
	# with open(file_name, 'w') as ourfile:
	# 	ourfile.writelines(raw_lines)
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

def format_edges(file_name, output_file_name):

	# Read in raw lines
	with open(file_name) as input_file:
		raw_lines = input_file.readlines()

	output_file = open(output_file_name, 'w')

	# Strip newline from each line
	for i in range(len(raw_lines)):
		raw_lines[i] = raw_lines[i].strip()

	# Store lines in a queue (using deque) for efficient processing
	lines = deque(raw_lines)

	# Maintain a list of graphs
	graphs = []

	# Read the number of graphs in file
	if len(lines) > 0:
		number_of_graphs = int(lines.popleft())
	else:
		return []
	output_file.write(str(number_of_graphs)  + '\n')
	# Read lines in nested structure
	for _ in range(number_of_graphs):
		edges = []
		edge_vtx_info = lines.popleft().split()
		number_of_vertices = int(edge_vtx_info[0])
		number_of_edges = int(edge_vtx_info[1])


		for _ in range(number_of_edges):
			edge_ends = lines.popleft().split()
			u = int(edge_ends[0])
			v = int(edge_ends[1])
			edges.append(Edge(u, v))

		edges.sort(key=lambda x: (x.ends[0], x.ends[1]))
		output_file.write(str(np.max(number_of_vertices)) + ' ' + str(number_of_edges) + '\n')

		# Output all the edges in this graph to file
		for edge in edges:
			u = edge.ends[0]
			v = edge.ends[1]
			output_file.write(str(u) + ' ' + str(v) + '\n')


	


	

# def output_graphs_to_new_file(graphs, file_name):
# 	output_file = open(file_name, 'w')

# 	# Output number of graphs
# 	# number_of_graphs = len(graphs)
# 	# output_file.write(str(number_of_graphs) + '\n')

# 	for graph in graphs:
# 		output_graph_file(graph, output_file)

# 	output_file.close()

# def output_graph_file(graph: Graph, output_file):

# 	# Build a list of distinct edges
# 	edges = get_edges(graph)
# 	vertices = get_nodes(graph) 
# 	number_of_vertices = len(vertices)
# 	# Output number of edges in this graph to file
# 	number_of_edges = len(edges)
# 	output_file.write(str(np.max(number_of_vertices)) + ' ' + str(number_of_edges) + '\n')

# 	# Output all the edges in this graph to file
# 	for edge in edges:
# 		u = edge.ends[0]
# 		v = edge.ends[1]
# 		output_file.write(str(u) + ' ' + str(v) + '\n')


# network-simulation

AUTHOR:
Gabrielle Talavera

DESCRIPTION: This project simulates a mesh network where nodes and links may fail. Nodes may fail intermittently,
and as an input to the simulation, each node and link will have a certain probability to fail. When such failure
occurs, the network must adapt and re-route to avoid the faulty node. This network uses the Floyd-Warshall algorithm 
to route to a source and destination.

ADDITIONAL FEATURE: This program uses the Floyd-Warshall algorithm to route to a source to destination. There is a 
feature that can compare Dijkstra's and the Bellman-Ford algorithm to the Floyd-Warshall algorithm. To compare
Floyd-Warshall to Dijkstra's uncomment lines: 107, 112, 122. To compare Floyd-Warshall with the Bellman-Ford algorithm
uncomment lines: 108, 113, 123.

RUNNING THE PROGRAM:
1. Make sure Python is installed. I used version 3.7.4 to build this project.
2. Make sure numpy and networkx packages are downloaded
3. Run the program using 'python sim.py'
4. Follow the prompts that the program gives you when executed

OUTPUT:
- Original Path
- Number of hops with no node failures
- Total Cost of Path
- Updates:
	- Nodes that fail every cycle.
	- Updated path from source node to destination node
	- Number of hops (how many links it has to pass over)
	- Total Cost of path (all the weights on links added up)
	- If the Dijkstra and Bellman-Ford feature is activated, then the
  	  path, hops, and total cost would be printed for these algorithms

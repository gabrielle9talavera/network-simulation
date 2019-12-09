#####################################################################################################################
# AUTHOR:
# Gabrielle Talavera
#
# DESCRIPTION: This project simulates a mesh network where nodes and links may fail. Nodes may fail intermittently,
# and as an input to the simulation, each node and link will have a certain probability to fail. When such failure
# occurs, the network must adapt and re-route to avoid the faulty node.
#
# RUNNING THE PROGRAM:
# 1. Make sure Python is installed preferrably 3.7.4
# 2. Make sure numpy and networkx packages are downloaded
# 3. Run the program using 'python sim.py'
#
# OUTPUT:
# - Original Path
# - Number of hops with no node failures
# - Total Cost of Path
# - Updates:
#   - Nodes that fail every cycle.
#   - Updated path from source node to destination node
#   - Number of hops (how many links it has to pass over)
#   - Total Cost of path (all the weights on links added up)
#   - If the Dijkstra and Bellman-Ford feature is activated, then the
#   path, hops, and total cost would be printed for these algorithms
######################################################################################################################
import networkx as nx
import random
import numpy as np


# this gets a user input of how many nodes that are wanted
# returns an integer of the amount of nodes
def nodeAmount():
    # An input is requested and stored in a variable
    text = input("Enter number of nodes: ")

    # Converts the string into a integer.
    nodes = int(text)

    return nodes


# this gets a user input of the probability of node failure
# returns a float which is the probability of failure
def nodeFailure():
    failProb = -1
    while failProb < 0 or failProb > 1:
        text = input("Enter probability of node failure (0-1): ")
        failProb = float(text)
    return failProb


# this gets a user input of the starting node
# returns an integer which is the source node
def srcNode(nodeAmount):
    src = -1
    while src > (nodeAmount-1) or src < 0:
        text = input("Enter source node (possible values from 0 to the number of nodes - 1): ")
        src = int(text)
    return src


# this gets a user input of the ending node
# returns an integer which is the destination node
def destNode(nodeAmount):
    dest = -1
    while dest > (nodeAmount-1) or dest < 0:
        text = input("Enter destination node (possible values from 0 to the number of nodes - 1): ")
        dest = int(text)
    return dest


# this generates the graph
# Parameters: n = node amount (based on user input)
# returns the graph (network)
def generateGraph(n):
    # finds the max amount of edges that can exist
    maxEdges = (n * (n - 1)) / 2

    # based on the max amount of edges, it randomizes a number of edges that our graph will have
    e = random.randint(n, maxEdges)

    # this generates a random graph using the amount of nodes and edges
    g = nx.gnm_random_graph(n, e)

    # this randomly assigns weights to the edges
    for (u, v) in g.edges():
        g.edges[u, v]['weight'] = random.randint(1, 10)

    return g

# this finds the shortest path using the Floyd-Warshall function which was imported from networkx
# if you want to compare Floyd-Warshall with Dijkstra's uncomment lines: 107, 112, 122
# if you want to compare Floyd-Warshall with Bellman-Ford uncomment lines: 108, 113, 123
def findPath(graph, src, dest):
    # finds node predecessors using a function imported from networkx
    predecessors, _ = nx.floyd_warshall_predecessor_and_distance(graph)

    try:
        # finds the shortest path through the Floyd-Warshall algorithm by using a function imported from networkx
        path = nx.reconstruct_path(src, dest, predecessors)
        dpath = nx.dijkstra_path(graph, src, dest)
        bfpath = nx.bellman_ford_path(graph, src, dest)

        # prints the shortest path
        print("Path:", path)
        # print("Dijkstra's Path:", dpath)
        # print("Bellman-Ford Path:", bfpath)

        # prints the number of hops from source to destination
        print("Number of Hops:", len(path)-1)
        # print("Dijkstra's Number of Hops:", len(dpath)-1)
        # print("Bellman-Ford Number of Hops:", len(bfpath)-1)

        # gets the total cost
        edge = 0
        for i in range(1, len(path)):
            edge += graph.edges[path[i - 1], path[i]]['weight']
        dpathcost = nx.dijkstra_path_length(graph, src, dest)
        bfpathcost = nx.bellman_ford_path_length(graph, src, dest)
        print("Total Cost:", edge)
        # print("Dijkstra's Total Cost:", dpathcost)
        # print("Bellman-Ford Total Cost:", bfpathcost)
        print()

    except:
        # Print to the terminal if no path exists.
        print("ERROR: No available path from source: node", src, "to destination: node", dest)


# this is to calculate which nodes are failing
# parameters: nodeAmount = amount of nodes
#            nodeProbs = probabilities that were assigned to each node to fail
#            failProb = the probabily of node failure based on user input
#            src = starting node
#            dest = ending node
# returns a list of the nodes that failed
def calculateFailure(nodeAmount, nodeProbs, failProb, src, dest):
    # calculates the amount of nodes that can fail
    failAmount = round(failProb / (1 / nodeAmount))

    # this randomly generates the nodes that could fail
    holder = {random.randint(0, nodeAmount) for x in range(0, failAmount)}
    failure = []

    # this goes through the nodes that could fail and if their probability is lower than the failProb, then the node
    # will be added to the fail list
    for x in holder:
        if nodeProbs[x - 1] < failProb and x != src: #and x != dest:
            failure.append(x)

    return failure


# this updates the path and graph based on the node failures
def update(graph, nodeAmount, nodeProbs, failProb, src, dest):
    print("Updates: ")

    # uses the calculateFailure to get the failed nodes
    failure = calculateFailure(nodeAmount, nodeProbs, failProb, src, dest)

    print("Nodes that failed: ", failure)

    # removes the nodes that failed from the graph
    graph.remove_nodes_from(failure)

    # finds the new shortest path
    findPath(graph, src, dest)


def main():
    # get user inputs
    n = nodeAmount()
    src = srcNode(n)
    dest = destNode(n)
    f = nodeFailure()

    # randomly generates a list of the probability of each node failing
    nodeProbs = np.random.rand(n)

    # generates the graph
    g = generateGraph(n)

    # finds the shortest path
    findPath(g, src, dest)

    # automatically does one case of failed nodes, so user can see what happens
    update(g, n, nodeProbs, f, src, dest)

    # will keep executing update until user enters a q
    q = ''
    while q != 'q':
        print('Enter q to exit, or enter any other key to continue to update the graph with failed nodes: ')
        q = input()
        if q != 'q':
            update(g, n, nodeProbs, f, src, dest)


if __name__ == "__main__":
    main()

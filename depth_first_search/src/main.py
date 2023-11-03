# source: https://www.scaler.com/topics/dfs-python/

def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively


if __name__ == "__main__":

    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    node = 4  # root node
    visited = [False]*len(graph)  # Make all nodes to False initially
    component = []
    dfs(node, graph, visited, component)
    print(f"Following is the Depth-first search: {component}")  # Print the answer
# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F', 'G'],
         'C': ['I'],
         'D': [],
         'E': [],
         'F': ['L'],
         'G': ['H'],
         'H': [],
         'K': [],
         'I': ['K', 'J'],
         'L': [],
         'J': []}


def bfs(graph, start, goal):
    explored = []
    if start in goal:
        print('Root node itself is goal')
        return 'success'

    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node in goal:
            print('Goal Found:', node)
            print('TRAVERSAL ORDER:')
            for v in explored:
                print(v, "->", end="")
            print(node)
            return "success"
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def main(goals, graph, start):
    tempstr = "string"
    for goal_ in goals:
        print(f"For goal {goal_}:")
        if type(bfs(graph, start, goal_)) != type(tempstr):
            print("No node Exists")
        print()


goal = []


def goal_input():
    while True:
        g = input("Press q if over or Enter Goal: ").upper()  # ['G', 'J']
        if g == 'Q':
            break
        goal.append(g)


graph_ = dict()


def take_tree(graph):
    temp = input("Enter node: ").upper()
    children = []
    while True:
        temp2 = input("Press q if no children or Enter Child: ").upper()
        if temp2 == 'Q':
            break
        children.append(temp2)

    graph[temp] = children
    for child in children:
        graph[child] = []
    flag = input("To add more nodes press Y: ").upper()
    if flag == 'Y':
        take_tree(graph)
    return graph


graph_ = take_tree(graph_)

goal_input()

print(graph_)
start = input('Enter starting node: ').upper()
main(goal, graph, start)

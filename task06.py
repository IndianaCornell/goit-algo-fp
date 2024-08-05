import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as patches

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_visualization(root):
    color_map = {}
    node_colors = {}
    stack = [(root, 0)]  
    level = 0

    while stack:
        node, level = stack.pop()
        if node:
            color = "#{:02x}{:02x}{:02x}".format(0, 255 - level * 50, level * 30)
            color_map[node.value] = color
            node_colors[node.value] = color
            
            # Додаємо дітей до стека
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

    return color_map


def bfs_visualization(root):
    color_map = {}
    node_colors = {}
    queue = [(root, 0)] 
    level = 0

    while queue:
        node, level = queue.pop(0)
        if node:
            color = "#{:02x}{:02x}{:02x}".format(0, 255 - level * 50, level * 30)
            color_map[node.value] = color
            node_colors[node.value] = color
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

    return color_map


def visualize_tree(root, colors, title):
    G = nx.DiGraph()
    pos = {}

    def add_edges(node, pos, x=0, y=0, layer=1):
        if node:
            G.add_node(node.value)
            pos[node.value] = (x, y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, pos, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, pos, x + 1 / layer, y - 1, layer + 1)
        return pos

    add_edges(root, pos)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=[colors.get(node, '#ffffff') for node in G.nodes], font_size=16, font_weight='bold', edge_color='gray')
    plt.title(title)
    plt.show()

# Тестове дерево
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# обхід у глибину
dfs_colors = dfs_visualization(root)
visualize_tree(root, dfs_colors, "DFS Visualization")

#обхід в ширину
bfs_colors = bfs_visualization(root)
visualize_tree(root, bfs_colors, "BFS Visualization")

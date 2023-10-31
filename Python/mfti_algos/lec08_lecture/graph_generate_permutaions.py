# Produced by ChatGPT and modified by myself.
# Importing required libraries
import networkx as nx
import matplotlib.pyplot as plt

# Function to build the graph based on the recursive nature of generate_permutations
def build_graph_with_permutations_final(N, M=-1, prefix=None, G=None, parent_name=None, pos=None, level=0, x_center=0.5, step=1, steps=None, backtracks=None):
    """Final graph building for generate_permutations with proper connections."""
    if G is None:
        G = nx.DiGraph()
        pos = {}
        steps = {}
        backtracks = []

    prefix = prefix or []
    node_name = ''.join(map(str, prefix))
    if not node_name:
        node_name = 'start'

    G.add_node(node_name)
    if parent_name is not None:
        G.add_edge(parent_name, node_name)
        steps[(parent_name, node_name)] = step
        step += 1

    pos[node_name] = (x_center, -level)

    M = N if M == -1 else M

    if M == 0:
        if parent_name:
            backtracks.append((node_name, parent_name, step))
            step += 1
        return G, pos, step, steps, backtracks

    child_spacing = 1 / (2 ** (len(prefix) + 2))
    next_child_center = x_center - (N - 1) * child_spacing

    for number in range(1, N + 1):
        if number in prefix:
            continue
        new_prefix = prefix + [number]
        G, pos, step, steps, backtracks = build_graph_with_permutations_final(
            N,
            M - 1,
            new_prefix,
            G,
            node_name,
            pos,
            level + 1,
            next_child_center,
            step,
            steps,
            backtracks
        )
        next_child_center += 2 * child_spacing

    if parent_name:
        backtracks.append((node_name, parent_name, step))
        step += 1

    return G, pos, step, steps, backtracks

# Function to draw arrows with adjusted labels
def draw_arrows_with_adjusted_labels(G, pos, ax, offset=0.03, vertical_shift=0.03):
    """Draw arrows with step numbers integrated horizontally and adjusted vertically."""
    arrow_length_ratio = 0.2  # Ratio to determine where the arrow breaks for the label

    # Define pairs of overlapping numbers to adjust vertically
    overlapping_pairs = [("4", "5"), ("10", "11"), ("18", "19"), ("24", "25")]

    for edge, step in steps.items():
        start_x, start_y = pos[edge[0]]
        end_x, end_y = pos[edge[1]]
        start_x -= offset
        end_x -= offset

        # Calculate intermediate points for breaking the arrow
        diff_x = end_x - start_x
        diff_y = end_y - start_y

        mid1_x = start_x + diff_x * (0.5 - arrow_length_ratio / 2)
        mid1_y = start_y + diff_y * (0.5 - arrow_length_ratio / 2)

        mid2_x = start_x + diff_x * (0.5 + arrow_length_ratio / 2)
        mid2_y = start_y + diff_y * (0.5 + arrow_length_ratio / 2)

        # Draw the broken arrow segments
        ax.annotate("", xy=(mid1_x, mid1_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="->", color='blue', shrinkA=0,
                                    shrinkB=0),
                    ha="right", va="center")
        ax.annotate("", xy=(end_x, end_y), xytext=(mid2_x, mid2_y),
                    arrowprops=dict(arrowstyle="->", color='blue', shrinkA=0,
                                    shrinkB=0),
                    ha="right", va="center")

        # Place the step number horizontally and adjust vertically if needed
        midpoint_x = (mid1_x + mid2_x) / 2
        midpoint_y = (mid1_y + mid2_y) / 2

        # Adjust vertical position for overlapping numbers
        if str(step) in [pair[0] for pair in overlapping_pairs]:
            midpoint_y -= vertical_shift
        elif str(step) in [pair[1] for pair in overlapping_pairs]:
            midpoint_y += vertical_shift

        ax.text(midpoint_x, midpoint_y, str(step), fontsize=12, color='blue',
                ha='center', va='center')

    # Draw backtracking arrows with the same approach
    for src, dst, step in backtracks:
        start_x, start_y = pos[src]
        end_x, end_y = pos[dst]
        start_x += offset
        end_x += offset

        # Calculate intermediate points for breaking the arrow
        diff_x = end_x - start_x
        diff_y = end_y - start_y

        mid1_x = start_x + diff_x * (0.5 - arrow_length_ratio / 2)
        mid1_y = start_y + diff_y * (0.5 - arrow_length_ratio / 2)

        mid2_x = start_x + diff_x * (0.5 + arrow_length_ratio / 2)
        mid2_y = start_y + diff_y * (0.5 + arrow_length_ratio / 2)

        # Draw the broken arrow segments
        ax.annotate("", xy=(mid1_x, mid1_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="->", color='red', ls='dashed',
                                    shrinkA=0, shrinkB=0),
                    ha="right", va="center")
        ax.annotate("", xy=(end_x, end_y), xytext=(mid2_x, mid2_y),
                    arrowprops=dict(arrowstyle="->", color='red', ls='dashed',
                                    shrinkA=0, shrinkB=0),
                    ha="right", va="center")

        # Place the step number horizontally and adjust vertically if needed
        midpoint_x = (mid1_x + mid2_x) / 2
        midpoint_y = (mid1_y + mid2_y) / 2

        # Adjust vertical position for overlapping numbers
        if str(step) in [pair[0] for pair in overlapping_pairs]:
            midpoint_y -= vertical_shift
        elif str(step) in [pair[1] for pair in overlapping_pairs]:
            midpoint_y += vertical_shift

        ax.text(midpoint_x, midpoint_y, str(step), fontsize=12, color='red',
                ha='center', va='center')

# Generate the graph for N=3
G, pos, _, steps, backtracks = build_graph_with_permutations_final(3)

# Plotting the graph
fig, ax = plt.subplots(figsize=(12, 9))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', ax=ax)
nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()}, font_size=15, ax=ax)
draw_arrows_with_adjusted_labels(G, pos, ax)

plt.title("Recursive Tree for generate_permutations")
plt.show()

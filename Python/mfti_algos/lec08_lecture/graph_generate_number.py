# Produced by ChatGPT and modified by myself.
import networkx as nx
import matplotlib.pyplot as plt


def build_graph_with_full_backtracking(N, M, prefix=None, G=None,
                                       parent_name=None, pos=None, level=0,
                                       x_center=0.5, step=1, steps=None,
                                       backtracks=None):
    """Build a graph to illustrate the recursive steps with full backtracking."""
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

    if M == 0:
        if parent_name:
            backtracks.append((node_name, parent_name, step))
            step += 1
        return G, pos, step, steps, backtracks

    left_child_center = x_center - 0.5 / (2 ** (len(prefix) + 1))
    right_child_center = x_center + 0.5 / (2 ** (len(prefix) + 1))

    for i, digit in enumerate(range(N)):
        new_prefix = prefix + [digit]
        child_center = left_child_center if i == 0 else right_child_center
        G, pos, step, steps, backtracks = build_graph_with_full_backtracking(
            N,
            M - 1,
            new_prefix,
            G,
            node_name,
            pos,
            level + 1,
            child_center,
            step,
            steps,
            backtracks
        )

    if parent_name:
        backtracks.append((node_name, parent_name, step))
        step += 1

    return G, pos, step, steps, backtracks


G, pos, _, steps, backtracks = build_graph_with_full_backtracking(2, 3)


# ... [Rest of the plotting code]


def draw_arrows_with_adjusted_labels(G, pos, ax, offset=0.03,
                                     vertical_shift=0.03):
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


# Plotting the graph with broken arrows and adjusted labels.
fig, ax = plt.subplots(figsize=(12, 9))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', ax=ax)
nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes()},
                        font_size=15, ax=ax)
draw_arrows_with_adjusted_labels(G, pos, ax)

plt.title("Recursive Tree with Adjusted Arrow Labels")
plt.show()

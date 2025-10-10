def display_tree_aux(node):
    if node.right is None and node.left is None:
        line = f"{node.val}"
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle
    
    if node.right is None:
        lines, n, p, x = display_tree_aux(node.left)
        s = f"{node.val}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    
    if node.left is None:
        lines, n, p, x = display_tree_aux(node.right)
        s = f"{node.val}"
        u = len(s)
        first_line = s + x * ' ' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    
    left, n, p, x = display_tree_aux(node.left)
    right, m, q, y = display_tree_aux(node.right)
    s = f"{node.val}"
    u = len(s)
    
    # Calculate proper spacing for centering
    gap = 2  # minimum gap between subtrees
    total_width = n + gap + m
    root_pos = n + gap // 2
    
    # Create the root line with proper centering
    first_line = ' ' * root_pos + s
    
    # Create connection lines
    left_connector_pos = x
    right_connector_pos = root_pos + u + (y - left_connector_pos)
    second_line = ' ' * left_connector_pos + '/' + ' ' * (root_pos - left_connector_pos - 1 + u) + '\\' + ' ' * (total_width - right_connector_pos - 1)
    
    # Pad shorter subtree
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    
    # Combine left and right subtrees
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + ' ' * gap + b for a, b in zipped_lines]
    return lines, total_width, max(p, q) + 2, root_pos


def print_tree(root):
    if root is None:
        print("Empty tree")
        return
    lines, *_ = display_tree_aux(root)
    for line in lines:
        print(line)
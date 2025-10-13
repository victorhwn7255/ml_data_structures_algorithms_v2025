def display_tree_aux(node):
    if not node:
        return [], 0, 0, 0
        
    if not node.left and not node.right:
        line = str(node.val)
        width = len(line)
        return [line], width, 1, width // 2
    
    if not node.right:
        lines, n, p, x = display_tree_aux(node.left)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    
    if not node.left:
        lines, n, p, x = display_tree_aux(node.right)
        s = str(node.val)
        u = len(s)
        first_line = s + x * ' ' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    
    left, n, p, x = display_tree_aux(node.left)
    right, m, q, y = display_tree_aux(node.right)
    s = str(node.val)
    u = len(s)
    
    gap = 2
    first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s + (y + 1) * ' ' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y + 1) * ' ' + '\\' + (m - y - 1) * ' '
    
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, (n + u) // 2


def print_tree(root):
    if root is None:
        print("Empty tree")
        return
    lines, *_ = display_tree_aux(root)
    for line in lines:
        print(line)
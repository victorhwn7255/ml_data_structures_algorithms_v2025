class TrieNode():
  def __init__(self):
    self.children = {}
    self.word = None

def findWords(board: list[list[str]], words: list[str]):
  rows = len(board)
  cols = len(board[0])
  root = TrieNode()
  for word in words:
    node = root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.word = word
  
  results = []
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  def dfs(r, c, node: TrieNode):
    char = board[r][c]
    if char not in node.children:
      return
    
    next_node: TrieNode = node.children[char]
    if next_node.word is not None:
      results.append(next_node.word)
      next_node.word = None
    
    board[r][c] = '#'
    for (dr, dc) in directions:
      nr, nc = r+dr, c+dc
      if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
        dfs(nr, nc, next_node)
    board[r][c] = char
    
    if not next_node.children and next_node.word is None:
      del node.children[char]
    
  for r in range(rows):
    for c in range(cols):
      if board[r][c] in root.children:
        dfs(r, c, root)
  
  return results


test_board_1 = [
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
test_words_1 = ["oath","pea","eat","rain"]
test_board_2 = [
  ["a","b"],
  ["c","d"]
]
test_words_2 = ["abcb"]

print(findWords(test_board_1, test_words_1))
print(findWords(test_board_2, test_words_2))
class TrieNode:
  def __init__(self):
    self.children = {}
    self.isEnd = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    current_node = self.root
    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char]
    
    current_node.isEnd = True
        
  def search(self, word: str) -> bool:
    current_node = self.root
    def dfs(node: TrieNode, index):
      if index == len(word):
        return node.isEnd
      current_char = word[index]
      if current_char == '.':
        for child in node.children.values():
          if dfs(child, index+1):
            return True
        return False
      else:
        if current_char not in node.children:
          return False
        return dfs(node.children[current_char], index+1)
      
    return dfs(current_node, 0)
  
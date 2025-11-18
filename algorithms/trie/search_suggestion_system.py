class Trie:
    def __init__(self):
        self.children = {}
        self.suggestions = []
    

def suggestedProducts(products: list[str], searchWord: str):
  products.sort()
  root = Trie()
  
  for word in products:
    node = root
    for char in word:
      if char not in node.children:
        node.children[char] = Trie()
      node = node.children[char]
      
      if len(node.suggestions) < 3:
        node.suggestions.append(word)
  
  result = []
  node = root
  
  for char in searchWord:
    if char in node.children:
      node = node.children[char]
      result.append(node.suggestions)
    else:
      result.append([])
      node.children = {}
    
  return result


test_products = ["mobile","mouse","moneypot","monitor","mousepad"]
test_search = "mouse"

print(suggestedProducts(test_products, test_search))
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]):
  if endWord not in wordList:
    return 0
  
  wordSet = set(wordList)
  queue = deque([(beginWord, 1)])
  
  while queue:
    current_word, steps = queue.popleft()
    if current_word == endWord:
      return steps
    
    for i in range(len(current_word)):
      for char in "abcdefghijklmnopqrstuvwxyz":
        if char == current_word[i]:
          continue
        new_word = current_word[:i] + char + current_word[i+1:]
        if new_word in wordSet:
          wordSet.remove(new_word)
          queue.append((new_word, steps+1))
          
  return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
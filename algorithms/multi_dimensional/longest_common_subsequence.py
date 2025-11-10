import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.visualize_db_table import visualize_dp

def longestCommonSubsequence(text1, text2):
  dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
  visualize_dp(dp, text1, text2)
  
  return text1

print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))
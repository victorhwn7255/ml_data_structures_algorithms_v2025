def visualize_dp(dp, text1="", text2=""):
    """Visualize the DP table with optional text labels"""
    
    # Print column headers (text2 characters)
    print("    ", end="")
    for char in " " + text2:
        print(f"{char:>3}", end="")
    print()
    
    # Print each row with row header (text1 characters)
    for i, row in enumerate(dp):
        # Row header
        if i == 0:
            print(" ", end="")
        else:
            print(text1[i-1], end="")
        print(" | ", end="")
        
        # Print row values
        for val in row:
            print(f"{val:>3}", end="")
        print()
def minFlips(self, a: int, b: int, c: int):
    flips = 0

    # Iterate over all 32 bits
    for i in range(32):
        abit = (a >> i) & 1
        bbit = (b >> i) & 1
        cbit = (c >> i) & 1

        if cbit == 1:
            # OR must be 1 → at least one of (a, b) is 1
            if abit == 0 and bbit == 0:
                flips += 1

        else:  # cbit == 0
            # OR must be 0 → both must be 0
            flips += abit + bbit

    return flips
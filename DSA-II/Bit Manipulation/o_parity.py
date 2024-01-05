# Create lookup table with parity of all 16-bit numbers
lookup_table = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]

def parity_using_lookup(num):
    # Extract 4 bits at a time and look up their parity in the table
    parity = lookup_table[num & 15]
    parity ^= lookup_table[(num >> 4) & 15]
    parity ^= lookup_table[(num >> 8) & 15]
    parity ^= lookup_table[(num >> 12) & 15]
    
    # Return final parity
    return parity

print(parity_using_lookup(255))
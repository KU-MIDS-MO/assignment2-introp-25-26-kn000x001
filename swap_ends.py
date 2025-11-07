def swap_ends(L, k):
    ### Replace with your own code (begin) ###
    if k <= 0 or len(L) == 0 or k > len(L) // 2:
        return (L.copy(), 0)
    
    new_list = L[-k:] + L[k:-k] + L[:k]
    num_swaps = k
    return (new_list, num_swaps)
    pass
    ### Replace with your own code (end)   ###

def has_adjacent_duplicate(L):
    ### Replace with your own code (begin) ###
    if len(L) <= 1:
        return False
    
    for i in range(len(L) -1):
        if L[i] == L[i+1]:
            return True
        i += 1
        
    return False
    pass
    ### Replace with your own code (end)   ###

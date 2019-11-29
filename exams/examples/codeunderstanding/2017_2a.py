def bin_search(liste, verdi, imin, imax): 
    if (imax < imin): 
        return False
    else: 
        imid = (imin + imax)
        if verdi < liste[imid]: 
            return bin_search(liste, verdi, imin, imid-1)
        elif verdi > liste[imid]: 
            return bin_search(liste, verdi, imid+1, imax)
        else: 
            return imid
def white_walkers(village):
    i = 0
    pairs_found = False
    
    while i < len(village) - 1:
        if village[i].isdigit():
            j = i + 1
            count = 0
            
            while j < len(village) and (village[j] == "=" or village[j].isalpha()):
                if village[j] == "=":
                    count += 1
                j += 1
                
            if j < len(village) and village[j].isdigit() and int(village[i]) + int(village[j]) == 10:
                if count != 3:
                    return False
                pairs_found = True
            
            i = j
        else:
            i += 1
    return pairs_found


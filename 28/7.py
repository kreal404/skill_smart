def WordSearch(max_len: int, s: str, subs: str) -> str:
    result = []
    
    lines = s.split("\n")
    for line in lines:
        words = line.split()
        new_lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) <= max_len:
                current_line += word + " "
            else:
                new_lines.append(current_line.strip())
                current_line = word + " "
        
        new_lines.append(current_line.strip())
        
        for new_line in new_lines:
            result.append(str(int(subs in new_line)))
    
    return " ".join(result)



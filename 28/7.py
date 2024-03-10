def WordSearch(max_len: int, s: str, subs: str) -> str:
    result = []

    lines = s.split("\n")
    for line in lines:
        words = line.split()
        new_lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) > max_len:
                if current_line:
                    new_lines.append(current_line.strip())
                    current_line = ""
            current_line += word + " "
            if len(current_line) - 1 == max_len:
                new_lines.append(current_line.strip())
                current_line = ""

        if current_line:
            new_lines.append(current_line.strip())

        for new_line in new_lines:
            words_in_line = new_line.split()
            result.append(str(int(subs in words_in_line)))

    return " ".join(result)


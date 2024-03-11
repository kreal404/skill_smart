def WordSearch(line_length: int, s: str, subs: str) -> list[int]:
    result = []

    words = s.split()
    new_lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            new_lines.append(current_line)
            current_line = word

    new_lines.append(current_line)

    for new_line in new_lines:
        result.append(int(subs in new_line.strip()))

    return result





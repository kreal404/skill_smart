def WordSearch(line_length: int, s: str, subs: str) -> list[int]:
    result = []

    words = s.split()
    new_lines = []
    current_line = ""

    for word in words:
        if len(word) > line_length:
            if current_line:
                new_lines.append(current_line)
            for i in range(0, len(word), line_length):
                new_lines.append(word[i:i+line_length])
            current_line = ""
        elif len(current_line) + len(word) + 1 <= line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            new_lines.append(current_line)
            current_line = word

    if current_line:
        new_lines.append(current_line)

    for new_line in new_lines:
        result.append(int(subs in new_line.split()))

    return result



def LineAnalysis(line):
    if line[0] != '*' or line[-1] != '*':
        return False

    segments = line.split("*")

    for i in range(2, len(segments) - 1):
        if segments[i] != segments[i-1]:
            return False

    return True


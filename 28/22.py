def SherlockValidString(s: str) -> bool:
    char_frequencies = {}
    for char in set(s):
        char_frequencies[char] = s.count(char)

    frequencies = sorted(list(char_frequencies.values()))
    max_freq = max(frequencies, key=frequencies.count)

    diff = 0

    for f in frequencies:
        diff += abs(f - max_freq)

    return diff <= 1


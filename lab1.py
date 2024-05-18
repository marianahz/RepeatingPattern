

def repeats(list):
    if list is None:
        return None
    
    n = len(list)
    longest = None
    # See if the pattern repeats

    def is_repeating(pattern):
        pattern_length = len(pattern)
        for i in range(pattern_length, n):
            if list[i] != pattern[i % pattern_length]:
                return False
        return True
    
    for pattern_length in range(1, n // 2 + 1):
        # Can the list be divided into patterns that are equal
        if n % pattern_length == 0:
            pattern = list[: pattern_length]
            if is_repeating(pattern) and (longest is None or pattern_length > len(longest)):
                longest = pattern
                return pattern
    return longest

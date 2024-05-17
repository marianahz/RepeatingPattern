

def repeats(list):
    if list is None:
        return None
    
    n = len(list)
    longest = None
    # See if the pattern repeats

    def isRepeating(pattern):
        patternLength = len(pattern)
        for i in range(patternLength, n):
            if list[i] != pattern[i % patternLength]:
                return False
        return True
    
    for patternLength in range(1, n // 2 + 1):
        # Can the list be divided into patterns that are equal
        if n % patternLength == 0:
            pattern = list[: patternLength]
            if isRepeating(pattern) and (longest is None or patternLength > len(longest)):
                longest = pattern
                return pattern
    return longest

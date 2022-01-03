
def string_pattern_search(text, pattern):
    i = 0
    n = len(text)
    m = len(pattern)

    while i <= n - m:
        j = 0
        while (j < m and text[i + j] == pattern[j]):
            j = j + 1

        if j == m:
            return i

        i+= 1

    return -1

def main():
    st1 = "I am Ben!"
    st2 = "Ben"
    print("string_pattern_search return :", string_pattern_search(st1, st2))

    """
    string_pattern_search return : 5
    """

if __name__ == "__main__":
    main()
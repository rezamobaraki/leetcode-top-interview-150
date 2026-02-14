def is_subsequence(s: str, t: str) -> bool:
    s_ptr, t_ptr = 0, 0

    # Traverse t with t_ptr and s with s_ptr
    while t_ptr < len(t):
        if s_ptr < len(s) and s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    return s_ptr == len(s)


if __name__ == '__main__':
    s, t = "abc", "ahbgdc"
    print(is_subsequence(s, t))  # True

    s, t = "axc", "ahbgdc"
    print(is_subsequence(s, t))  # False


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        if s[i] in s_map:
            if s_map[s[i]] != t[i]:
                return False
        else:
            s_map[s[i]] = t[i]

        if t[i] in t_map:
            if t_map[t[i]] != s[i]:
                return False
        else:
            t_map[t[i]] = s[i]

    return True

def is_isomorphic_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map, t_map = {}, {}

    for i in range(len(s)):
        if s_map.get(s[i], t[i]) != t[i] or t_map.get(t[i], s[i]) != s[i]:
            return False
        s_map[s[i]] = t[i]
        t_map[t[i]] = s[i]
    return True

if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(is_isomorphic(s, t))  # True

    s = "foo"
    t = "bar"
    print(is_isomorphic(s, t))  # False

    s = "paper"
    t = "title"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "aa"
    print(is_isomorphic(s, t))  # False

    s = "ab"
    t = "ca"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "cb"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "cc"
    print(is_isomorphic(s, t))  # False

    s = "ab"
    t = "cd"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "ef"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "fg"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "gh"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "hi"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "ij"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "jk"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "kl"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "lm"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "mn"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "no"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "op"
    print(is_isomorphic(s, t))  # True

    s = "ab"
    t = "pq"
    print(is_isomorphic(s, t))  # True
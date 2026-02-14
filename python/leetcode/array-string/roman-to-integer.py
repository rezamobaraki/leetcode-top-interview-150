romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(s: str) -> int:
    total = 0
    pointer = len(s) - 1
    while pointer >= 0:
        if pointer > 0 and romans[s[pointer]] > romans[s[pointer - 1]]:
            total += romans[s[pointer]] - romans[s[pointer - 1]]
            pointer -= 2
        else:
            total += romans[s[pointer]]
            pointer -= 1
    return total


def roman_to_int_v2(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if i < len(s) - 1 and romans[s[i]] < romans[s[i + 1]]:
            result -= romans[s[i]]
        else:
            result += romans[s[i]]


    return result


if __name__ == '__main__':
    # s1 = 'III'
    # print(roman_to_int(s1))  # Output: 3
    #
    # s2 = 'IV'
    # print(roman_to_int(s2))  # Output: 4
    #
    # s3 = 'IX'
    # print(roman_to_int(s3))  # Output: 9
    #
    # s4 = 'LVIII'
    # print(roman_to_int(s4))  # Output: 58

    s5 = 'MCMXCIV'
    print(roman_to_int_v2(s5))  # Output: 1994


def roman_numerals(string):
    total = 0
    if len(string) == 0:
        return total
    string = string.upper()
    roman_hash = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in range(0,len(string) - 1):
        if string[i] not in roman_hash:
            raise Exception("String includes invalid roman numeral")
        left = roman_hash[string[i]]
        right = roman_hash[string[i+1]]
        if left < right:
            total -= left
        else:
            total += left
    total += roman_hash[string[len(string) - 1]]
    return total


if __name__ == "__main__":
    romans = "MMMDCCXXIV"
    result = roman_numerals(romans)
    print(result)

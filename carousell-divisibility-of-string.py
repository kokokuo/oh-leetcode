

"""
The small project use the pipenv to build enviroment and write the code by python 3.7
"""


def DivisibilityOfString(s: str, t: str) -> int:
    # i is the index of t, smallest is the smallest size and means the end of compared location
    i = 0
    smallest = 1
    match = None
    while(i < smallest):
        j = 0
        # j is the index of s string
        while(j < len(s)):
            print(f"i = {i}, j = {j}, t[{i}] = {t[i]}, s[{j}] = {s[j]}")
            # if match, then move to the next index of s to compared
            if t[i] == s[j]:
                match = True
                j += 1
                # the index of i move too ( if i is still not reach to smallest location)
                if smallest > i + 1:
                    i += 1
                else:
                    # or set to start location, means to compare to char text
                    i = 0
            else:
                # not matched, then we move smallest to the next char.
                match = False
                smallest += 1
                break
        # If the s string has travered, or smallest has been larger than size of t
        # it's time to leave traverse loop and check the final result
        if j == len(s) or smallest > len(t):
            break
    if match:
        return smallest
    return -1


if __name__ == "__main__":
    output = DivisibilityOfString("rbrb", "rbrb")
    print(output)
    output = DivisibilityOfString("lrbb", "lrbb")
    print(output)
    output = DivisibilityOfString("lrbb", "lrdc")
    print(output)

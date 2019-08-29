

def firstOccurrence(src, pattern):
    # Write your code here
    start = i = j = 0
    match = False
    while(i != len(pattern) - 1):
        print("start = ", start, ", patetrn char = ", pattern[i])
        while(j < len(src)):
            # 如果為不為星號
            # 有匹配到
            if pattern[i] == "*" or pattern[i] == src[j]:
                if not match:
                    start = j
                match = True
                i += 1
                # 有匹配到，且先前匹配過了，則跳過
            else:
                match = False
                if i > 0:
                    i -= 1
            print("src char =", src[j], ", j = ", j, ",match = ", match)
            j += 1
            if match:
                break
        print("break => j =", j)
        if j >= len(src):
            break
    if not match:
        return -1
    return start


if __name__ == "__main__":
    print("result = ", firstOccurrence("xabcdey", "ab*de"))
    print("========")
    print("result = ", firstOccurrence("juliasamanthantjulia", "ant"))
    print("========")
    print("result = ", firstOccurrence("juliasamanthantjulia", "bbb"))

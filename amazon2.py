def videocut(liststring):
    unique = []
    location = []
    result = []
    for m in liststring:
        if m in unique:
            pass
        else:
            unique.append(m)

    for l,str in enumerate(liststring):
        single = [l,str]
        location.append(single)

    left = 0
    right = 0

    print(location)
    for x in range(0, len(liststring)):
        for ele in location:
            if liststring[x] == ele[1]:
                right = max(right, ele[0])
                if right == x and right-left != 0 and right-left > 0:
                    result.append(right - left + 1)
                    left = right +1
    return result

if __name__ == "__main__":
    teststring = "abcdaefghije"
    test = ["z", "z", "c", "b", "z", "c", "h", "f", "i", "h", "i"]
    print(videocut(test))
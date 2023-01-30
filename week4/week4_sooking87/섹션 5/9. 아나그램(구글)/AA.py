str1 = list(map(str, input()))
str2 = list(map(str, input()))

if len(str1) != len(str2):
    print("NO")
else:
    while str1:
        if str1[0] in str2:
            str2.remove(str1[0])
            str1.pop(0)
        else:
            print("NO")
            break
    if len(str1) == 0:
        print("YES")

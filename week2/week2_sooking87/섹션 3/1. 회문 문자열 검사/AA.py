n = int(input())

for i in range(n):
    word = input()
    word = word.lower()
    lenWord = len(word) - 1
    isSame = True
    for j in range(lenWord):
        if word[j] != word[len(word) - 1 - j]:
            isSame = False

    if isSame:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))

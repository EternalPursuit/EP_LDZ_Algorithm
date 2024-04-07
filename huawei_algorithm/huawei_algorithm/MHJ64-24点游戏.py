def cal_tar(s, res):
    if len(s) == 1:
        return s[0] == res
    for i in range(len(s)):
        word_only = s[i]
        rest = s[:i] + s[i + 1:]
        if cal_tar(rest, res + word_only) \
                or cal_tar(rest, res - word_only) \
                or cal_tar(rest, res / word_only) \
                or cal_tar(rest, res * word_only):
            return True

    return False


while True:
    try:
        s_tar = list(map(int, input().split()))
        if cal_tar(s_tar, 24):
            print("true")
        else:
            print("false")
    except:
        break
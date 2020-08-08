def b(in1):
    spl = in1.split("/n")
    paths = [0] * (len(spl) + 1)
    longest = 0
    paths[0] = 0
    for x in spl:
        print(x)
        tCount = x.count("/t")
        curLength = paths[tCount] + len(x) - (2 * tCount) + 1
        paths[tCount + 1] = curLength

        if "." in x:
            longest = max(longest, curLength - 1)

    return str(longest)


in1 = "dir/n/tsubdir1/n/t/tfile1.ext/n/t/tsubsubdir1/n/tsubdir2/n/t/tsubsubdir2/n/t/t/tfile2.ext"
print(b(in1))
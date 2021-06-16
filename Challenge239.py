"""
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

    All of its keys must be distinct.
    It must not connect two keys by jumping over a third key, unless that key has already been used.

For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""
def Solution(N):
    jump = [[0 for i in range(10)] for j in range(10)];
    jump[1][3] = jump[3][1] = 2
    jump[7][9] = jump[9][7] = 8
    jump[1][7] = jump[7][1] = 4
    jump[3][9] = jump[9][3] = 6
    jump[1][9] = jump[9][1] = jump[2][8] = jump[8][2] = jump[3][7] = jump[7][3] = jump[4][6] = jump[6][4] = 5
    visit = [False] * 10
    ways = 0
    for i in range(1, N + 1):
        ways += 4 * TotalPattern(visit, jump, 1, i - 1)
        ways += 4 * TotalPattern(visit, jump, 2, i - 1)
        ways += TotalPattern(visit, jump, 5, i - 1)
    return ways

def TotalPattern(visit, jump, cur, next):
    if next <= 0:
        if next == 0:
            return 1
        else:
            return 0

    ways = 0
    visit[cur] = True

    for i in range(1, 10):
        if (visit[i] == False and (jump[i][cur] == 0 or visit[jump[i][cur]])):
            ways += TotalPattern(visit, jump, i, next - 1);
    visit[cur] = False
    return ways

print(Solution(9))
MAX_CHAR = 26
def runCustomerSimulation(n, seq):
    seen = [0] * MAX_CHAR
    res = 0
    occupied = 0
    for i in range(len(seq)):
        ind = ord(seq[i]) - ord('A')
        if seen[ind] == 0:
            seen[ind] = 1
            if occupied < n:
                occupied += 1
                seen[ind] = 2
            else:
                res += 1
        else:
            if seen[ind] == 2:
                occupied -= 1
            seen[ind] = 0

    return res

print(runCustomerSimulation(1, "ABCBCADEED"))

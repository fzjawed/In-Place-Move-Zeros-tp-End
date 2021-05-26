#creds to cs_abhi on binarysearch
class Solution:
    def solve(self, a):
        j = 0
        for i in range(len(a)):
            if a[i] != 0:
                a[j] = a[i]
                j += 1
        while j < len(a):
            a[j] = 0
            j += 1
        return a

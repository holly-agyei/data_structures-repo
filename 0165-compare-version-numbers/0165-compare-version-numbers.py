from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")

        for i,j in zip_longest(arr1,arr2, fillvalue = "0"):
            if int(i)>int(j):
                return 1
            elif int(i)<int(j):
                return -1
        return 0
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nn = n
        sm = 0
        prod = 1
        i = 0
        arr = []
        while n >= 10:
            arr.append(int(n % 10))
            n /= 10
        arr.append(int(n))
        while i < len(arr):
            sm = int(sm + arr[i])
            prod = int(prod * arr[i])
            i += 1
        return True if nn % (sm + prod) == 0 else False
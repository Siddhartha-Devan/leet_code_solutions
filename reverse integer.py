class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        y = str(y)
        y = y[::-1]
        y = int(y)
        if x<0:
            y = y*-1
            r = 2147483648*-1
            if y < r:
                return 0
            return y
        if y>2147483647:
            return 0
        return y


        
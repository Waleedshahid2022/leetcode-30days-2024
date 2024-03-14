class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):  #32-bit integer
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

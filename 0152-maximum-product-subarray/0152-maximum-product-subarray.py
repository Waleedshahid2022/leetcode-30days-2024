
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_product = float('-inf')
        current_product = 1

        for num in nums:
            current_product *= num
            max_product = max(max_product, current_product)
            if num == 0:
                current_product = 1

        current_product = 1
        for num in reversed(nums):
            current_product *= num
            max_product = max(max_product, current_product)
            if num == 0:
                current_product = 1

        return max_product



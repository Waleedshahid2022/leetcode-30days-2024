class Solution(object):
    def productExceptSelf(self, nums):
        leftProd = [1] * len(nums)
        rightProd = [1] * len(nums)

        # Calculate the left product for each element
        for i in range(1, len(nums)):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]

        # Calculate the right product for each element
        for i in range(len(nums) - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * nums[i + 1]

        # Multiply corresponding elements of both lists
        for i in range(len(nums)):
            nums[i] = leftProd[i] * rightProd[i]

        return nums
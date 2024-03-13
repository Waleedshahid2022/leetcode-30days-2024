class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        requriedNumbers = len(nums)+1
        if(not(len(nums)==requriedNumbers)):
            check = [False]*requriedNumbers
            for i in nums:
                check[i]=True

            indexOfMissing = check.index(False)

            return indexOfMissing
        else:
            pass
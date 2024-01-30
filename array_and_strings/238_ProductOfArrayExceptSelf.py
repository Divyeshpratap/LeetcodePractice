'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preCumProduct = [1]
        postCumProduct = [1]
        revNums = nums[::-1]
        prodList = [0] * len(nums)
        for i in range(1, len(nums)):
            preCumProduct.append(nums[i - 1] * preCumProduct[i - 1])
            postCumProduct.append(revNums[i - 1] * postCumProduct[i - 1])
        postCumProduct = postCumProduct[::-1]
        print(f'Prefix Cumulative list is {preCumProduct}')
        print(f'Postfix Cumulative list is {postCumProduct}')

        for i in range(len(nums)):
            prodList[i] = preCumProduct[i] * postCumProduct[i]
        return prodList
'''
Time Complexity: O(N)
Space Complexity: O(N)
'''

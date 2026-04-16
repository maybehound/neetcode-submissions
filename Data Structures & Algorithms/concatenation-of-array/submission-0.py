class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nlist = nums
        for i in range(len(nums)):
            nlist.append(nums[i])
        return nlist
            
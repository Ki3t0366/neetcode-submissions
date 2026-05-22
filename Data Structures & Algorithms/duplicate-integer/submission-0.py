class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = set()
        for i in nums:
            if i not in tmp:
                tmp.add(i)
            elif i in tmp:
                return True



        return False


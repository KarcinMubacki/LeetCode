class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_ = dict()
        i, len_ = 0, len(nums)
        while i < len_:
            if hash_.get(nums[i], 0):
                return True
            hash_[nums[i]] = 1
            i += 1
        return False
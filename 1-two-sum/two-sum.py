class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = dict()
        for i in range(len(nums)):
            if hash_.get(nums[i]) is not None:
                return [i, hash_.get(nums[i])]
            hash_[target - nums[i]] = i
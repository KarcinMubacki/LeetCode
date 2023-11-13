class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        frequency = [[] for i in range(len(nums) + 1)]

        for number in nums:
            counter[number] = 1 + counter.get(number, 0)
        for number, count in counter.items():
            frequency[count].append(number)
        
        ret, len_res = [], 0
        for count in range(len(nums), -1, -1):
            if len_res == k:
                return ret
            if frequency[count]:
                ret += frequency[count]
                len_res += len(frequency[count])
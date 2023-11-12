class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ = dict()
        for string in strs:
            key = ''.join(sorted(string))
            if hash_.get(key, 0):
                hash_[key].append(string)
            else:
                hash_[key] = [string]
        return hash_.values()
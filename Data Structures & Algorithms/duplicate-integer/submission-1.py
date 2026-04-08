class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        truearr = set()
        for v in nums:
            if v  not in  truearr:
                truearr.add(v)
            elif v in truearr:
                return True
        
        return False
        
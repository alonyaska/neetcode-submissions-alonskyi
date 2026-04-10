class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            currents_num = nums[i]
            diff = target  - currents_num

            if diff in seen:
                return [seen[diff], i]


            seen[currents_num] = i
    


        
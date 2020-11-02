

class Solution:

    @staticmethod
    def twoSum(nums, target):
        value_index_map = {}

        for index, value in enumerate(nums):
            current_target = target - value
            if current_target in value_index_map:
                return [index, value_index_map[current_target]]

            value_index_map[value] = index

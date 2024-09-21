from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_indexes = sorted(range(len(nums)), key=lambda x: nums[x])
        # sorted_value = sorted(nums)

        first_index = 0
        while first_index < len(sorted_indexes) - 3:
            if first_index == 0 or nums[sorted_indexes[first_index - 1]] != nums[sorted_indexes[first_index]]:
                second_index = first_index + 1
                while second_index < len(sorted_indexes) - 2:
                    if (second_index == first_index + 1 or nums[sorted_indexes[second_index - 1]] != nums[
                        sorted_indexes[second_index]]):
                        left_index = second_index + 1
                        right_index = len(sorted_indexes) - 1
                        two_sum = nums[sorted_indexes[first_index]] + nums[sorted_indexes[second_index]]

                        while left_index < right_index:
                            four_sum = two_sum + nums[sorted_indexes[left_index]] + nums[sorted_indexes[right_index]]
                            if four_sum < target:
                                left_index += 1
                            elif four_sum > target:
                                right_index -= 1
                            else:
                                result.append([nums[sorted_indexes[first_index]], nums[sorted_indexes[second_index]],
                                               nums[sorted_indexes[left_index]], nums[sorted_indexes[right_index]]])

                                increment = 1
                                while left_index + increment < right_index and nums[sorted_indexes[left_index]] == nums[
                                    sorted_indexes[left_index + increment]]:
                                    increment += 1
                                left_index += increment

                                decrement = 1
                                while right_index - decrement > left_index and nums[sorted_indexes[right_index]] == \
                                        nums[sorted_indexes[right_index - decrement]]:
                                    decrement += 1
                                right_index -= decrement

                    second_index += 1
            first_index += 1

        return result

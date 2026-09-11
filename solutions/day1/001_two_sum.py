"""
LeetCode 1: Two Sum
Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Time Complexity: O(n) - We iterate through the list once
Space Complexity: O(n) - We store up to n elements in the hash map
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map for O(1) lookup.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers
        """
        # Hash map to store number -> index mapping
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement we need to reach target
            complement = target - num
            
            # If complement exists in our map, we found the solution
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number's index for future lookups
            num_map[num] = i
        
        # According to problem constraints, this line should never be reached
        return []

# Alternative brute force solution for comparison (O(n^2) time, O(1) space)
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach - check all pairs.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2]
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")  # Expected: [0, 1]
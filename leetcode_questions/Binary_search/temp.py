from typing import List


class Solution:
    def __init__(self):
        self.first = 0
        self.last = 0

    def test_location(self, cards, query, mid, hi):
        mid_number = cards[mid]
        if mid_number == query:
            if mid - 1 >= 0 and cards[mid - 1] == query:
                self.last = mid
                self.first = mid - 1
                return "left"
            if mid + 1 <= hi and cards[mid + 1] == query:
                self.last = mid + 1
                self.first = mid
                if mid + 1 == hi:
                    return "found"
                return "right"
            else:
                self.first,self.last=mid,mid
                return "found"
        elif mid_number < query:
            return "right"
        else:
            return "left"

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        if hi == 0:
            return [self.first, self.last]
        while lo <= hi:
            mid = (lo + hi) // 2
            result = self.test_location(nums, target, mid, hi)
            if result == "found":
                return [self.first, self.last]
            elif result == "right":
                lo = mid + 1
            elif result == "left":
                hi = mid - 1
            elif result == "special":
                lo = mid + 2

        return [-1, -1]


# Create an instance of the Solution class
sol = Solution()

# Define the test case
nums = [1,4,4,4]
target = 4

# Call the searchRange method and print the result
result = sol.searchRange(nums, target)
print(result)  # Expected output: [0, 0]

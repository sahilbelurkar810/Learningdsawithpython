from jovian.pythondsa import evaluate_test_cases
from jovian.pythondsa import evaluate_test_case
def count_rotation_linear(nums):
    if not nums:  # Handle empty array
        return 0

    length = len(nums)

    # Check if the array is sorted in descending order
    if all(nums[i] >= nums[i + 1] for i in range(length - 1)):
        return 0  # Return 0 for descending order

    position = 0

    # Check for the number of rotations
    while position < length:
        # If we find the point where current element is less than the previous one
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1

    return 0  # If array is already sorted


test_cases = [
    {"input": {"nums": [1, 2, 3, 4, 5]}, "output": 0},  # No Rotation (Original Array)
    {"input": {"nums": [5, 1, 2, 3, 4]}, "output": 1},  # Single Rotation
    {"input": {"nums": [3, 4, 5, 1, 2]}, "output": 3},  # Multiple Rotations (Midway)
    {
        "input": {"nums": [1, 2, 3, 4, 5]},
        "output": 0,
    },  # Full Rotation (Back to Original)
    {"input": {"nums": [2, 3, 4, 5, 1]}, "output": 4},  # Reverse Rotation
    {"input": {"nums": [1]}, "output": 0},  # Single Element Array
    {"input": {"nums": []}, "output": 0},  # Empty Array
    {"input": {"nums": [4, 5, 1, 2, 3]}, "output": 2},  # Rotated Twice
    {
        "input": {"nums": [3, 3, 3, 1, 3, 3]},
        "output": 3,
    },  # Array with Repeating Elements
    {
        "input": {"nums": [5, 4, 3, 2, 1]},
        "output": 0,
    },  # Array Sorted in Descending Order
]
result = evaluate_test_cases(count_rotation_linear,test_cases)
print(result)

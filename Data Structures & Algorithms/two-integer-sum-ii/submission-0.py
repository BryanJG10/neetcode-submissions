class Solution:
    # Define a function that finds two numbers that add up to the target.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Start the left pointer at the beginning of the array.
        left = 0

        # Start the right pointer at the end of the array.
        right = len(numbers) - 1

        # Continue searching while the two pointers have not crossed.
        while left < right:

            # Add the numbers currently pointed to by left and right.
            current_sum = numbers[left] + numbers[right]

            # Check if the two numbers add up to the target.
            if current_sum == target:

                # Return the positions using 1-based indexing.
                return [left + 1, right + 1]

            # If the sum is too small, we need a larger number.
            elif current_sum < target:

                # Move the left pointer right to increase the sum.
                left += 1

            # Otherwise, the current sum is greater than the target.
            else:

                # Move the right pointer left to decrease the sum.
                right -= 1
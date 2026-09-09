class Solution: 

    def twoSum(self, nums: list[int], target: int) -> list[int]:
# Nums is the list of numbers and target is the value we want two numbers to add up to.

        prevMap = {}
# Creates an empty dictionary called prevMap. Store each number we have already visited as the key and that number's index as the value.

        for i, num in enumerate(nums):
# Loops through every number in nums. i represents the current index. num represents the value stored at that index.

            difference = target - num
# Calculates the number we would need to add to the current number in order to reach the target.

            if difference in prevMap:
# Checks whether the number we need has already appeared earlier in the array and was stored in the dictionary.

                return [prevMap[difference], i]
# If the needed number exists, return its saved index along with the index of the current number. These are the two indices whose values add up to target.

            prevMap[num] = i
# If we did not find a match yet, store the current number and its index in the dictionary so it can be used later.

        return []
# Returns an empty list if no pair is found. The problem guarantees a valid pair, so this normally will not execute.
        